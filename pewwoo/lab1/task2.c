// Borodin Alexey <nenavizhu.leto@gmail.com>
// Lab #1/7

#include <math.h>
#include <stdlib.h>

float f(float a);

int main(int argc, char **kwargs) {

  float a = atof(kwargs[1]);
  float answer = f(a);

  return 0;
}

float f(float a) {
  if (-2.0f > a && a < 2.0f) {
    return sqrtf(a);
  } else {
    return 4.0f;
  }
}
