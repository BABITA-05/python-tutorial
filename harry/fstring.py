letter = "hey my name is {1} and i am from {0}"
country = "india"
name = "babita"
print(letter.format(country, name))

print(f"Hey my name is {name} and i am from {country}")
price = 49.09999
txt = f"for only {price: .2f} dollars!"
print(txt)
# print(txt.format(price = 49.09999))