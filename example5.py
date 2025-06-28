#script description

'''
1. get 2 numbers (float or integer)
2. show mai menu:(1). add, (2). sub, (3). mul, (4). div
3. selec an option
4. create a fuction get the result according with the opt
other: clear screen

'''
import os

''''
def calc1(x, y, z):
    if (z == '1'):
        ans = x + y

    if (z == '2'):
        ans = x - y
    if (z == '3'):
        ans = x * y
    if (z == '4'):
        ans = x / y


    return ans
##tipo espagueti

def calc2 (x, y, z):
     if (z == '1'):
        ans = x + y
     else:
        if (z == '2'):
            ans = x - y
        else:
            if (z == '3'):
                ans = x * y
            else:
                if (z == '4'):
                    ans = x / y

     return ans
'''
def calc3 (x, y, z):
    if (z == '1'):
        ans = x + y
    elif (z == '2'):
        ans = x - y
    elif (z == '3'):
        ans = x * y
    elif (z == '4'):
        ans = x / y
        if (x, y / 0):
            ans = "no se puede dividir entre 0"
    else:
        ans = (x + y, x - y, x * y, x / y)

    return ans
### main #################
num1 = float(input('press first number'))
num2 = float(input('press second number'))


print ("### MAIN MENU ###")
print ("[1]. add")
print ("[2]. sub")
print ("[3]. mult")
print ("[4]. div")
opt = input("::. press any option: ")
print(type(opt))
os.system('pause')

#print(type(opt))
#os.system('pause')
'''''
res1 = calc1 (num1, num2, opt)
print (f"the result with f1 is: {res1}")

res2 = calc2 (num1, num2, opt)
print (f"the result with f2 is: {res2}")
'''
res3 = calc3 (num1, num2, opt)
print (f"the result add is: {res3[0]}")
print (f"the result rest is: {res3[1]}")
print (f"the result mul is: {res3[2]}")
print (f"the result div is: {res3[3]}")