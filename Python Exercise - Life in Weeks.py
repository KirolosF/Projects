# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

new_age = int(age)

x = int((90 * 365) - (new_age * 365))
y = int((90 * 52) - (new_age * 52))
z = int((90 * 12) - (new_age * 12))

print(f"You have {x} days, {y} weeks, and {z} months left.")

