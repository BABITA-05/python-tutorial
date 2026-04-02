#strings are immutable
a = " Babita Bhandari !!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.strip())
print(a.rstrip("!"))
print(a.replace("Babita", "Bijaya"))
print(a.split(" "))
print(a.capitalize())

#center
str1 = "Welcome to the console"
print(len(str1))
print(len(str1.center(50)))

str1 = "welcome to the console"
print(str1.count("e"))
print(str1.endswith("!"))