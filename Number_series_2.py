class term():
    def findTerm(N):
        a = 0
        b = 0
        lst = []
        for i in range(1,N+1):
            if i == 1:
                lst.append(a)
            if i == 2:
                lst.append(b)
            if i > 2:
                if (i-2) % 2 != 0:
                    term = 7 + ((i-3)//2)*7
                    lst.append(term)
                else:
                    term = 6 + ((i-3)//2)*6
                    lst.append(term)
        return lst

T = term
N = int(input("Please input term: "))
test = T.findTerm(N)
print(test)
