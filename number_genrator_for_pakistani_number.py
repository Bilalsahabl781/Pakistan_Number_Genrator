#importing random module
import random

# a user input for first four digit of the number
user_first_four_digit = input("Enter your first four digit: ")
# a user input for how many numbers he/she wants to generate
how_many_numbers = int(input("How many numbers do you want to generate? "))
# a for loop to generate the numbers
for i in range(how_many_numbers):
    last_7_digit = random.randint(0, 9999999)
    print(f"{user_first_four_digit + str(last_7_digit)}")
# after donw this will print
print("Here is your requested numbers which are generated randomly.The ammount of number is: ", how_many_numbers)
# credit to Umar Aslam