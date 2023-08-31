// This is similar to the Rust impl, see in the file B-AAC.rs

#include <stdio.h>

typedef struct{
    char name[40];
    int age;
    void (*sayHi)(void);
    
} person;

void sayHi(){
    printf("Hi");
}


void main() {

    person nuni; 
        strcpy(nuni.name, "nuni"); 
        nuni.age = 20;

    nuni.sayHi();
}

