#   Author : Nekyz
#   Date : 30/06/2015
#   Project Euler Challenge 3
# Using the fact that anw integer greater than 1 is either a prime number or can
# be written as unique product of prime number

def largest_prime_factor(n: int) -> int:
    result = 0
    temp_number = n
    #First prime number
    divisor = 2
    # While we have a product inferior to the number
    while divisor * divisor <= n:
        if temp_number % divisor == 0:
            temp_number = temp_number / divisor
            result = divisor
        else:
            if divisor == 2:
                divisor = 3
            else:
                divisor += 2
    if temp_number > result:
        result = temp_number

    return result

print("####################################")
print("Project Euler, Largest prime factor.")
print("####################################")

while True:
    entered_number = input("Please your number : ")
    if entered_number.isdigit():
        if int(entered_number) > 0:
            break
    else:
        print("Please enter a number greater than 0.");

print("Your number is : ", entered_number)
print("The sum of the even fibonacci lesser than your number is : ",
      largest_prime_factor(int(entered_number)))

