
#include "simbd.h"

struct bd_simulation_t * bd_init_simulation( int N, 
                                             const double * concentrations, 
                                             const double * a_rates,
                                             const double * b_rates,
                                             double influx
                                           ) {
    //
    // Memory allocation
    //

    struct bd_simulation_t * sim = malloc( sizeof(struct bd_simulation_t) );
    if ( sim == NULL ) return NULL;

    sim->c       = malloc( sizeof(double) * N );
    sim->a_rates = malloc( sizeof(double) * N );
    sim->b_rates = malloc( sizeof(double) * N );

    if ( sim->c == NULL || sim->a_rates == NULL || sim->b_rates == NULL ) {
        free( sim->c ); free( sim->a_rates ); free( sim->b_rates );
        free( sim );
        return NULL;
    }

    //
    // Initialize variables
    //
    
    for ( int i = 0; i < N; i++ ) {
        sim->c[i]    = concentrations[i];
        sim->a_rates[i] = a_rates[i];
        sim->b_rates[i] = b_rates[i];
    }

    sim->influx = influx;

    sim->time = 0;
    sim->target_dt = BD_DEFAULT_TARGET_DT;

    sim->nr_failed_adaptions = 0;
    sim->nr_steps            = 0;

    return sim;
}


void bd_free_simulation(struct bd_simulation_t * sim) {
    free( sim->c );
    free( sim->a_rates );
    free( sim->b_rates );

    free( sim );
}

//
// Time evolution functions: routine, step, evolution
//

int bd_rkck_routine( double dt, const double * c, const double * a_rates, double * b_rates, 
                      double influx, unsigned N, double * dcout, double * dcerr, double ** buffers ) {}

int bd_rkck_step( struct bd_simulation_t * sim, double max_dt, double * dcout, double * dcerr, double ** buffers ) {}

int bd_rkck_evolution_until( struct bd_simulation_t * sim, double until_time, double until_cmax ) {}

int bd_rkck_evolution_single( struct bd_simulation_t * sim ) {}


// 
// Api Interface functions
//

int bd_get_max_cluster_size( struct bd_simulation_t * sim ) {
    return sim->N;
}

double * bd_get_concentrations( struct bd_simulation_t * sim ) {
    return sim->c;
}

void bd_set_concentrations( struct bd_simulation_t * sim, double * concentrations ) {
    for ( int i = 0; i < sim->N; i++ ) sim->c[i] = concentrations[i];
}

double * bd_get_a_rates( struct bd_simulation_t * sim ) {
    return sim->a_rates;
}

void bd_set_a_rates( struct bd_simulation_t * sim, double * a_rates ) {
    for ( int i = 0; i < sim->N; i++ ) sim->a_rates[i] = a_rates[i];
}

double * bd_get_b_rates( struct bd_simulation_t * sim ) {
    return sim->b_rates;
}

void bd_set_b_rates( struct bd_simulation_t * sim, double * b_rates ) {
    for ( int i = 0; i < sim->N; i++ ) sim->b_rates[i] = b_rates[i];
}

double bd_get_influx( struct bd_simulation_t * sim ) {
    return sim->influx;
}

void bd_set_influx( struct bd_simulation_t * sim, double influx ) {
    sim->influx = influx;
}

double bd_get_time( struct bd_simulation_t * sim ) {
    return sim->time; 
}

void bd_set_time( struct bd_simulation_t * sim, double time ) {
    sim->time = time; 
}

double bd_get_target_dt( struct bd_simulation_t * sim ) {
    return sim->target_dt; 
}

void bd_set_target_dt( struct bd_simulation_t * sim, double target_dt ) {
    sim->target_dt = target_dt; 
}

unsigned bd_get_nr_failed_adaptions( struct bd_simulation_t * sim ) {
    return sim->nr_failed_adaptions;
}

unsigned bd_get_nr_steps( struct bd_simulation_t * sim ) {
    return sim->nr_steps;
}

double bd_get_error_tolerance( struct bd_simulation_t * sim ) {
    return sim->error_tolerance;
}

void bd_set_error_tolerance( struct bd_simulation_t * sim, double error_tolerance ) {
    sim->error_tolerance = error_tolerance;
}

char * bd_get_error_message( struct bd_simulation_t * sim ) {
    return sim->error_message;
}
