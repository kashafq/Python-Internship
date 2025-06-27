#!/usr/bin/env python
# coding: utf-8

# In[27]:


#Day 4 Task
print('        ---< STUDENT RECORD SYSTEM >---\n')

#tuple to store student IDs
student_id=(102, 203, 111, 139,457)
print(f'Student IDs: {student_id}')

#set containing course names
course_name={"AI","ML","OS"}

#displays list of courses
print(f'\n--< Course List >--')
for course in course_name:
    print(course)
    
print('\n') 

#taking input from the user to add a course
add_course=input("- Enter a course you would like to add: ").upper()
course_name.add(add_course)
print(f'Updated Courses: {course_name}')

#taking input from the user to add a course
remove_course=input("\n- Enter a course you would like to remove(from the course list): ").upper()
course_name.remove(remove_course)
print(f'Updated Courses: {list(course_name)}')

#displays final updated course list
print(f'\n--< Final Course List >--')
for course in course_name:
    print(course)


# In[ ]:




