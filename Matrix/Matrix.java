import java.util.Scanner;

public class Matrix {

    public static double multp(int n){
        int A[][] = new int[n][n], B[][] = new int[n][n], C[][] = new int[n][n];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                A[i][j] = 1;
                B[i][j] = 2;
            }
        }
        long t0, t1;
        t0 = System.nanoTime();
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                for(int k = 0; k < n; k++){
                    if(k == 0){
                        C[i][j] = A[i][k]*B[k][j];
                    }else{
                        C[i][j] += A[i][k]*B[k][j];
                    }
                }
            }
        }
        t1 = System.nanoTime();
        return t1 - t0;
    }

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        long s;
        System.out.println("[");
        for(int i = 2; i <= n; i++){
            s = 0;
            for(int j = 0; j < 10; j++) {
                s += multp(i);
            }
            //System.out.println((s/10.0)/1000.0 + ",");
            System.out.println(s/1000000000.0 + ",");
        }
        System.out.println("]");
    }
}

