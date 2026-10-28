space=7
star=1
for i in range(1,8):
    for j in range(1,8):
        if j==2:
            print("* ",end="")
        elif i==7 and 9<= (i+j) <=13:
            print("* ",end="")
        elif i==1 and 4<= i+j <=7:
            print("* ",end="")
        elif j==7 and i+j==9:
            print(" "*space+"*"*star,end="")
        elif j==7 and i+j==10:
            print(" "*space+"*"*star,end="")
        elif i==4 and 7<= i+j <=10:
            print("* ",end="")
        elif j==7 and i+j==12:
            print(" "*space+"*"*star,end="")
        elif j==7 and i+j==13:
            print(" "*space+"*"*star,end="")
            
    print()
