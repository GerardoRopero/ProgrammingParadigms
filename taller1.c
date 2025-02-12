#include <stdio.h>
#include <stdbool.h>
#include <math.h>

int factorialRecursivo(int n);
int factorialIterativo(int n);
bool esPrimo(int n);
void conjuntoPrimosIntervalo(int a, int b);
int algoritmoEuclides(int a, int b);

int main() {
    printf("%d", factorialRecursivo(5));
    printf("\n");
    printf("%d", factorialIterativo(5));
    printf("\n");
    printf("%s", esPrimo(5) ? "Sí" : "No");
    printf("\n");
    
    conjuntoPrimosIntervalo(1, 100);

    printf("%d", algoritmoEuclides(10, 100));

    return 0;
}

int factorialRecursivo(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    return n * factorialRecursivo(n - 1);
}

int factorialIterativo(int n) {
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
