# anything encloses in single or doble quotation marks is considered as the string, it;s a array od textual data

name=input("enter your name")
print("Hello! " + name)

print("Hey, i am me")
print("Hey!, i'm me ")
#ca be this print("Hello, he said, "i want to eat mango" ")

#multiline bhaneko triple double or single quotation marks bhitra, like
print("""hey
      hi
      how are you!
      """)


#accessing characters in string
print("Let's use a for loop\n")
for character in name:
    print(character)