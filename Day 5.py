#!/usr/bin/env python
# coding: utf-8

# In[45]:


print('\t---< GPA Calculator >---\n')

#function to calculate GPA
def calculate_gpa(title1, title2, title3, title4, title5, title6="AI Lab"):
    subjects=[title1, title2, title3, title4, title5, title6]
    earned_credits=[]
    total_credits=[]

    #taking input for each subject 
    print("\n-- Enter Subject Details --")
    #subject 1
    earned1=float(input(f'\nEnter the credit earned in {title1}: '))
    credit1=float(input(f'Enter the total credit hours for {title1}: '))
    earned_credits.append(earned1)
    total_credits.append(credit1)

    #subject 2
    earned2=float(input(f'\nEnter the credit earned in {title2}: '))
    credit2=float(input(f'Enter the total credit hours for {title2}: '))
    earned_credits.append(earned2)
    total_credits.append(credit2)

    #subject 3
    earned3=float(input(f'\nEnter the credit earned in {title3}: '))
    credit3=float(input(f'Enter the total credit hours for {title3}: '))
    earned_credits.append(earned3)
    total_credits.append(credit3)

    #subject 4
    earned4=float(input(f'\nEnter the credit earned in {title4}: '))
    credit4=float(input(f'Enter the total credit hours for {title4}: '))
    earned_credits.append(earned4)
    total_credits.append(credit4)

    #subject 5
    earned5=float(input(f'\nEnter the credit earned in {title5}: '))
    credit5=float(input(f'Enter the total credit hours for {title5}: '))
    earned_credits.append(earned5)
    total_credits.append(credit5)

    #subject 6
    earned6=float(input(f'\nEnter the credit earned in {title6}: '))
    credit6=float(input(f'Enter the total credit hours for {title6}: '))
    earned_credits.append(earned6)
    total_credits.append(credit6)

    #calculate total
    total_earned=sum(earned_credits)
    total_credit=sum(total_credits)
    gpa = total_earned / total_credit

    #display table
    print("\n---< RESULT >---")
    print(f"{'Subject':<15}{'Credit Earned':<15}{'Credit Hours':<15}")
    print("-"*42)
    for i in range(len(subjects)):
        print(f"{subjects[i]:<15}{earned_credits[i]:<15}{total_credits[i]:<15}")
    print("-"*42)
    print(f"{'TOTAL':<15}{total_earned:<15.2f}{total_credit:<15.2f}")
    return round(gpa,2)

#calling function using named arguments 
result = calculate_gpa(title1="OS",title2="DSA", title3="NIC",title4="OOP",title5="AI")

#result
print(f"\n >>> Your GPA is: {result:.2f}")




# In[ ]:




