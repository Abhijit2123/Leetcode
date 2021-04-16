class series():
    def check(N):
        a = 0
        b = 0
        lst = []
        for i in range(N+1):
            if i == 1:
                lst.append(a)
            if i == 2:
                lst.append(b)
            if i > 2:
                if i % 2 != 0:
                    lst.append(2 + ((i-3)//2)*2)
                else:
                    lst.append((i-2)//2)
        return lst
    
T = series
N = int(input("Enter the term: "))
test = T.check(N)
print(test)
