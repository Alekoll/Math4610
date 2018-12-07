#include <omp.h>




int main (int argc, char *argv[])
{
int numThreads, tid;

/* Fork a team of threads giving them their own copies of variables */
#pragma omp parallel private(numThreads, tid)
  {

  /* Obtain thread number */
  tid = omp_get_thread_num();
  printf("Hi from thread = %d\n", tid);

  /* Only master thread does this */
  if (tid == 0)
    {
    numThreads = omp_get_num_threads();
    printf("# of threads = %d\n", numThreads);
    }

  }  /* All threads join master thread and disband */

}