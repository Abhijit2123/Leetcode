class series():
    def check(N):
        a = 1
        b = 1
        if N == 1:
            return a
        if N == 2:
            return b
        if N > 2:
            if N % 2 != 0:
                return 2*2**((N-3)//2)
            else:
                return 3*3**((N-3)//2)                # As this is in GP tn = a*r**(n-1)
T = series
N = int(input("Please enter the term: "))
test = T.check(N)
print("The {0}th term is {1}".format(N,test))
            
