#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 13:03:16 2019

@author: Javier Alejandro Acevedo Barroso
"""

#import numpy as np
from math import sqrt
#from math import *


primes = [2,3,5,7,11] 

      
class factors:
      def __init__(self, number):
            self.number = number
            self.primes = [2,3,5,7,11,13]
            self.Prime = None
            self.prime_factors = None
            self.multiplicity = None
            self.n_divisors = None
            self.divisors = None
            
      def __repr__(self):
            return 'N = {}, primeF = {}, mult = {}\n numberDiv = {}, Prime? {}'     .format(
                        self.number,self.prime_factors, self.multiplicity, self.n_divisors, self.Prime)

       
      def assign(self,number):
            self.number = number
            self.Prime = None
            self.prime_factors = None
            self.multiplicity = None
            self.n_divisors = None
            self.divisors = None
           
      def calculate_all(self):
            self.Prime = self.isPrime()
            self.pDiv()
            self.nDiv()
            self.div
            
      def pDiv(self, n = None):
            if(n==None):
                  n=self.number
            n0 = n
            if(self.isPrime(n)):
                  return [[n],[1]]
            pFac = []
            multiplicity = []
            if(n%2 == 0):
                  pFac.append(2)
                  q = 1; n = n/2
                  while(n%2 == 0):
                        q += 1
                        n = n/2
                  multiplicity.append(q)
            pindex = 1
            cuenta = self.primes[pindex]
            while(n != 1 ):
                  if(n%cuenta == 0):
                        pFac.append(cuenta)
                        q = 1; n = n/cuenta
                        while(n%cuenta == 0):
                              q += 1
                              n = n/cuenta
                        multiplicity.append(q)
                  if(cuenta < self.primes[-1]):
                        pindex +=1
                        cuenta = self.primes[pindex]
                  else:
                        if(cuenta != self.primes[-1] and self.isPrime(cuenta)):
                              self.primes.append(cuenta)
                        cuenta += 2
                        
                        
            if(n0 == self.number):
                  self.prime_factors = pFac
                  self.multiplicity = multiplicity
            return [pFac, multiplicity]
      

      #Return the number of positive divisors of n.
      def nDiv(self, n = None, multiplicity = None):
            if(n==None):
                  n=self.number 
            if(self.multiplicity != None):
                  multiplicity = self.multiplicity
            if(multiplicity == None):
                  multiplicity = self.pDiv(n)[1][1:]

            a = 0
            total=1
            while(a < len(multiplicity)):
                  total = (multiplicity[a] +1)*total
                  a += 1
            if(n == self.number):
                  self.n_divisors = total
            return total

      #Returns the divisors of a number.
      def div(self, n= None, prime_factors = None, multiplicity = None):
            if(n==None):
                  n=self.number 
            if(prime_factors == None and multiplicity == None):
                  prime_factors, multiplicity = self.pDiv(n)
            rta = [1]
            for i in range(len(prime_factors)):
                  rta += [x*(prime_factors[i]**j) for j in range(1,multiplicity[i]+1) for x in rta]
            if(n == self.number):
                  self.divisors = rta
            return rta

      #Returns True if  n is prime. False otherwise.
      def isPrime(self, n = None):
            if(n == None):
                  n = self.number
                  if(self.Prime != None):
                        return self.Prime
            if (n == 2):
                  return True
            if ( n%2 == 0):
                  return False
            if(n == 1):
                  return False
      
            pIndex = 1
            b = self.primes[pIndex]
            while(b<= sqrt(n)):
                  #print(b)
                  if(n%b == 0):
                        if(n == self.number):
                              self.Prime = False
                        return False
                  if(b<self.primes[-1]):
                        pIndex+=1
                        b = self.primes[pIndex]
                  else:
                        b +=2
            return True
      
      

     
















