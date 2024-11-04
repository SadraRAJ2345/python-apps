# dictionary
d1 = {"First_name" : "Alireza", "Age": 34} # Items ->> Key value pair

# print(len(d1))

# what's difference between line 7 and 8?
# print(d1.get("First_nasfdsfme"),"not found")
# print(d1["First_nadsme"])

# d1.clear()
# copy_d1 = d1.copy()
# ks = d1.keys()
# vl = d1.values()
# it = d1.items()
# kes = ["F1","F2","F3"]
# new_dict = d1.fromkeys(kes,"OK")

# r = d1.setdefault("Firfst_name","None")
# print(r)
# print(d1)

# -----------------------------------------
# dict = {
#     "name": "",
#     "age": ""
# }
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# dict["name"] = name
# dict["age"] = age
# print("Done")
# print(dict)

# final_list = []
# dict = {
#     "id":"",
#     "height":""
# }

# for i in range(4):
#     id=int(input("enter your id: "))
#     height=int(input('enter your height: '))
#     dict["id"]=id
#     dict["height"]=height
#     final_list.append(dict)
# print(final_list)

# ------------------------------

# numbers = [2,9,23,65,78,4,11]
# slice in python
# print(numbers[0:2])
# print(numbers[5:7])
# print(numbers[0:7:2])
# print(numbers[2:5:3])
# print(numbers[3:2:1])
# print(numbers[-1:-4:-1])
# print(numbers[5:-1:-1])
# print(numbers[::-1])

# -----------------------------------
# nums = [0,1,2,3,4,5,6,7,8,9,10]
# print(nums[::2])
# print(nums[1::2])

# ----------------------------
# List Comprehension
# list = [i for i in range(1, 501,2)]
# print(list)


# list = [i for i in range(0,1001,2)]
# # print(list)
# u=0
# for i in list:
#     u+=i
# print(u)