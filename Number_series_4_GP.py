class series():
    def check(N):
        a = 1
        b = 1
        lst = []
        for i in range(1,N+1):
            if i == 1:
                lst.append(a)
            if i == 2:
                lst.append(b)
            if i > 2:
                if i % 2 != 0:
                    lst.append(2*2**((i-3)//2))
                else:
                    lst.append(3*3**((i-3)//2))               # As this is in GP tn = a*r**(n-1)
        
        return lst
T = series
N = int(input("Please enter the term: "))
test = T.check(N)
print(test)
