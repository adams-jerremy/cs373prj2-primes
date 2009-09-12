#!/usr/bin/env python




# -------
# globals
# -------

import math

i = 0 # input
p1 = 0 # output
p2 = 0 # output
allPrimes = [2, 3,     5,     7,     11, 13, 17,     19,     23,     29,     31,     37,     41,     43,     47,     53,     59,     61,     67,
            71, 73,     79,     83,     89,     97,     101,     103,     107,     109,     113,     127,     131,     137,     139,     149,     151,     157,
            163,     167,     173, 179,     181,     191,     193,     197,     199,     211,     223,     227,     229,    233,     239,     241,     251,     257,
            263,     269,     271,     277,     281, 283,     293,     307,     311,     313,     317,     331,     337,     347,     349,     353,     359,     367,
            373,     379,     383,     389,     397,     401,     409, 419,     421,     431,     433,     439,     443,     449,     457,     461,     463,     467,
            479,     487,     491,     499,     503,     509,     521,     523,     541, 547,     557,     563,     569,     571,     577,     587,     593,     599,
            601,     607,     613,     617,     619,     631,     641,     643,     647,     653,     659, 661,     673,     677,     683,     691,     701,     709,
            719,     727,     733,     739,     743,     751,     757,     761,     769,     773,     787,     797,     809, 811,     821,     823,     827,     829,
            839,     853,     857,     859,     863,     877,     881,     883,     887,     907,     911,     919,    929,     937,     941, 947,     953,     967,
            971,     977,     983,     991,     997,     1009,     1013,     1019,     1021,     1031,     1033,     1039,     1049,     1051,     1061,     1063,     1069, 1087,
            1091,     1093,     1097,     1103,     1109,     1117,     1123,     1129,     1151,     1153,     1163,     1171,     1181,     1187,     1193,     1201,     1213,
            1217,     1223, 1229,    1231,     1237,     1249,     1259,     1277,     1279,     1283,     1289,     1291,     1297,     1301,     1303,     1307,     1319,     1321,
            1327,     1361,    1367,     1373, 1381,    1399,     1409,     1423,     1427,     1429,     1433,     1439,     1447,     1451,     1453,     1459,     1471,     1481,
            1483,     1487,     1489,     1493,     1499,     1511, 1523,    1531,     1543,     1549,     1553,     1559,     1567,     1571,     1579,     1583,     1597,     1601,
            1607,     1609,     1613,     1619,     1621,     1627,     1637,     1657, 1663, 1667,     1669,     1693,     1697,     1699,     1709,     1721,     1723,     1733,
            1741,     1747,     1753,     1759,     1777,     1783,     1787,     1789,     1801,     1811, 1823,    1831,     1847,     1861,    1867,     1871,     1873,     1877,
            1879,     1889,     1901,     1907,     1913,     1931,     1933,     1949,     1951,     1973,     1979,     1987, 1993,    1997,     1999,     2003,     2011,     2017,
            2027,     2029,     2039,     2053,     2063,     2069,     2081,     2083,     2087,     2089,     2099,     2111,     2113,     2129, 2131,    2137,     2141,     2143,
            2153,     2161,     2179,     2203,     2207,     2213,     2221,     2237,     2239,     2243,     2251,     2267,     2269,     2273,     2281,     2287, 2293, 2297,
            2309,     2311,     2333,     2339,     2341,     2347,     2351,     2357,     2371,     2377,     2381,     2383,     2389,     2393,     2399,     2411,     2417,    
            2423, 2437,     2441,     2447,     2459,     2467,     2473,     2477,     2503,     2521,     2531,     2539,     2543,     2549,     2551,     2557,     2579,   
            2591,    2593,     2609,     2617, 2621,     2633,     2647,     2657,     2659,     2663,     2671,     2677,     2683,     2687,     2689,     2693,     2699,
            2707,     2711,     2713,     2719,     2729,     2731,     2741, 2749,     2753,     2767,     2777,    2789,     2791,     2797,     2801,     2803,     2819,    
            2833,     2837,     2843,     2851,     2857,     2861,     2879,     2887,     2897,     2903, 2909,     2917,     2927,     2939,     2953,     2957,     2963,
            2969,     2971,     2999,     3001,     3011,     3019,     3023,     3037,     3041,     3049,     3061,     3067,     3079, 3083,     3089,     3109,     3119,
            3121,     3137,     3163]

# -----------
# InputReader
# -----------

class InputReader (object) :
    def read (self) :
        return raw_input()

# ------------
# OutputWriter
# ------------

class OutputWriter (object) :
    def write (self, *a) :
        for w in a :
            print w,
        print

# -------
# my_read
# -------

def my_read (r) :
    """
    reads an int into i
    @param r - InputReader
    @return boolean - true if read succeeds, false otherwise
    """
    global i
    try :
        s = r.read()
    except EOFError :
        return False
    i = int(s)
    return True

def isPrime(n) :
    """
    Primality tester.  
    @param n - Number to be tested for primality
    @return boolean - True if n is prime, False otherwise
    """
    global allPrimes
    if n==2:
        return True # 2 prime
    if n&1 == 0:
        return False #Evens other than 2 not prime
    if n < 3167 :
        return binarySearch(n,allPrimes) # if in collection, prime # return n in allPrimes
    limit = int(n**0.5)+1
    for x in xrange(1,len(allPrimes)): #otherwise, test each prime less than the square root
        if allPrimes[x] > limit:
            break
        if n%allPrimes[x] == 0:
            return False
    return True
    

def binarySearch(x,xs):
    """
    Performs a binary search
    @param x - The value being searched for
    @param xs - the collection searched
    """
    end = len(xs)-1
    beg = 0
    while True:
        mid = (end+beg)/2
        if xs[mid] == x or xs[beg] == x or xs[end] == x:
            return True
        if beg == mid :
            break
        if x > xs[mid]:
            beg = mid
        else :
            end = mid
    return False
# -------
# my_eval
# -------

def my_eval (n) :
    """
    Finds the sum of two primes that sum to n.
    @param n - Integer
    """
    global p1
    global p2
    v = 0
    for x in xrange(0,len(allPrimes)):
        p1 = allPrimes[x] # select first prime
        p2 = n - p1 # test difference
        if isPrime(p2): # if difference prime, done
            return
        
            
        
# --------
# my_print
# --------

def my_print (w) :
    """
    Prints results in the form "p1 p2 p3 p4" where each pi is a prime number and the sum adds to the input.
    @param w - OutputWriter 
    """
    w.write(2, (2+(i&1)), p1, p2)

# ----
# main
# ----

def main () :
    """
    Program driver.  Executes a read-eval-print loop to solve the sum of four primes problem.
    """
    global i
    
    
    while my_read(InputReader()) :
        if i < 8 :
            print "Impossible."
        else :
            my_eval(i-(4+(i&1)))
            my_print(OutputWriter())

if __name__ == "__main__" :
    main()