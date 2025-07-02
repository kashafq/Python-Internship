#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#day 7
def analyze_numbers(numbers):
    sorted_list = numbers[:]
    for i in range(len(sorted_list)):
        for j in range(i + 1, len(sorted_list)):
            if sorted_list[i] > sorted_list[j]:
                sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]

    total = 0
    smallest = sorted_list[0]
    largest = sorted_list[0]

    for num in sorted_list:
        total += num
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    average = total / len(sorted_list)

    return {
        "sorted": sorted_list,
        "sum": total,
        "average": average,
        "min": smallest,
        "max": largest
    }

def print_dashboard(data):
    print("\nAnalysis Result:\n")
    for i, (key, value) in enumerate(data.items(), start=1):
        print(f"{i}. {key} → {value}")

user_list = []

count_input = input("How many numbers do you want to input? ")
if count_input.isdigit():
    count = int(count_input)
else:
    print("Please enter a valid whole number.")
    exit()

for i in range(count):
    num = input(f"Enter number {i+1}: ")
    if num.replace('.', '', 1).isdigit():
        user_list.append(float(num))
    else:
        print("Invalid input. Only numbers allowed.")
        exit()

results = analyze_numbers(user_list)
print_dashboard(results)

