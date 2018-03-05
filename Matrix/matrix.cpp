#include<bits/stdc++.h>
#include<ctime>
using namespace std;
/**
/*Stackoverflow: "easily-measure-elapsed-time c++"
/*
**/

double multp(int n){
    int A[n][n], B[n][n], C[n][n];
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            A[i][j] = 1;
            B[i][j] = 2;
        }
    }

    clock_t t0 = clock();
    for(int k = 0; k < n; k++){
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(k == 0){
                    C[i][j] = A[i][k]*B[k][j];
                }else{
                    C[i][j] += A[i][k]*B[k][j];
                }
            }
        }
    }
    clock_t t1 = clock();
    return double(t1 - t0) / CLOCKS_PER_SEC;
}


int main(){
    freopen("out.txt", "w", stdout);
    int n;
    cin >> n;
    double s;
    cout << "[\n";
    for(int i = 2; i <= n; i++){
        s = 0.0;
        for(int j = 0; j < 10; j++) {
            s += multp(i);
        }
        cout << s/10.0 <<  ",\n";
    }
    cout << "]\n";
}
