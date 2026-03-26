systms = [2, 4, 8, 10, 16]

Binary = [0, 1]

Quaternary = [0, 1, 2, 3]

Octal = [0, 1, 2, 3, 4, 5, 6, 7]

Decimal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Hexadecimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

def CheckSyst(syst):
    return int(syst) in systms

def CheckNum(num,sysnm):
    sysnm = int(sysnm)
    if sysnm == 2:
        for dg in num:
            if int(dg) not in Binary:
                return False
        return True
    elif sysnm == 4:
        for dg in num:
            if int(dg) not in Quaternary:
                return False
        return True
    elif sysnm == 8:
        for dg in num:
            if int(dg) not in Octal:
                return False
        return True
    elif sysnm == 10:
        for dg in num:
            if int(dg) not in Decimal:
                return False
        return True
    elif sysnm == 16:
        for dg in num:
            if dg not in Hexadecimal:
                return False
        return True
    return False

def Conversion_From_Binary_To_Decimal(Num):
    ans  = 0
    cnt  = len(Num) - 1
    for i in Num:
        if int(i) == 1:
            ans += 2**cnt
        cnt -= 1
    return ans

def Conversion_From_Quaternary_To_Decimal(Num):
    ans = 0
    cnt = len(Num) - 1
    for i in Num:
        ans += int(i)*(4**cnt)
        cnt -= 1
    return ans

def Conversion_From_Octal_To_Decimal(Num):
    ans = 0
    cnt = len(Num) - 1
    for i in Num:
        ans += int(i) * (8 ** cnt)
        cnt -= 1
    return ans

def Conversion_From_Hexadecimal_To_Decimal(Num):
    ans = 0
    cnt = len(Num) - 1
    for i in Num:
        ans += Hexadecimal.index(i)*(16**cnt)
        cnt -= 1
    return ans

def Conversion_From_Decimal_To_Binary(Num):
    Num = int(Num)
    if Num == 0:
        return "0"
    ans = ""
    while Num > 0:
        rmd = Num % 2
        ans = str(rmd) + ans
        Num //= 2
    return ans

def Conversion_From_Decimal_To_Quaternary(Num):
    Num = int(Num)
    if Num == 0:
        return "0"
    ans = ""
    while Num > 0:
        rmd = Num % 4
        ans = str(rmd) + ans
        Num //= 4        
    return ans

def Conversion_From_Decimal_To_Octal(Num):
    Num = int(Num)
    if Num == 0:
        return "0"
    ans = ""
    while Num > 0:
        rmd = Num % 8
        ans = str(rmd) + ans
        Num //= 8
    return ans

def Conversion_From_Decimal_To_Hexadecimal(Num):
    Num = int(Num)
    if Num == 0:
        return "0"
    ans = ""
    while Num > 0:
        rmd = Num % 16
        ans = Hexadecimal[rmd] + ans
        Num //= 16
    return ans

def slv(sysnm, num, cvnm):
    sysnm = int(sysnm)
    cvnm = int(cvnm)
    
    if sysnm == 2:
        dec = Conversion_From_Binary_To_Decimal(num)
    elif sysnm == 4:
        dec = Conversion_From_Quaternary_To_Decimal(num)
    elif sysnm == 8:
        dec = Conversion_From_Octal_To_Decimal(num)
    elif sysnm == 10:
        dec = int(num)
    elif sysnm == 16:
        dec = Conversion_From_Hexadecimal_To_Decimal(num)
    
    if cvnm == 2:
        result = Conversion_From_Decimal_To_Binary(dec)
    elif cvnm == 4:
        result = Conversion_From_Decimal_To_Quaternary(dec)
    elif cvnm == 8:
        result = Conversion_From_Decimal_To_Octal(dec)
    elif cvnm == 10:
        result = str(dec)
    elif cvnm == 16:
        result = Conversion_From_Decimal_To_Hexadecimal(dec)
    
    print(f"Number in {cvnm} system is : {result}")


sysnm = input("Enter the system name : ")

if not CheckSyst(sysnm):
    print("Invalid System Name")
    exit()

num = input("Enter number : ")

if not CheckNum(num, sysnm):
    print("Invalid Number")
    exit()

cvnm = input("Which system do you want to convert to : ")

if not CheckSyst(cvnm):
    print("Invalid System Name")
    exit()

slv(sysnm,num,cvnm)