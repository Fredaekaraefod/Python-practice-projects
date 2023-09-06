# at times you would want to convert the value of a variable from a different value
# birth_year = input("Enter your birth year")
# age = 2023 - birth_year
# print(age)
# now when initally ran, it  gave an error  on line 3, so let's try to convert
birth_year = input("Enter your birth year:  ")
age = 2023 - int(birth_year)
print(age)
