

#ifndef __SIMBD
#define __SIMBD


#include <math.h>
#include <stdlib.h>
#include <stdio.h>


#define BD_DEFAULT_TARGET_DT 1e-6


//
// A Becker-Döring simulation of maximal cluster size N
//

struct bd_simulation_t {
    
    // Cluster size
    int N;

    // Concentrations, reaction-rates, and decay-rates
    double * c;
    double * a_rates;
    double * b_rates;

    // Influx rate of monomers
    double influx;

    // Current time and proposal for the next dt
    double time;
    double target_dt;

    // Some information to evaluate the algorithms efficiency
    unsigned nr_failed_adaptions;
    unsigned nr_steps;

    double error_tolerance;

    // Somewhere to place error messages
    char error_message[1024];
};




int bd_rkck_routine( double dt, const double * c, const double * a_rates, double * b_rates, 
                      double influx, unsigned N, double * dcout, double * dcerr, double ** buffers );

int bd_rkck_step( struct bd_simulation_t * sim, double max_dt, double * dcout, double * dcerr, double ** buffers );

int bd_rkck_evolution_until( struct bd_simulation_t * sim, double until_time, double until_cmax );

int bd_rkck_evolution_single( struct bd_simulation_t * sim );



#endif // __SIMBD
