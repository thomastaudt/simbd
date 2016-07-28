
import capi

class EvolutionError(Exception): 
    pass

class Simulation(object):

    def __init__( self,
                  concentrations,
                  influx,
                  a_rates = None,
                  b_rates = None,
                  t0 = 0.
                ):

        # Use default rates that converge to LSW without influx
        if a_rates == None:
            pass
        if b_rates == None:
            pass

        self.cptr = capi.lib.bd_init_simulation( concentrations.size, 
                                                 concentrations, 
                                                 a_rates, b_rates, 
                                                 influx
                                               )

        if self.cptr == None:
            raise MemoryError( "Library '%s' could not allocate memory " + \
                               "in bd_init_simulation." % capi.lib_name )

        self._as_parameter_ = self.cptr

        self.time = t0



    def __del__(self):
        # free the memory allocated by librampr-core.so
        capi.lib.bd_free_simulation(self)

    def evolve_rkck( self, 
                     steps = 1, 
                     until_time = None, 
                     until_cmax = None, 
                     initial_dt = None, 
                     error_tolerance = None
                   ):

        if initial_dt:      self.target_dt       = initial_dt
        if error_tolerance: self.error_tolerance = error_tolerance
        if not until_cmax:  until_cmax = -1

        if until_cmax and not until_time:
            raise EvolutionError("Must also specify until_time when using until_cmax")

        if until_time:
            res = capi.lib.bd_rkck_evolution_until(self, until_time, until_cmax)

        else:
            for step in range(steps):
                res = capi.lib.bd_rkck_evolution_single(self)
                if res < 0: break

        if res < 0: 
            raise EvolutionError("%s" % self.error_message)


    @property
    def N(self):
        return capi.lib.bd_get_max_cluster_size(self)

    @property
    def c(self):
        return np.ctypeslib.as_array(capi.lib.bd_get_concentrations(self), (self.N,))

    @property
    def a(self):
        return np.ctypeslib.as_array(capi.lib.bd_get_a_rates(self), (self.N,))

    @property
    def b(self):
        return np.ctypeslib.as_array(capi.lib.bd_get_b_rates(self), (self.N,))

    @property
    def influx(self):
        return capi.lib.bd_get_influx(self)

    @influx.setter
    def influx(self, val):
        capi.lib.bd_set_influx(self, val)

    @property
    def time(self):
        return capi.lib.bd_get_time(self)

    @time.setter
    def time(self, val):
        capi.lib.bd_set_time(self, val)

    @property
    def target_dt(self):
        return capi.lib.bd_get_target_dt(self)

    @target_dt.setter
    def target_dt(self, val):
        capi.lib.bd_set_target_dt(self, val)

    @property
    def nr_steps(self):
        return capi.lib.bd_get_nr_steps(self)

    @property
    def nr_failed_adaptions(self):
        return capi.lib.bd_get_nr_failed_adaptions(self)

    @property
    def error_tolerance(self):
        return capi.lib.bd_get_error_tolerance(self)

    @error_tolerance.setter
    def error_tolerance(self, val):
        return capi.lib.bd_set_error_tolerance(self, val)


    @property
    def error_message(self):
        return capi.lib.rampr_get_error_message(self)
