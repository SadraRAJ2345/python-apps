# file in python - temporary and permanent (json,pickle, csv, txt)

# my_name = "alireza"
# file = open("names2.txt","w")

# file.write(my_name)

#  --------------------------------
# name = input("Enter Your name: ")
# f = open("files/name.txt","w")
# f.write(name)
# ----------------------------------
# file = open("files/id.txt","w")
# for i in range(4):
#     id_ = input("Enter Your Id: ")
#     file.write(id_)
#     file.write("\n")
# ---------------------------------
# file=open("files/names.txt","w")
# for i in range(5):
#     name=input("enter yours names: ")
#     if len(name) >= 5:
#         file.write(name)
#         file.write("\n")
# --------------------------------
# file = open("files/info.txt","r+")
# info = file.read()
# print(info)
# -------------------------------
# file=open("files/info.txt","r")
# data=file.read()
# print(data)
# -----------------------------
# file = open("files/info.txt","r")
# data_list = file.readlines()
# print(data_list)
# ------------------------
# import time

# file = open("files/info.txt","r")
# data_list = file.read()
# print("Welcome to our program please signup first.")
# time.sleep(3)
# name = input("Enter a name: ")

# if name in data_list:
#     print("repetetive name.")
# else:
#     print("great")
# --------------------------------
# number = 76958967
# l = []
# for i in str(number):
#     l.append(int(i))

# print(sum(l))

# ------------------------------

file = open("files/aw.txt","a")
file.write("Alireza")