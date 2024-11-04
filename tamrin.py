# name=("sadra")
# print(name)

# number=int(input("enter your age: "))
# number2=int(input("enter your age2: "))
# print(number * number2)
# print(number ** number2)
# print(number / number2 )
# print(number // number2)
# print(number + number2)

# name=input("your friend name: ")
# name2=input("your friend family: ")
# print(name * name2)

# name=input("your name: ")
# number=int(input("enter your age: "))
# print(name * number)


# A=int(input(" tool mostatil: "))
# B=int(input(" arze mostatil: "))
# print(A * B)

# minute=int(input("enter your age: "))
# print(18*365*24*60*60)
# print(20*365*25*60*60)

# name=("sadra").isupper()
# print(name)


# hoghogh=int(input("hoghogheto bego: "))
# maliat=("20%")
# print("20% - hoghogh")
# hoghoghekhales=("800000")
# print(hoghoghekhales)



# list=[4,8,9,3,12,15,18,24,33,39,30]
# list.sort(reverse=True)
# print(list)



# list=[3,9,5,11,4,2,20]
# index=list.index(11)
# print(index)


# adad=int(input("ye adad: "))
# if adad % 2==0:
#     print(adad**10)

# else:
#     print(adad**5)



# matn=input("yechi bego: ").count("e")


# list=[9,7,3,8,10,2,4,]
# a=input("reverse.true or fulse?: ")
# if a=="k":
#     list.sort(reverse=False)
#     print(list)

# else:
#     list.sort(reverse=True)
#     print(list)


# list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# u=0
# for i in list:
#     u+=i
#     print(u)

# harf='salam mashti'
# vowels = ['a', 'i', 'o', 'u', 'e']
# tedad_harfa = 0
# for i in harf:
#     if i in vowels:
#         tedad_harfa += 1
    
# print(tedad_harfa)

# A={2,5,8}
# B={3,5,7}
# print(A.intersection(B))
# print(A.union(B))


# A=input('enter your Emails:')
# if "@" in A:
#     print("sahih ast")

# else:
#     print("eshtbah")


# A=input("matn:")
# print(A.count(" "))

# list=[9,3,8,6]
# list.sort(reverse=False)
# print(list)

# matn=input('ye matn:? ')
# f=open("files/matn.txt",('w'))
# f.write(matn)
# print(matn.count("a"))

# barayevorod=int(input("enter your passvord :"))
# pasvord =[22334455]
# A = 0
# for i in pasvord:
#     if i > A:
#         B=input("pasvord ra mojadad vared koni")


# else:
#     print("okeye")


# Adad = int(input("adad : "))
# for i in range(Adad + 1):
#     print(i)      


# name = input("your name: ") 
# d1={"a","b","c","d","e","f","g","l","i","r","z",}
# print(name)



# dict={
#     "name": ""  ,
#     "last name": "" ,
#     "naitional code":""
# }

# name=input("enter your name: ")
# last=input("enter your last name: ")
# code=int(input("enter your naitional code: "))

# dict["name"]=name
# dict["last"]=last
# dict["code"]=code
# print(dict)

# file=open("files/dict.txt","w")
# file.write(dict)


# m1={2,4,5,7}
# m2={3,4,1.7}
# print(m1.intersection(m2))
# print(m1.union(m2))


# list=[i for i in range(5,5001)]

# u=0
# for i in list:
#     u+=i
# print(u)


# data=input(":")
# punctuation = ["?",".",",","!",";"]
# alaem_negareshi = 0
# for i in punctuation:
#     t = data.count(i)
#     alaem_negareshi += t
# print(alaem_negareshi)
# m = []
# n = input(": ")
# punctuation = ["?",".",",","!",";"]
# for i in punctuation:
#     if i in n:
#         m.append(i)

# print(m)


# def name(ab:str):
#     for i in ab:
#         if i =="a":
#             ab = ab.replace(i,"f")
#     return ab


# y = name("alireza")

# n=int(input("enter: "))


# f = " "
# a = "*"
# for i in range(8):
#     for j in range(7):
#         print(" ",end="")
#         print(j * f,end=" ")
#     print(a * i)

# def a(a:list):
#     list= []
#     for i in a:
#         h = i ** 2
#         list.append(h)
#         list.sort(reverse=True)
#     return list

# print(a([2,2,3,9,6]))