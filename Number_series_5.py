class series():
    def check(N):
        a = 0
        b = 0
        if N == 1:
            return a
        if N == 2:
            return b
        if N > 2:
            if N % 2 != 0:
                return 2 + ((N-3)//2)*2
            else:
                return (N-2)//2
T = series
N = int(input("Enter the term: "))
test = T.check(N)
print(test)
