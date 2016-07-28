
# Makes the functions in libsimbd.so available in python

from os import path
from numpy import ctypeslib, float64
import ctypes

#
# Define types and variables
#

# Introduce the ctypes types needed
_uint      = ctypes.c_uint
_int       = ctypes.c_int
_double    = ctypes.c_double
_char_p    = ctypes.c_char_p
_void_p    = ctypes.c_void_p
_void      = None
_float_vec = ctypeslib.ndpointer( dtype=float64, 
                                  ndim=1, 
                                  flags='C_CONTIGUOUS'
                                )


# Load the c library librampr-core.so
module_dir = path.dirname(path.abspath(__file__))
lib_dir    = path.join(module_dir, '..', 'lib')
lib_name   = "libsimbd.so"
lib        = ctypeslib.load_library(lib_name, lib_dir)



lib.bd_init_simulation.argtypes           = [ _int, _float_vec, _float_vec, _float_vec, _double ]
lib.bd_init_simulation.restype            = _void_p

lib.bd_free_simulation.argtypes           = [ _void_p ]
lib.bd_free_simulation.restype            = _void


lib.bd_rkck_evolution_until.argtypes      = [ _void_p, _double, _double ]
lib.bd_rkck_evolution_until.restype       = _int

lib.bd_rkck_evolution_single.argtypes     = [ _void_p ]
lib.bd_rkck_evolution_single.restype      = _int


lib.bd_get_max_cluster_size.argtypes      = [ _void_p ]
lib.bd_get_max_cluster_size.restype       = _int

lib.bd_get_concentrations.argtypes        = [ _void_p ]
lib.bd_get_concentrations.restype         = ctypes.POINTER(_double)

lib.bd_get_a_rates.argtypes               = [ _void_p ]
lib.bd_get_a_rates.restype                = ctypes.POINTER(_double)

lib.bd_get_b_rates.argtypes               = [ _void_p ]
lib.bd_get_b_rates.restype                = ctypes.POINTER(_double)


lib.bd_set_a_rates.argtypes               = [ _void_p, _float_vec ]
lib.bd_set_a_rates.restype                = _void

lib.bd_set_b_rates.argtypes               = [ _void_p, _float_vec ]
lib.bd_set_b_rates.restype                = _void

lib.bd_get_influx.argtypes                = [ _void_p ]
lib.bd_get_influx.restype                 = _double

lib.bd_set_influx.argtypes                = [ _void_p, _double ]
lib.bd_set_influx.restype                 = _void

lib.bd_get_time.argtypes                  = [ _void_p ]
lib.bd_get_time.restype                   = _double

lib.bd_set_time.argtypes                  = [ _void_p, _double ]
lib.bd_set_time.restype                   = _void

lib.bd_get_target_dt.argtypes             = [ _void_p ]
lib.bd_get_target_dt.restype              = _double

lib.bd_set_target_dt.argtypes             = [ _void_p, _double ]
lib.bd_set_target_dt.restype              = _void

lib.bd_get_nr_failed_adaptions.argtypes   = [ _void_p ]
lib.bd_get_nr_failed_adaptions.restype    = _int

lib.bd_get_nr_steps.argtypes              = [ _void_p ]
lib.bd_get_nr_steps.restype               = _int


lib.bd_get_error_message.argtypes        = [ _void_p ]
lib.bd_get_error_message.restype         = _char_p

lib.bd_get_error_tolerance.argtypes      = [ _void_p ]
lib.bd_get_error_tolerance.restype       = _double 

lib.bd_set_error_tolerance.argtypes      = [ _void_p, _double ]
lib.bd_set_error_tolerance.restype       = _void
