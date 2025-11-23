name = input("Enter your full name: ")
city = input("Enter your city: ")

while True:
    age_input = input("Enter your age: ")
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("Please enter a valid number!")

print("Checking info...")


print("Your full name is : ",name)
print("Your city is :", city)
print("Your age is :", age)


