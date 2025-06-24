#lets create a object called "a" and assign it the number 5
a = 5
print(a)

print(a + a)

#reassign the value of a to 11
a = 11
print(a)

#use a to redefine the value of a
a = a + a
print(a)
"""
verable rules:
1. names can not start with a number.
2. names can not have spaces. insted use _.
3. cant use any of these symbols: !@#$%^&*()[]{};:'",.<>?/\|`~+=-
4. its considered best preactice (pep8) that names should be lowercase.
5. avoid carictors that look like numbers, such as l, O, and I.
6. abiode useing words that are reserved in python, such as def, class, if, else, etc.
"""
s="test"
print(s[:1])# get the first character
print(s[1:])# get the rest of the string
print(s[1:3])# get the second and third character
print(s[::-1])# reverse the string

#concatenate strings
print(s + "ing")  # adds "ing" to the end of the string

s = "test does this work?"
print(s.split())  # splits the string into a list of words
s_list = list(s.split())  # splits the string into a list of words
print(s_list)  # prints the list of words