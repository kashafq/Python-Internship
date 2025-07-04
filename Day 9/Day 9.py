#!/usr/bin/env python
# coding: utf-8

# ## Day 9

# In[108]:


print('---< Students Marks Reader >---\n')

def read_marks_file(filepath):
    marks={}
    skip=0
    try:
        with open(filepath, 'r') as file:
            for line in file:
                try:
                    name,score= line.split(',')
                    if not name or not score:
                        raise ValueError
                    score = int(score) 
                    marks[name] = score
                except ValueError:
                    skip+=1
    except FileNotFoundError:
        print('File not found!')

    else:
        print('Reading the file...\n')
        print(f'Finished reading the file.\n! There were {skip} invalid entries.')
        return marks
    

def print_summary(marks_dict):
    if not marks_dict:
        print('No valid enteris found in the dictionary!')
    else:
        print('\n--⊣ Displaying Student Marks ⊢--\n')
        for name, score in marks_dict.items():
            print(f' ⚬ {name} ➝ {score}')

        sum_of_marks=sum(marks_dict.values())
        count=len(marks_dict)
        try:
            avg=sum_of_marks/count
            if count != 0:
                print(f'\n➝ Average Score: {avg:.2f}')
            else:
                raise ZeroDivisionError()
        except ZeroDivisionError:
            print('There is no data in file!')

def __main__():
    filepath=input(r"Enter Student Data file path: ")
    marks_data=read_marks_file(filepath)
    print_summary(marks_data)

__main__()


# In[ ]:




