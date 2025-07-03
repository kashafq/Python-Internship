#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Day 8 
print('---< Dynamic Contact Book >---\n')

contacts = {}

def add_contact():
    name = input("\n-- Enter the name of the contact you want to add: ").title()
    if name in contacts:
        print("! Contact already exists!")
        return

    phone = input("-- Enter the phone number of the contact: ")
    
    # Email validation loop
    while True:
        email = input("-- Enter the email of the contact: ")
        if '@' in email and '.' in email:
            break
        else:
            print("! Invalid email! Please include '@' and '.'")

    contacts[name] = {
        'phone': phone,
        'email': email
    }
    print(f"✦ Contact for {name} added successfully.\n")


def update_contact():
    name = input("Enter the name of the contact you want to update: ").title()
    if name not in contacts:
        print("Contact not found!")
        return

    print(f"\nCurrent Info - Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
    phone = input("Enter new phone number (or press Enter to keep current): ")
    email = input("Enter new email (or press Enter to keep current): ")

    if phone.strip():
        contacts[name]['phone'] = phone

    if email.strip():
        while True:
            if '@' in email and '.' in email:
                contacts[name]['email'] = email
                break
            else:
                print("Invalid email! Please include '@' and '.'")
                email = input("Enter a valid email: ")

    print(f"✦ Contact for {name} updated successfully.\n")


def retrieve_contact():
    name = input("Enter the name of the contact you want to retrieve: ").title()
    if name in contacts:
        info = contacts[name]
        print(f"\nName: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print("-" * 20,'\n')
    else:
        print("Contact not found!\n")


def display_contacts():
    if not contacts:
        print("There are no contacts.\n")
    else:
        print("\n--- Contact List ---\n")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print("-" * 20)
        print()


def display_menu():
    while True:
        print("\t--< MENU >--\n 1. Add Contact\n 2. Update Contact\n 3. Retrieve Contact\n 4. View All Contacts\n 5. Exit")
        choice = input("\nEnter your choice (1–5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            update_contact()
        elif choice == '3':
            retrieve_contact()
        elif choice == '4':
            display_contacts()
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid option! Please choose a number between 1 and 5.\n")


# Run the menu
display_menu()


# In[ ]:




