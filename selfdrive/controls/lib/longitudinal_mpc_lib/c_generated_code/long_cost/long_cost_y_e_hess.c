/* This file was automatically generated by CasADi 3.6.4.
 *  It consists of: 
 *   1) content generated by CasADi runtime: not copyrighted
 *   2) template code copied from CasADi source: permissively licensed (MIT-0)
 *   3) user code: owned by the user
 *
 */
#ifdef __cplusplus
extern "C" {
#endif

/* How to prefix internal symbols */
#ifdef CASADI_CODEGEN_PREFIX
  #define CASADI_NAMESPACE_CONCAT(NS, ID) _CASADI_NAMESPACE_CONCAT(NS, ID)
  #define _CASADI_NAMESPACE_CONCAT(NS, ID) NS ## ID
  #define CASADI_PREFIX(ID) CASADI_NAMESPACE_CONCAT(CODEGEN_PREFIX, ID)
#else
  #define CASADI_PREFIX(ID) long_cost_y_e_hess_ ## ID
#endif

#include <math.h>

#ifndef casadi_real
#define casadi_real double
#endif

#ifndef casadi_int
#define casadi_int int
#endif

/* Add prefix to internal symbols */
#define casadi_f0 CASADI_PREFIX(f0)
#define casadi_s0 CASADI_PREFIX(s0)
#define casadi_s1 CASADI_PREFIX(s1)
#define casadi_s2 CASADI_PREFIX(s2)
#define casadi_s3 CASADI_PREFIX(s3)
#define casadi_s4 CASADI_PREFIX(s4)
#define casadi_sq CASADI_PREFIX(sq)

/* Symbol visibility in DLLs */
#ifndef CASADI_SYMBOL_EXPORT
  #if defined(_WIN32) || defined(__WIN32__) || defined(__CYGWIN__)
    #if defined(STATIC_LINKED)
      #define CASADI_SYMBOL_EXPORT
    #else
      #define CASADI_SYMBOL_EXPORT __declspec(dllexport)
    #endif
  #elif defined(__GNUC__) && defined(GCC_HASCLASSVISIBILITY)
    #define CASADI_SYMBOL_EXPORT __attribute__ ((visibility ("default")))
  #else
    #define CASADI_SYMBOL_EXPORT
  #endif
#endif

casadi_real casadi_sq(casadi_real x) { return x*x;}

static const casadi_int casadi_s0[7] = {3, 1, 0, 3, 0, 1, 2};
static const casadi_int casadi_s1[3] = {0, 0, 0};
static const casadi_int casadi_s2[9] = {5, 1, 0, 5, 0, 1, 2, 3, 4};
static const casadi_int casadi_s3[10] = {6, 1, 0, 6, 0, 1, 2, 3, 4, 5};
static const casadi_int casadi_s4[9] = {3, 3, 0, 1, 3, 3, 1, 0, 1};

/* long_cost_y_e_hess:(i0[3],i1[],i2[],i3[5],i4[6])->(o0[3x3,3nz]) */
static int casadi_f0(const casadi_real** arg, casadi_real** res, casadi_int* iw, casadi_real* w, int mem) {
  casadi_real a0, a1, a10, a2, a3, a4, a5, a6, a7, a8, a9;
  a0=arg[3]? arg[3][0] : 0;
  a1=arg[0]? arg[0][1] : 0;
  a2=10.;
  a2=(a1+a2);
  a3=(1./a2);
  a3=(a3/a2);
  a3=(a0*a3);
  if (res[0]!=0) res[0][0]=a3;
  a3=(a0/a2);
  a4=(a3/a2);
  if (res[0]!=0) res[0][1]=a4;
  a5=2.0000000000000001e-01;
  a6=(a1+a1);
  a6=(a5*a6);
  a7=arg[4]? arg[4][4] : 0;
  a6=(a6+a7);
  a6=(a6/a2);
  a8=arg[4]? arg[4][2] : 0;
  a9=arg[0]? arg[0][0] : 0;
  a8=(a8-a9);
  a9=casadi_sq(a1);
  a10=5.;
  a9=(a9/a10);
  a10=(a7*a1);
  a9=(a9+a10);
  a10=6.;
  a9=(a9+a10);
  a8=(a8-a9);
  a8=(a8/a2);
  a9=(a8/a2);
  a6=(a6+a9);
  a6=(a6/a2);
  a8=(a8/a2);
  a8=(a8/a2);
  a6=(a6+a8);
  a0=(a0*a6);
  a7=(a7*a4);
  a0=(a0+a7);
  a7=2.;
  a3=(a5*a3);
  a7=(a7*a3);
  a1=(a1+a1);
  a5=(a5*a4);
  a1=(a1*a5);
  a7=(a7-a1);
  a0=(a0-a7);
  if (res[0]!=0) res[0][2]=a0;
  return 0;
}

CASADI_SYMBOL_EXPORT int long_cost_y_e_hess(const casadi_real** arg, casadi_real** res, casadi_int* iw, casadi_real* w, int mem){
  return casadi_f0(arg, res, iw, w, mem);
}

CASADI_SYMBOL_EXPORT int long_cost_y_e_hess_alloc_mem(void) {
  return 0;
}

CASADI_SYMBOL_EXPORT int long_cost_y_e_hess_init_mem(int mem) {
  return 0;
}

CASADI_SYMBOL_EXPORT void long_cost_y_e_hess_free_mem(int mem) {
}

CASADI_SYMBOL_EXPORT int long_cost_y_e_hess_checkout(void) {
  return 0;
}

CASADI_SYMBOL_EXPORT void long_cost_y_e_hess_release(int mem) {
}

CASADI_SYMBOL_EXPORT void long_cost_y_e_hess_incref(void) {
}

CASADI_SYMBOL_EXPORT void long_cost_y_e_hess_decref(void) {
}

CASADI_SYMBOL_EXPORT casadi_int long_cost_y_e_hess_n_in(void) { return 5;}

CASADI_SYMBOL_EXPORT casadi_int long_cost_y_e_hess_n_out(void) { return 1;}

CASADI_SYMBOL_EXPORT casadi_real long_cost_y_e_hess_default_in(casadi_int i) {
  switch (i) {
    default: return 0;
  }
}

CASADI_SYMBOL_EXPORT const char* long_cost_y_e_hess_name_in(casadi_int i) {
  switch (i) {
    case 0: return "i0";
    case 1: return "i1";
    case 2: return "i2";
    case 3: return "i3";
    case 4: return "i4";
    default: return 0;
  }
}

CASADI_SYMBOL_EXPORT const char* long_cost_y_e_hess_name_out(casadi_int i) {
  switch (i) {
    case 0: return "o0";
    default: return 0;
  }
}

CASADI_SYMBOL_EXPORT const casadi_int* long_cost_y_e_hess_sparsity_in(casadi_int i) {
  switch (i) {
    case 0: return casadi_s0;
    case 1: return casadi_s1;
    case 2: return casadi_s1;
    case 3: return casadi_s2;
    case 4: return casadi_s3;
    default: return 0;
  }
}

CASADI_SYMBOL_EXPORT const casadi_int* long_cost_y_e_hess_sparsity_out(casadi_int i) {
  switch (i) {
    case 0: return casadi_s4;
    default: return 0;
  }
}

CASADI_SYMBOL_EXPORT int long_cost_y_e_hess_work(casadi_int *sz_arg, casadi_int* sz_res, casadi_int *sz_iw, casadi_int *sz_w) {
  if (sz_arg) *sz_arg = 5;
  if (sz_res) *sz_res = 1;
  if (sz_iw) *sz_iw = 0;
  if (sz_w) *sz_w = 0;
  return 0;
}


#ifdef __cplusplus
} /* extern "C" */
#endif
