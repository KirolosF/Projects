# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined = name1 + name2
lower_combined_name = combined.lower()

t = lower_combined_name.count("t")
r = lower_combined_name.count("r")
u = lower_combined_name.count("u")
e = lower_combined_name.count("e")

true = t + r + u + e

l = lower_combined_name.count("l")
o = lower_combined_name.count("o")
v = lower_combined_name.count("v")
e = lower_combined_name.count("e")

love = l + o + v + e

truelove = int(str(true) + str(love))

if (truelove < 10) or (truelove > 90):
    print(f"Your score is {truelove}, you go together like coke and mentos.")
elif (truelove >= 40) and (truelove <= 50):
    print(f"Your score is {truelove}, you are alright together.")
else:
    print(f"Your score is {truelove}.")









