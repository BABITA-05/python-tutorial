#strings are immutable
a = "Babita Bhandari"
print(len(a))
print(a.upper())
print(a.lower())

#strip removes whitespace befor and after the string
a = " Babita Bhandari !!!"
print(a.strip())
#rstrip le chai removes any trailing character
a = " Babita Bhandari !!!"
print(a.rstrip("!"))

a = "Babita Bhandari"
print(a.replace("Babita", "Bijaya"))
print(a.split(" "))
#capitalize le chai turn first letter of string capital ani baki lai chai lowercase ma
print(a.capitalize())

#center
str1 = "Welcome to the console"
print(len(str1))
print(len(str1.center(50)))

str1 = "welcome to the console"
print(str1.count("e"))
print(str1.endswith("!"))
print(str1.endswith("to", 4, 10 ))
print(str1.find("to"))

str1 = "welcometotheconsole1"
print(str1.isalnum())
str1 = "welcometotheconsole"
print(str1.isalpha())
print(str1.islower())
str1 = "welcome to the console1\n"
print(str1.isprintable())
print(str1.title())
print(str1.swapcase())
str1 = " "
print(str1.isspace())
str1 = "Welcome To Theconsole1\n"
print(str1.istitle())
