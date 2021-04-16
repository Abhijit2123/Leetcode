class Leap():
    def LeapYear(N):
        if N % 4 == 0:
            if N % 100 == 0:
                if N % 400 == 0:
                    print(str(N) + " is a Leap Year")
                else:
                    print(str(N) + " is not a Leap Year")
            else:
                print(str(N) + " is a Leap Year")
        else:
            print(str(N) + " is not a Leap Year")
            
T = Leap
N = int(input("Please input Year: "))
T.LeapYear(N)
