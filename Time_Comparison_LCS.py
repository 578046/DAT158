# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 10:39:42 2021

@author: silja

DAT158 Problem 9 c - Compulsory exercise
 
Experiment with strings of different length. At some point the recursive version will start 
using “a lot of time” while the dynamic version is still fast. Approximately, at what point does 
this happen?
"""
import time

"""Recursive version of the longest common subsequence problem"""
def lcsRec(X, Y, m, n):
    
   if m == 0 or n == 0:
    return 0;
   elif X[m-1] == Y[n-1]: 
    return 1 + lcsRec(X, Y, m-1, n-1);
   else:
    return max(lcsRec(X, Y, m, n-1), lcsRec(X, Y, m-1, n));


"""Dynamic Programming implementation of Longest Common Subsequence problem"""
def lcs(X, Y):
    
    """ Elements """
    m = len(X)
    n= len(Y)
    
    
    L = [[None]*(n+1) for i in range(m+1)]
    
    
    for i in range(m+1) :
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
                
    return L[m][n]


X = "babbabab"
Y = "bbabbaaab"

"""Recursive """
startRecursive = time.time()
print("Length of LCS is", lcsRec(X, Y, len(X), len(Y)))
endRecursive = time.time()
print("Time spent with Recursive: ", endRecursive - startRecursive)

"""Dynamic Programming"""

startDynamic = time.time();
print("Length of LCS is", lcs(X,Y))
endDynamic = time.time();
print("Time spent with Dynamic Programming: ", endDynamic - startDynamic)