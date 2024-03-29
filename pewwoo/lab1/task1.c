// Borodin Alexey <nenavizhu.leto@gmail.com>
// Lab #1/7

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define ERRFEWARGS 100 // Too few arguments

float calculate_a(float x, float y);
float calculate_b(float x, float z);

int main(int argc, char **kwargs) {

  if (argc < 3) {
    printf("too few arguments. at least 3 required\n");
    return ERRFEWARGS;
  }

  // Task 1
  float x = atof(kwargs[1]);
  float y = atof(kwargs[2]);
  float z = atof(kwargs[3]);
  float a = calculate_a(x, y);
  float b = calculate_b(x, z);

  printf("a = %f\nb = %f\n", a, b);
  return 0;
}

float calculate_a(float x, float y) {
  float nominator = sqrtf(fabsf(x - 1)) - powf(fabsf(y), 1.f / 3);
  float denominator = 1 + (powf(x, 2) / 2) + (powf(y, 2) / 4);

  return nominator / denominator;
}

float calculate_b(float x, float z) { return x * (asinf(z) + expf(-(x + 3))); }
