#   Author : Nekyz
#   Date : 29/06/2015
#   Project Euler Challenge 2

def sum_fib_even(n: int) -> int:
    fib_number, temp_number = 1, 1
    result = 0
    # If the fibonacci is even we add it
    while fib_number <= n:
        if fib_number % 2 == 0:
            result += fib_number
        # Fibonacci formula : temp_number is always the next in the fibonacci sequence
        fib_number, temp_number = temp_number, fib_number + temp_number
    return result


print("####################################")
print("Project Euler, Even Fibonacci Number.")
print("####################################")

while True:
    entered_number = input("Please enter the maximum number: ")
    if entered_number.isdigit():
        if int(entered_number) > 0:
            break
    else:
        print("Please enter a number greater than 0.");

print("Your number is : ", entered_number)
print("The sum of the even fibonacci lesser than your number is : ",
      sum_fib_even(int(entered_number)))
