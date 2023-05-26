print('''
                                        
 █▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ ▀█▀ █▀█ █▀█
 █▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄''')
print()
print("     _______A______  ATIF  ________H_______")

print()
print(" Program Start")
print ("  ___________")
print()


def startt():
    num1 = int(input(" [~~] Enter First Number : "))
    
    print()
    print(" ---------------------------")
    print(" ---------------------------")
    print()
    
    num2 = int(input(" [~~] Enter Secound Number : "))
    print()
    opr = input(" [~~] Enter Any Opration > + - x / : ")
    
    print()
    print(" ---------------------------")
    print(" ---------------------------")
    print()

    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def dev(a, b):
        return a / b



    if opr == '+':
        print(" [ ANS ]" , num1, "+", num2, "=", add(num1, num2))

    elif opr == '-':
        print(" [ ANS ]" ,num1, "-", num2, "=", sub(num1, num2))
        
        print()

    elif opr == 'x':
        print(" [ ANS ]" ,num1, "x", num2, "=", mul(num1, num2))
        
        print()

    elif opr == '/':
        print(" [ ANS ]" ,num1, "/", num2, "=", dev(num1, num2))
        
        print()

    else:
        print(" [ !!!! ] Wrong Oprater Sellect !")
        print()
        

    program = input(" [~~] Enter N for EXIT & Y for RESTART : ")

    if program == 'y':
        startt()

    else:
        print(" [ TNKS ] Thank You Calculator is Exit ")


startt()




