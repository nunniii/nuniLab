
#include <stdio.h>

// bool.h
#ifndef BOOL_H
#define BOOL_H

int and();
int or();
int not();

#endif




void printTruthTable(int (*func)(int, int), const char *operationName) {
    printf("True table for %s:\n", operationName);
    printf("n1 | n2 | Result \n");
    printf("---|----|----------\n");

    if (func == not) {
        for (int n = 0; n <= 1; n++) {
            int resultado = func(n, 0); // 0 é passado como o segundo argumento para não quebrar 😥
            printf("%d  | %d  | %d\n", n, 0, resultado);
        }
    } else {
        for (int n1 = 0; n1 <= 1; n1++) {
            for (int n2 = 0; n2 <= 1; n2++) {
                int resultado = func(n1, n2);
                printf("%d  | %d  | %d\n", n1, n2, resultado);
            }
        }
    }
}

void main() {
    // Chamando as funções e imprimindo as tabelas da verdade
    printTruthTable(and, "AND (E lógico)");
    printTruthTable(or, "OR (OU lógico)");
    printTruthTable(not, "NOT (NÃO lógico)");
}