#include "stdio.h"

static int c_fib(int n){
    if(n==0)
            return 0;
    if(n==1)
            return 1;
    return c_fib(n-1)+c_fib(n-2);
}