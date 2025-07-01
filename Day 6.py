#!/usr/bin/env python
# coding: utf-8

# # Day 6

# In[ ]:


def evaluate_grade(score):
    if score>=90 and score<=100:
        grade = 'A'
    elif score>=85 and score<=89:
        grade = 'A-'
    elif score>=80 and score<=84:
        grade = 'B+'
    elif score>=75 and score<=79:
        grade = 'B'
    elif score>=70 and score<=74:
        grade = 'B-'
    elif score>=65 and score<=69:
        grade = 'C+'
    elif score>=60 and score<=64:
        grade = 'C'
    elif score>=50 and score<=59:
        grade = 'D'
    elif score<50:
        grade = 'F'
    else:
        print('Invalid score!')
    return grade

def print_grade_summary(student_name= 'Unnamed', score= 0.0):
    if score<0 or score>100 :
        print(f'--> Invalid!. Please enter a value between 0 and 100.')
        __main__()
    else:
        print(f'\n--> Student {student_name} scored {score} -> Grade: {evaluate_grade(score)}')


def __main__():
    name=input('\nEnter your name: ').capitalize()
    score=float(input('Enter your score(0-100): '))
    print_grade_summary(score=score, student_name=name)

print('\t---> Score Based Grading System')
__main__()


# In[ ]:




