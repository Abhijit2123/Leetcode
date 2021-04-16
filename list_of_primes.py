class primelst():
    def primenos(N):
        lst = set()
        for num in range(2, N + 1):
           # all prime numbers are greater than 1
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    lst.add(num)
                    
        return sorted(lst)
T = primelst
test = T.primenos(int(input("Please enter number: ")))
print(test)
