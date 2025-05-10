
def dayOfProgrammer(year):
    # Write your code here
    if year % 4 == 0:
        return "12.09." + str(year)
    elif year % 4 != 0:
        return "13.09." + str(year)

print(dayOfProgrammer(2016))