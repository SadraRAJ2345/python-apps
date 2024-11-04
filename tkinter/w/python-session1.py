# name = "don't"

# print(len(name))

# name2 = "mohammad pedram".count("a")
# name2 = "sepehr".endswith("rt")
# name2 = "sepehr".endswith("Pi")
# name2 = "              sepehr   ".center(100,"*")
# name2 = "sepehr".capitalize()  # title()    # upper()   # lower()
# name2 = "sepehr".find("e") # index()
# name2 = "sepehr".index("e")
# name2 = "".isalnum()
# name2 = "sepehr".isascii()
# name2 = "de?f".isidentifier()








# list = [4,7,8,9]
# # ترتیب
# # متدهای لیست
# # اندکس معکوس
# # اسلایس
# list.append(100)
# list.insert(2,900)
# # list.clear()
# list.remove(8)
# list.pop()
# list2 = [33,44]
# list.extend(list2)
# list.reverse()
# list.sort(reverse=True)



# list2 = [5,8,3,6,1]
# print(list2[2:4]) 


# print(list[-2])



# unppack

# a , b , c = [3,6,8]

# a , b , *c = [2,6,7,9,8,0,9]


# # متغیر همزمان 
# a = 3
# b = 6

# a , b = b , a




# list = ["ali" , "mohammad", "yasin"]
# for i in list:
#     print()


# for index, name in enumerate(list,start=1):
#     print(index , name)


# list = [4,78,54,7,6,48,7656,23]

# temp = 0 
# for i in list:
#     temp += i

# print(temp)


# print(chr(23433))
# print(ord("安"))


# password = int(input(": "))

# version_2 = ""
# for i in str(password):
#    version_2 += (str(ord(i) - 5 ))

# print(version_2)



# version_2 = ""
# for i in str(password):
#    version_2 += str(ord(i) + 5 )

# print(version_2)



# dictionary = {
#     "name": "reza",
#     "age": 0
# }

# key lookup
# print(dictionary["name"])
# print(dictionary.get("nagsdgme","Not Found"))

# new_dict = dictionary.fromkeys(["name", "addr"],10)
# print(new_dict)

# print(dictionary.items())
# print(dictionary.values())
# print(dictionary.keys())
# dictionary.setdefault()

# import os
# current = os.getcwd()
# addr = os.path.join(current, "w")
# os.chdir('C:\\Users\\ASUS\\Desktop\\فایل های دوره\\w')
# print(os.getcwd())


# files = open(r"{0}".format(addr), "w")

# files.write("Salam")


# def operation(a: int, b: int):
#     return a + b


# operation(4, 8)

# def factoriel(number):
#     if number == 1:
#         return 1
#     elif number == 2:
#         return 2
#     else:
#         return factoriel(number - 1) * number
    
# print(factoriel(5))


# name = "mohamadreza".upper()
# print(name)