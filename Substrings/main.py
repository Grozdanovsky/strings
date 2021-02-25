string = "cefi i viktor odat asdasddasd"
substring = "cefi viktor neso ovo ono asdasddasd"
final = ""
list1 = string.split(" ")
list2 = substring.split(" ")
max = 0
for item in list1:

    if item in list2:
      lenght = len(item)
      if lenght > max:
          final = item
          max = lenght

print(final)

