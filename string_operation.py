class StringCheck():
    def check(N1, N2, N3):
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        
        M1 = ""
        M2 = ""
        M3 = ""
        
        for i in N1:
            if i in vowels:
                M1 = M1 + "%"
            else:
                M1 = M1 + i
                
        for i in N2:
            if i not in vowels:
                M2 = M2 + "#"
            else:
                M2 = M2 + i
                
        N3 = N3.upper()
        
        print(M1+M2+N3)

T = StringCheck
N1 = input()
N2 = input()
N3 = input()
T.check(N1,N2,N3)           
