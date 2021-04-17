class Power():
    def check(N,P):
        N = int(N)
        P = int(P)
        
        if P == 1:
            return N
        
        if P != 1:
            return (N*Power.check(N,P-1))

T = Power
arr = input().split(",")
N = arr[0]
P = arr[1]
test = T.check(N,P)
print("{0}^{1} = {2}".format(N,P,test))
