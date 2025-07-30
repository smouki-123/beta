#listas (mutable)
import os
os.system('cls')


my_list = [1,2,3, True, False, "apple", 2j, 3.14, ['mazda', 'ford', 'audi']]
for x in my_list:
    print(x)
my_list[1] = ['banano', 'mango']
print(my_list)
print(type(my_list[6]))




#print(my_list)
#print(my_list[8])
#print(my_list[8][1])
#print(type(my_list))


#tuplas (inmutable)

my_tupla = (1, 2 ,3)
print(type(my_tupla))
print(my_tupla)
#my_tupla[0] = 10
#print(my_tupla)

#diccionarios (mutables)

my_data = {
    "firstime": "johan",
    "lastnme": "ayala",
    "city": "col"
}
print(my_data)
print(my_data["firstime"])

name = "johan"
for n in name:
    print(n)
print(name[3])