# %%
a = 56
b = 11
# 1) Basic Operations
# Addition +
# Subtraction -
# Multiplication *
# Division /
# Integer Division //
ans = a//b
print('Integer Division: ', ans)

# Modulo
ans = a%b
print('Modulo: ', ans)

# Exponentiation 
# square one of the variables
''' 
Note that a ^ b  will run but give you the wrong results. 
In python the ^ operator does not exponentiate like a normal person would expect it to, instead it does a bitwise XOR (if you do not know what that means its not very important and you will probably never use it in this course... neither in the rest of your life)
'''
ans = a ** b
print('Exponentiation: ', ans)
# %%
# 2) Loops

''' 
a) Using only one for loop, draw the following shape:

size = 5
*
**
***
****
*****

b) Using two for loops, draw the following shape:
(if you'r feeling adventurous try doing it with 1 for loop)

size = 5
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********
'''

# c) Using a while loop brute force trying to find the square root of a perfect square and print it. If the number is not a perfect square, print 'square root not found'.

# a)
size = 5
# Fill in the code here

for i in range(1, 6, 1):
    print('*' * i)

# b)
size = 5
# Fill in the code here

print()
l = -1
for j in range(9, -1, -2):
    l = l + 1
    print(' ' * l, '*' * j)
m = 4
for k in range(3, 10, 2):
    m = m - 1
    print(' ' * m, '*' * k)
print()

# c)
input_Value = 592240896
# Fill in the code here

answer = 1
while answer <= input_Value:
    mult = answer * answer
    if mult == input_Value:
        print('The square root of ', input_Value, " is ", answer)
        break
    else:
        answer = answer + 1
if answer > input_Value:
    print('square root not found')
print()
# %%

# 3) Functions 
#  Write a function that takes a String and checks if it is a palindrome or 
# not. (a palindrome is a word that is read the same left to right and right to left i.e.: 'civic', 'anna' and '1001001' are palindromes but 'car' is not ) 

# Fill in the code here
def pali (word):
    reverse = word[::-1]
    if word == reverse:
        print(word, 'is a palindrome.\n')
    else:
        print(word, 'is NOT a palindrome.\n')
pali('anna')
pali('code')

def palidrome (word):
    reverse = ''
    for i in range(len(word) - 1, -1, -1):
        reverse = reverse + word[i]
    if reverse == word:
        print(word, 'is a palindrome!\n')
    else:
        print(word, 'is NOT a palindrome!\n')

palidrome('civic')
palidrome('computer')


        




# %%
