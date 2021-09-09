# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

__author__      = "Silja Stubhaug Torkildsen"
DAT158 Problem 2 b - Compulsory exercise
the Boyer-Moore matching algorithm

"""


NO_OF_CHARS = 256

def badCharH(string, size):
    
    badChar = [-1]*NO_OF_CHARS
    
    for i in range(size):
        badChar[ord(string[i])] = i;
        
    return badChar


def search(txt, pat):
    
    m = len(pat)
    n = len(txt)
    
    badChar = badCharH(pat, m)
    
    s = 0
    c = 0
    while(s <= n-m):
        j = m-1
        c += 1
        
        while j >= 0 and pat[j] == txt[s+j]:
            j -= 1
            
            
        if j < 0:
            
            print("Pattern occur at shift = {}".format(s))
            print("Average comparisons for characters: " + str(c/n))
            
            s += (m-badChar[ord(txt[s+m])] if s+m<n else 1)
    
        else:
            
            s += max(1, j-badChar[ord(txt[s+j])])
            
        
def main():
    
    txt = "Høgskulen på Vestlandet er en norsk statlig høgskole som ble opprettet 1. januar 2017 gjennom en sammenslåing av Høgskolen i Bergen, Høgskulen i Sogn og Fjordane og Høgskolen Stord/Haugesund."
    pat = "ergen"

    
    search(txt, pat)
    
if __name__ == '__main__':
    main()
            
            
            
    