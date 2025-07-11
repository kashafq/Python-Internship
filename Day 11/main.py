#!/usr/bin/env python
# coding: utf-8

# In[1]:


manager = EmployeeManager()

while True:
    print_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        manager.add_employee()
    elif choice == '2':
        manager.list_employees()
    elif choice == '3':
        term = input("Enter name or department to search: ")
        manager.search_employee(term)
    elif choice == '4':
        order = input("Sort descending? (y/n): ").lower()
        manager.sort_by_salary(desc=(order == 'y'))
    elif choice == '5':
        manager.generate_report()
    elif choice == '6':
        manager.save_employees()
        print("✅ Data saved. Exiting...")
        break
    else:
        print("❌ Invalid choice. Please try again.")


# In[ ]:




