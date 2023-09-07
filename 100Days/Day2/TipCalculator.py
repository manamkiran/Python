#Strings
# print('Hello'[0])

#Integers
# print('123'+'456')

# print(123+456)

# underscore is ignored in numners and can be used a demarcator
# print(123_456_789)

# #Float
# print(1234.567890)

# Boolean

# print(12==12) 

# print(12==13)

# Coding Challenge 
# inp =input('Enter a 2 digit number \n')
# sum=0
# for x in inp:
#     sum+=int(x)

# print('Sum is '+str(sum))

# # BEMDAS
# print(3*3+3/3-3)

# print(3*(3+3)/3-3)

# BMI
# height = float(input('enter your height in meter :'))
# weight = float(input('enter your weight in kilogram :'))

# print('Your BMI is :' + str(round(weight/height**2)))
# round(8/3,2) # round to precision of 2
# print(8 // 3) # // does a floor with divison

# F String
# score = 0
# print (f'yor score is {score}')

# # Weeks in life

# age = input('What is your current age?\n')
# rem=90-int(age)
# print(f'You have {rem*365} days {rem*52} weeks and {rem*12} months left')

# formating
a=12.9499999999999999
print('{:.2f}'.format(a))

# Tip Calculator
print('Welcome to the tip calculator')
bill=input('What was the total bill? ')
tip=input('What percentage tip would you like to give? 10,12,or 15? ')
persons=input('How many people to split the bil? ')
print(f'Each person should pay {round(float(bill)*(100+int(tip))/100/int(persons),2)}')
