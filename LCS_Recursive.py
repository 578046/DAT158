# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 09:53:16 2021

@author: silja

DAT158 Problem 9 a - Compulsory exercise
Recursive version of the longest common subsequence problem
"""

def lcs(X, Y, m, n):
    
   if m == 0 or n == 0:
    return 0;
   elif X[m-1] == Y[n-1]: 
    return 1 + lcs(X, Y, m-1, n-1);
   else:
    return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));

X = "babbabab"
Y = "bbabbaaab"

print("Length of LCS is", lcs(X, Y, len(X), len(Y)))

