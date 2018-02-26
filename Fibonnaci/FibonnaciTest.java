import java.util.Scanner;

public class FibonnaciTest {

    static long fib(long n){
        long a = 0, b = 1, i = 0;
            for(; i < n; i++){
                long c = b;
                b = a + b;
                a = c;
            }
        return a;
    }

    static int fib(int n){
        int a = 0, b = 1, i = 0;
            for(; i < n; i++){
                int c = b;
                b = a + b;
                a = c;
            }
        return a;
    }

    static short fib(short n){
            short a = 0, b = 1, i = 0;

                 for(; i < n; i++){
                     short c = b;
                     b = (short) (a + b);
                     a = c;
                 }
             return a;
    }


    static byte fib(byte n){
            byte a = 0, b = 1, i = 0;

                 for(; i < n; i++){
                     Byte c = b;
                     b = (byte) (a + b);
                     a = c;
                 }
             return a;
    }

    public static void main(String[] args){
        /**
         * Resultados:
         * byte overflow para n = 12
         * short overflow para n = 24
         * int overflow para n = 47
         * long overflow para n = 94
         */


        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        for(int i = 0; i < n; i++){
            System.out.println(fib((long)i) + " " + i);
        }
    }
}
