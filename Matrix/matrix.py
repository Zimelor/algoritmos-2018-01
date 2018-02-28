import time
import numpy as np
import matplotlib.pyplot as plt

def multp(N):
    A = np.random.randint(N,size=(N,N), dtype=np.int64)
    B = np.random.randint(N,size=(N,N), dtype=np.int64)
#    A = np.ones((N,N), dtype=np.int64)
#    B = np.ones((N,N)) + np.ones((N,N), dtype = np.int64)
    C = np.zeros((N,N), dtype=np.int64)
    ans = 0.0
    for i in range(N):
        for j in  range(N):
            for k in range(N):
                t0 = time.clock()
                mul = A[i,k]*B[k,j];
                C[i,j] = C[i,j] + mul
                t1 = time.clock()
                ans = ans + t1 - t0
    return ans

def test(N):
    X = np.arange(2,N)
    Y = [np.average([multp(i) for j in range(10)], axis = 0) for i in range(2,N)]
    plt.xlabel('N')
    plt.ylabel('Tiempo(ms)')
    plt.title('Tiempo total para multiplicación matrices 1\'s y 2\'s')
    plt.plot(X,Y)
    return Y

def test1(N, t):
    X = np.arange(2,N)
    Y =  [np.average([multp(i) for j in range(t)]) for i in range(2,N)]
    tAvg =  [Y[i-2]/(2*i*i*i - i*i) for i in range(2,N)]
    print(Y)
    print(tAvg)
    plt.xlabel('N')
    plt.ylabel('Tiempo(ms)')
    plt.title('Tiempo por operación elemental matrices 1\'s y 2\'s')
    plt.plot(X,tAvg)

#test(20)
test1(20, 10)