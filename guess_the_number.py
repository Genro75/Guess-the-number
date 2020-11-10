#actual_num user_num count
import random

user_num = int(input("Guess the number : "))
x=True
count=1
actual_num = random.randint(1,101)

while x:
    if user_num == actual_num:
        break
    elif user_num > actual_num:
        print("your number is greater than the actual number")
    elif user_num < actual_num:
        print("your number is smaller than the actual number")
    count += 1
    user_num = int(input("try again : "))


print("\n\nYou Won\nyou took " + str(count) + " move to succeed")
