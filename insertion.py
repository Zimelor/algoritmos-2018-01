#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 22:12:44 2018

@author: miaortizma
"""
import numpy as np
import itertools as it
import matplotlib.pyplot as plt

def insert(arr, num):
    i = len(arr)
    arr = arr + [num]
    while(i >= 1 and arr[i-1] > num):
        arr[i]= arr[i-1]
        i = i - 1
    arr[i] = num
    if(i == 0):
        comparations = 2*(len(arr)-1) + 1
    else:
        comparations = 2*(len(arr) - i)
    swaps = len(arr) - i 
    others = 2 + (len(arr) - i - 1)
    return arr, (comparations, swaps, others)
5

def insertionSort(toSort):
    n = len(toSort)
    comparations = 0
    swaps = 0
    others = 0
    arr = []
    for i in range(n):
        arr, temp = insert(arr, toSort[i])
        comparations = comparations + temp[0]
        swaps = swaps + temp[1]
        others = others + temp[2]
    return (comparations, swaps, others)


'''
perms = it.permutations(range(n))


#for perm in perms:
#    print(perm)

print(np.arange(n))
'''
def allPerms(n):
    if(n > 8):
        print("Input too big, try a number like 8 or less")
    comparations = []
    swaps = []
    others = []
    perms = it.permutations(range(n))
    for perm in perms:
        temp = insertionSort(perm)
        comparations = comparations + [temp[0]]
        swaps = swaps + [temp[1]]
        others = others + [temp[2]]
    N = len(comparations)
    print("Average:")
    print("Comparations:", sum(comparations)/N)
    print("Swaps:", sum(swaps)/N)
    print("Others:", sum(others)/N)
    print("Distribucion:")
    plt.hist(comparations,bins='auto')
    plt.title("Histogram of Comparations")
    plt.show()
    plt.hist(swaps,bins='auto')
    plt.title("Histogram of Swaps")
    plt.show()
    plt.hist(others,bins='auto')
    plt.title("Histogram of Others")
    plt.show()
    
allPerms(8)

def samplePerms(n, m):
    comparations = []
    swaps = []
    others = []
    rng = range(n)
    for i in range(m):
        nxt = np.random.permutation(rng)
        temp = insertionSort(nxt)
        comparations = comparations + [temp[0]]
        swaps = swaps + [temp[1]]
        others = others + [temp[2]]
    N = len(comparations)
    print("Average:")
    print("Comparations:", sum(comparations)/N)
    print("Swaps:", sum(swaps)/N)
    print("Others:", sum(others)/N)
    print("Distribucion:")
    plt.hist(comparations,bins='auto')
    plt.title("Histogram of Comparations")
    plt.show()
    plt.hist(swaps,bins='auto')
    plt.title("Histogram of Swaps")
    plt.show()
    plt.hist(others,bins='auto')
    plt.title("Histogram of Others")
    plt.show()

samplePerms(20, 10000)