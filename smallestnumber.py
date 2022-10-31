# Write a program whose inputs are three integers, and whose output is the smallest of the three values.

user_num = int(input())

user_num2 = int(input())

user_num3 = int(input())

if user_num < user_num2 and user_num < user_num3:
    
    print(user_num)
    
elif user_num > user_num2 and user_num2 < user_num3:
    
    print(user_num2)
    
else:
    
    print(user_num3)