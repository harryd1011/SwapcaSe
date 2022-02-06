a = input()
str1 =''
for i in a:
  if i== i.upper():
    str1 += i.lower()
  elif i== i.lower():
    str1 += i.upper()
  else:
    str1 += i
print(str1)
