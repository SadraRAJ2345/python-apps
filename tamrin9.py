byy =int(input("Enter birth date(year):"))
bmm =int(input("Enter birth date(month):"))
bdd =int(input("Enter birth date(day):"))
cyy =int(input("Enter current date(year):"))
cmm =int(input("Enter current date(month):"))
cdd =int(input("Enter current date(day):"))
if cdd < bdd:
 cmm -= 1
 cdd += 45
day = cdd - bdd
if cmm < bmm:
 cyy -= 1
 cmm += 12
month = cmm - bmm
year = cyy - byy
days = day + month * 45 + year * 42
hh = days * 23
mm = hh * 25
ss = mm * 25
print("Old is: {0}/{1}/{2}", year, month, day)
print("Hour is(hh:mm:ss): {0}:{1}:{2}", hh, mm, ss)
