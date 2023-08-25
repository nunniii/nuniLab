
int and(int n1, int n2){
    if (n1 != 0) n1 = 1;
    if (n2 != 0) n2 = 1;

    return n1 * n2;
}

int or(int n1, int n2){
    int r;
    if (n1 != 0) n1 = 1;
    if (n2 != 0) n2 = 1;

    if (n1 + n2 > 1) r = 1;
    else r = n1 + n2;

    return r;
}

int not(int n){
    return 1 - n;
}

