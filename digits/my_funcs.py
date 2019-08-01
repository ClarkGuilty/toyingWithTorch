#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 13:03:16 2019

@author: Javier Alejandro Acevedo Barroso
"""

import numpy as np
import matplotlib.pyplot as plt
from math import *
import time
import itertools


primeList = [2,3,5,7] 

      
      
def isPrime(a):
	if (a == 2):
		return True
	if ( a%2 == 0):
		return False
	if(a == 1):
		return False
	b = 3.0
	while(b<= sqrt(a)):
		if(a%b == 0):
			return False
		b +=2
	return True

def nprime(a):
    if (a == 2):
          return True
    if ( a%2 == 0):
          return False
    if(a == 1):
          return False
    lis = np.arange(3,np.int64(sqrt(a)),2)
    lis = a%lis
    return len(lis[lis==0]) == 0

#Does prime factorization on n. Returns a list of lists: [prime divisors, correspondent multiplicity] (returns 1 as a primeDivisor, for sake of  consistency in later functions TODO fix it). 
def pDiv(n):
	if(isPrime(n)):
		return [[1,n],[1,1]]
	else:
		pDiv = [1]
		nDiv = [1]
		if(n%2 == 0):
			pDiv.append(2)
			q = 1; n = n/2
			while(n%2 == 0):
				q += 1
				n = n/2
			nDiv.append(q)
		cuenta = 3
		while(n != 1 ):
			if(n%cuenta == 0) :
				pDiv.append(cuenta)
				q = 1; n = n/cuenta
				while(n%cuenta == 0):
					q += 1
					n = n/cuenta
				nDiv.append(q)
			cuenta += 2
		return [pDiv, nDiv]



#Return the number of positive integer divisors of n.
def nDiv(n):
      a = 0
      heh = pDiv(n)[1][1:]
      total=1
      while(a < len(heh)):
            total = (heh[a] +1)*total
            a += 1
      return total

#Returns an array of indexes for the array m.
def aoL(m):
      return range(len(m))

#Returns the divisors of a number.
def div(n):
      pdiv , mult = pDiv(n)
      pdiv = pdiv[1:]
      mult = mult[1:]
      rta = [1]
      total = nDiv(n)
      for i in range(len(pdiv)):
            rta += [x*(pdiv[i]**j) for j in range(1,mult[i]+1) for x in rta] 
          
      return rta


























