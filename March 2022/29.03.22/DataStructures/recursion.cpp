#include <iostream>

int factorial {
    int n = 1;
    for (int i =1;i <= n; ++i) {
        n = n * i
    }
    return n;
}

int facorial(int n) {
    if(n == 0)
      return 1;
    else
      return n * factorial(n -1)
}