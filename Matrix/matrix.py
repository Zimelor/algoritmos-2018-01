import time
import numpy as np
import matplotlib.pyplot as plt

def multp(N):
    A = np.ones((N,N), dtype=np.int64)
    B = np.ones((N,N)) + np.ones((N,N), dtype = np.int64)
    t0 = time.clock()
    np.dot(A,B)
    t1 = time.clock()
    return t1 - t0

def multpNoNumpy(N):
    A = [[1]*N]*N
    B = [[2]*N]*N
    C = [[0]*N]*N
    t0 = time.clock()
    for i in range(N):
        for j in  range(N):
            for k in range(N):
                C[i][j] += A[i][k]*B[k][j];
    t1 = time.clock()
    return t1 - t0



def test(N):
    X = np.arange(2,N)
    Y = [np.average([multp(i) for j in range(10)], axis = 0) for i in range(2,N)]
    plt.xlabel('N')
    plt.ylabel('Tiempo(ms)')
    plt.title('Tiempo total para multiplicación matrices 1\'s y 2\'s')
    plt.plot(X,Y)
    return Y

def test1(N, t):
    #Y =  [np.average([multp(i) for j in range(t)]) for i in range(2,N)]
    #tAvg =  [Y[i-2]/(2*i*i*i - i*i) for i in range(2,N)]
    print('[')
    for i in range(2,N):
        A = np.average([multp(i) for j in range(t)])
        A = A/(2*i*i*i - i*i)
        print(A, ',')
    print(']')
    #plt.xlabel('N')
    #plt.ylabel('Tiempo(ms)')
    #plt.title('Tiempo por operación elemental matrices 1\'s y 2\'s')
    #plt.plot(X,tAvg)

def testNoNumpy(N,t):
    print('[')
    for i in range(2,N):
        A = np.average([multpNoNumpy(i) for j in range(t)])
        A = A/(2*i*i*i - i*i)
        print(A, ',')
    print(']')
    

#test(20)
#plt.show()
test1(100, 10)