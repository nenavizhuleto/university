
// Borodin Alexey <nenavizhu.leto@gmail.com>
// Lab #1/7
//
#include <math.h>
#include <stdio.h>
#include <sys/types.h>

#define ERRFEWARGS 100 // Too few arguments

void task_1(float, float, float);
void task_2(float);

int main(int argc, char **kwargs) { return 0; }

void task_1(float x, float y, float z) {

  float a = (sqrtf(fabsf(x - 1)) - powf(fabsf(y), 1.f / 3)) /
            (1 + (powf(x, 2) / 2) + (powf(y, 2) / 4));

  float b = x * (asinf(z) + expf(-(x + 3)));

  printf("A = %f\n", a);
  printf("B = %f\n", b);
}

void task_2(float a) {
  if (-2.0f > a && a < 2.0f) {
    printf("f(%f) = %f\n", a, sqrtf(a));
  } else {
    printf("f(%f) = %f\n", a, sqrtf(4.0f));
  }
}

void task_3(int n, int k) {
  // every number has '1' in common dividers
  int count = 1;
  if (k > n) {
    printf("k > n\n");
    return;
  }

  if (n % 2 == 0)
    n = n / 2;

  if (k > n) {
    printf("k > n/2\n");
    return;
  }
}
