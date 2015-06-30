#   Author : Nekyz
#   Date : 30/06/2015
#   Project Euler Challenge 3
# Largest palindrome of 2 three digit number

def is_palindrome (n):
    # Reversing n to see if it's the same ! Extended slice are fun
    if str(n) == (str(n))[::-1]:
        return True
    return False

max = 0
for i in range(999,100,-1):
    for j in range (999,100,-1):
        product = i * j
        if is_palindrome(product):
            if (product > max):
                max = product
                print(i," * ",j," = ", product)

print("Max palindrome is : ", max)
