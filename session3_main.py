# if 4 < 2:
#     print('ok')


# name = 'alireza'
# if name == 'alireza':
#     print(f"Hello {name}")



# number = 22

# if number % 2 == 0:
#     print("It is Even")
#     c = 4 + 5
#     print(c)




user_input = int(input("Enter a number mate: "))
if user_input % 2 != 0:
    print("damet garm.")


name = input("Enter your name: ")

if len(name) >= 5:
    print('salam')

else:
    print("len is under 5")



if len(name) >= 10:
    print(f"Len is {len(name)}")

else:
    print("boro bache sal")

age =int(input("enter your age: "))
if age > 18:
    print("bro to")

elif age == 18:
    print("bezar fekramo bokonam hala")

else:
    print("bro bache")


height = float(input("Enter your height: "))
if height < 150:
    print("moosh bokhoratet")

elif   170 >= height > 150:
    print("ghadet badak ni")

else:
    print("dadashami")



number=int(input("enter your height:"))
number2=int(input("enter your hight: "))

if number > number2:
    print("The bigger number is :", number)

elif number2 > number:
    print("The bigger number is :", number2)

else:
    print('both are same')

nomreha = []
d1 = float(input(": "))
d2 = float(input(": "))



if d1 > d2:
    nomreha = [d1]


else:
    nomreha = [d2]


print(nomreha)



hava=int(input("darage hava chande: "))
if hava >40 :
    print("vaaaayyy kheily garme: ")


elif hava >10 and hava < 40:
    print("yekam kheily garme: ")


else:
    print("khoooobeee")


# logical operator = or - and

# if 23 < 5 or (and) 7 > 14 or 2 > 1 :
#     print('salam') 


# list methods
number = int(input(": "))
list = [3,7,5,1]

# 1 = append 
list.append(number)
print(list)

# 2 = clear
list.clear()
print(list)

# 3 = pop and remove
list.pop()
list.pop()
list.pop()
print(list)

list.remove(50)
print(list)

# 4 = index
index = list.index(5)
print(index)

list=[3,21,46,1,7,9,15]
a=int(input("ye adad: "))
# list.append(a)
print(list)

list.remove(6)
print(list)

# 5 = sort
list.sort(reverse=True)
print(list)
