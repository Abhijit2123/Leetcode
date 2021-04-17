class Check():
    def test(n,m,s):
        if (m+s-1) % n == 0:
            return n
        else:
            return (m+s-1) % n
T = Check
N = int(input())
for i in range(N):
    num = [int(d) for d in input().split()]
    n = num[0]
    m = num[1]
    s = num[2]
    res = T.test(n,m,s)
    print(res)
