class term():
    def findTerm(N):
        a = 0
        b = 0
        if N == 1:
            return a
        if N == 2:
            return b
        if N > 2:
            if (N-2) % 2 != 0:
                term = 7 + ((N-3)//2)*7               # Here the series in AP so tn = a + (n-1)d
                return term
            else:
                term = 6 + ((N-3)//2)*6
                return term

T = term
N = int(input("Please input term: "))
test = T.findTerm(N)
print("The {0}th term is {1}".format(N,test))
