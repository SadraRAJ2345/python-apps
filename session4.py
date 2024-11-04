# اپند چی بود؟
list = [6,8]
list.append(12)
print(list)
# -------------------------
list  = [4,8,9]
list.insert(0,'ali')
print(list)
# ----------------------
list = [3,6]
r = list.index(6)
print(r)
# -------------------
list = [6,8,9]
list.pop()
list.pop()
print(list)
# -------------------------
list1 = ['a']
main = [3,6]
main.extend(list1)
print(main)
# ----------------------
list = [4,7,8]
list.reverse()
print(list)
# --------------------
id = 1
humans = ['amir','mohammad', 'sara',"sepide"]
for name in humans:
    # print('Hello', name)
    # print(len(name))
    print(id, ":",name)
    id += 1
# ------------------------
names = ['amir','mohammad',"saman","abbas","hooshang"]
for i in names:
    if len(i) >= 6:
        print(f'salam {i}') 
    else:
        print("hal nemikonam bat") 
# ----------------------------
numbers = [24,54,78,6564,76,563,437,647,53436]
even = 0
for i in numbers:
    if  i  % 2 ==0:
        even += 1

print(even)
# ----------------------------
numbers = [4,6,2,43,643,4,524,6,46,54,8,5,35,64,75,6,45,4,2]
even_numbers = []
odd_numbers = []
for i in numbers:
    if i % 2==0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
    
print("Even numbers are: ",even_numbers)
print("Odd numbers are: ", odd_numbers)
# -----------------------------
average = [14.25,16.30,14.80,19.71,16.71,15.36,14.80,19.02,17.06]
best = 0
for i in average:
    if i > best:
        best=i

print(best)
# --------------------------------
hoghogh=int(input("hoghoghet chande? "))
tax= hoghogh * 0.20
final=hoghogh - tax
print(final)
