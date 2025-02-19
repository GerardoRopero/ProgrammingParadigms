#include <stdio.h>
#include <stdbool.h>
#include <math.h>

long factorialRecursivo(int n);
long factorialIterativo(int n);
bool esPrimo(int n);
void conjuntoPrimosIntervalo(int a, int b);
int algoritmoEuclides(int a, int b);

int main() {
    printf("%ld", factorialRecursivo(34));
    printf("\n");
    printf("%ld", factorialIterativo(5));
    printf("\n");
    printf("%s", esPrimo(10) ? "Sí" : "No");
    printf("\n");
    
    conjuntoPrimosIntervalo(1, 10);

    printf("%d", algoritmoEuclides(10, 15));

    return 0;
}

long factorialRecursivo(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    return n * factorialRecursivo(n - 1);
}

long factorialIterativo(int n) {
    int resultado = 1;
    for (int i = 1; i <= n; i++) {
        resultado = resultado * i;
    }
    return resultado;
}

bool esPrimo(int n) {
    if (n < 2) {
        return false;
    }
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

void conjuntoPrimosIntervalo(int a, int b) {
    for (int i = a; i <= b; i++) {
        if (esPrimo(i)) {
            printf("%d ", i);
        }
    }
    printf("\n");
}

int algoritmoEuclides(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}
