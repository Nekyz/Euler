#   Author : Nekyz
#   Date : 29/06/2015
#   Project Euler Challenge 1

def sum_of_multiple_of_3_and_5(number: int) -> int:
    result = 0
    for num in range(0, number):
        if num % 3 == 0:
            result += num
        elif num % 5 == 0:
            result += num
    return result


print("###################################")
print("Project Euler, multiple of 3 and 5.")
print("###################################")

while True:
    entered_number = input("Please enter the maximum number: ")
    if entered_number.isdigit():
        if int(entered_number) > 0:
            break
    else:
        print("Please enter a number greater than 0.");

print("Your number is : ", entered_number)
print("The sum of the multiple of 3 and 5 inferior at your number are: ",
      sum_of_multiple_of_3_and_5(int(entered_number)))
