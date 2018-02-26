#include<bits/stdc++.h>
using namespace std;

short fib(short n){
    short a = 0, b = 1;
    for(short i = 0; i < n; i++){
        short c = b;
        b = a + b;
        a = c;
    }
    return a;
}


unsigned short fib(unsigned short n){
    unsigned short a = 0, b = 1;
    for(unsigned short i = 0; i < n; i++){
        unsigned short c = b;
        b = a + b;
        a = c;
    }
    return a;
}


int fib(int n){
    int a = 0, b = 1;
    for(int i = 0; i < n; i++){
        int c = b;
        b = a + b;
        a = c;
    }
    return a;
}

unsigned int fib(unsigned int n){
    unsigned int a = 0, b = 1;
    for(unsigned int i = 0; i < n; i++){
        unsigned int c = b;
        b = a + b;
        a = c;
    }
    return a;
}

long fib(long n){
    long a = 0, b = 1;
    for(long i = 0; i < n; i++){
        long c = b;
        b = a + b;
        a = c;
    }
    return a;
}

unsigned long fib(unsigned long n){
    unsigned long a = 0, b = 1;
    for(unsigned long i = 0; i < n; i++){
        unsigned long c = b;
        b = a + b;
        a = c;
    }
    return a;
}

long long fib(long long n){
    long long a = 0, b = 1;
    for(long long i = 0; i < n; i++){
        long long c = b;
        b = a + b;
        a = c;
    }
    return a;
}

unsigned long long fib(unsigned long long n){
    unsigned long long a = 0, b = 1;
    for(unsigned long long i = 0; i < n; i++){
        unsigned long long c = b;
        b = a + b;
        a = c;
    }
    return a;
}


int main(){
    /**
    *Resultados:
    *overflow de short en n = 24
    *overflow de unsigned short en n = 25
    *overflow de int en n = 47
    *overflow de unsigned int en n = 48
    *overflow de long en n = 93
    *overflow de unsigned long en n = 94
    *overflow de long long en n = 93
    *overflow de unsigned long long en n = 94
    */
    int n;
    cin >> n;
    for(int i = 1; i < n; i++){
        cout << "i: " << i << ' ' << fib((unsigned long long)i)<<'\n';
        if(fib((unsigned long long)i-1) > fib((unsigned long long)i) ) break;
    }

	return 0;
}
