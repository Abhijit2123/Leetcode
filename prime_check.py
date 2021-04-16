class prime():
    def primeno(N):
        for i in range(2,N):
            if N % i == 0:
                return "The number {0} is a not prime number divisible by {1}".format(N,i)
        return "The number {0} is a prime number".format(N)

T = prime
test = T.primeno(int(input("Please enter number: ")))
print(test)
