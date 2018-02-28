#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 22:12:44 2018

@author: miaortizma
"""
import numpy as np
import itertools as it
import matplotlib.pyplot as plt


def insert(arr, j):
    i = j
    while(i > 0 and arr[i] < arr[i-1]):
        arr[i], arr[i-1] = arr[i-1],arr[i]
        i = i - 1
    if(i == 0):
        comparations = 2*(j) + 1
        others = 1 + (j - 1)
    else:
        comparations = 2*(j - i)
    swaps = j - i
    others = 1 + (j - i)
    return arr, (comparations, swaps, others)


def insertionSort(toSort):
    n = len(toSort)
    comparations = 0
    swaps = 0
    others = 0
    for i in range(1,n):
        toSort, temp = insert(toSort, i)
        comparations = comparations + temp[0]
        swaps = swaps + temp[1]
        others = others + temp[2]
    return (comparations, swaps, others)


def graph(comparations, swaps, others):
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
    allOps = comparations + swaps + others
    plt.title("Histogram of all operations")
    plt.hist(allOps, bins='auto')
    plt.show()


def allPerms(n):
    if(n > 8):
        print("Input too big, try a number like 8 or less")
    comparations = []
    swaps = []
    others = []
    perms = it.permutations(range(n))
    for perm in perms:
        temp = insertionSort(list(perm))
        comparations = comparations + [temp[0]]
        swaps = swaps + [temp[1]]
        others = others + [temp[2]]
    graph(comparations, swaps, others)
    


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
    graph(comparations, swaps, others)

samplePerms(30, 10000)
    