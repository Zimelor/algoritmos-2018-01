import time
import numpy as np
import matplotlib.pyplot as plt

def multp(N):
    tMultp = 0.0
    tSum = 0.0
    A = np.ones((N,N), dtype=np.int64)
    B = np.ones((N,N)) + np.ones((N,N), dtype = np.int64)
    C = np.zeros((N,N), dtype=np.int64)
    for i in range(N):
        for j in  range(N):
            for k in range(N):
                
                t0 = time.clock()
                mul = A[i,k]*B[k,j];
                t1 = time.clock()
                tMultp = tMultp + (t1 - t0)
                
                t0 = time.clock()
                C[i,j] = C[i,j] + mul
                t1 = time.clock()
                tSum = tSum + (t1 - t0)
    #print(A)
    #print(B)
    #print(C)
    return tMultp, tSum

def test(N):
    X = np.arange(N)
    Y = [np.average([multp(i) for j in range(10)], axis = 0) for i in range(N)]
    plt.xlabel('N')
    plt.ylabel('Tiempo(ms)')
    plt.plot(X,Y)
    plt.legend(['Multp','Sum']);
    return Y

def test1(N):
    X = np.arange(N)
    Y = [np.average([multp(i) for j in range(10)], axis = 0) for i in range(N)]
    tAvg = [Y[0]] + [(Y[i][0]/i*i,Y[i][1]/i*i) for i in range(1,N)]
    
    plt.xlabel('N')
    plt.ylabel('Tiempo(ms)')
    plt.title('Tiempo por operación elemental')
    plt.plot(X,Y)
    plt.legend(['Multp','Sum']);
    for i in range(N):
        print(str(tAvg[i])+',')

test1(20)

