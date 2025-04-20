from datetime import datetime
#Data and variable types
name = "Uday"
age = 28
DOB = datetime(1999, 4, 8)
ages = age
'''
1.Variable identifiers can be from a to z, A to Z, 0-9, and underscore (_) only.
2.Identifiers cannot start with digits, such as "1variable".
3.Identifiers can be of any length.
4.Python can analyze datatype automatically
5.Datatypes are integer(number),String(words),Float(decimals),Boolean(T or F) and none(No values are stored in it)
'''

print("My name is ",name + " and Age is ",age)
print("My name is ",name + " and Age is ",ages)
print(type(ages))

'''
Reserved keyboards for variables:
    False      await      else       import     pass
    None       break      except     in         raise
    True       class      finally    is         return
    and        continue   for        lambda     try
    as         def        from       nonlocal   while
    assert     del        global     not        with
    async      elif       if         or         yield
'''

num1 = 2
num2 = 4
Sam = num1 + num2
print("The sum of number1 and numnber2 is ",Sam)

a = "4"
c = int(a)
b = 3.2
print(type(a))
print(type(c))
print("Sum of a and b", b+c)