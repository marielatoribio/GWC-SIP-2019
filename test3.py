str1= "fireflies"
str2= "another"
display = ""
temp= ""
for letter in str1:
    if letter not in str2:
        display+= letter
        temp+= letter
    else:
        temp+= letter
        print(temp)

print(display)
