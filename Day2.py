#!/usr/bin/env python
# coding: utf-8

# In[31]:


print('--< DAY 2 >--\n')
name=input("Enter you full name; ")
first_name=name[:6]
last_name=name[7:]
print(f'First Name: {first_name.capitalize()}')
print(f'Last Name: {last_name.capitalize()}')


print('\n\n---< Calculator >---\n')
first_number=input("Enter a number: ")
Second_number=input("Enter another number: ")

add=float(first_number)+float(Second_number)
sub=float(first_number)-float(Second_number)
div=float(first_number)/float(Second_number)
multiply=float(first_number)*float(Second_number)

print(f'\nAddition:         {first_number} + {Second_number} = {add}')
print(f'Subtraction:      {first_number} - {Second_number} = {sub}')
print(f'Division:         {first_number} / {Second_number} = {div}')
print(f'Multiplication:   {first_number} x {Second_number} = {multiply}')



# In[ ]:




