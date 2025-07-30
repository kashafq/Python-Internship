#!/usr/bin/env python
# coding: utf-8

# In[1]:

import tkinter as tk
from tkinter import messagebox
import json
import os

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("400x500")
        self.tasks = []
        
        # Color scheme
        self.bg_color = "#f5f5f5"
        self.entry_bg = "#ffffff"
        self.button_bg = "#3f51b5"
        self.list_bg = "#ffffff"
        
        self.setup_ui()
        self.load_tasks()
    
    def setup_ui(self):
        # Main container
        self.main_frame = tk.Frame(self.root, bg=self.bg_color)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Task entry
        self.task_entry = tk.Entry(
            self.main_frame, 
            font=("Arial", 12), 
            bg=self.entry_bg,
            relief=tk.FLAT
        )
        self.task_entry.pack(fill=tk.X, pady=(0, 10))
        self.task_entry.bind("<Return>", lambda e: self.add_task())
        
        # Add button
        self.add_btn = tk.Button(
            self.main_frame,
            text="Add Task",
            command=self.add_task,
            bg=self.button_bg,
            fg="white",
            relief=tk.FLAT
        )
        self.add_btn.pack(fill=tk.X)
        
        # Task list
        self.task_list = tk.Listbox(
            self.main_frame,
            font=("Arial", 11),
            bg=self.list_bg,
            selectbackground="#e0e0e0",
            selectmode=tk.SINGLE,
            relief=tk.FLAT,
            height=15
        )
        self.task_list.pack(fill=tk.BOTH, expand=True, pady=(10, 5))
        
        # Button container
        btn_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        btn_frame.pack(fill=tk.X, pady=(5, 0))
        
        # Action buttons
        self.complete_btn = tk.Button(
            btn_frame,
            text="Complete",
            command=self.mark_complete,
            bg="#2196F3",
            fg="white",
            relief=tk.FLAT
        )
        self.complete_btn.pack(side=tk.LEFT, expand=True, fill=tk.X)
        
        self.delete_btn = tk.Button(
            btn_frame,
            text="Delete",
            command=self.delete_task,
            bg="#f44336",
            fg="white",
            relief=tk.FLAT
        )
        self.delete_btn.pack(side=tk.LEFT, expand=True, fill=tk.X)
        
        # Save/Load buttons
        self.save_btn = tk.Button(
            self.main_frame,
            text="Save Tasks",
            command=self.save_tasks,
            bg="#607D8B",
            fg="white",
            relief=tk.FLAT
        )
        self.save_btn.pack(fill=tk.X, pady=(5, 0))
        
        self.clear_btn = tk.Button(
            self.main_frame,
            text="Clear Completed",
            command=self.clear_completed,
            bg="#9E9E9E",
            fg="white",
            relief=tk.FLAT
        )
        self.clear_btn.pack(fill=tk.X, pady=(5, 0))
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"text": task, "completed": False})
            self.update_list()
            self.task_entry.delete(0, tk.END)
    
    def mark_complete(self):
        selected = self.task_list.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_list()
    
    def delete_task(self):
        selected = self.task_list.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_list()
    
    def clear_completed(self):
        self.tasks = [task for task in self.tasks if not task["completed"]]
        self.update_list()
    
    def update_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            prefix = "[✓] " if task["completed"] else "[ ] "
            self.task_list.insert(tk.END, prefix + task["text"])
            if task["completed"]:
                self.task_list.itemconfig(tk.END, {'fg': '#757575'})
    
    def save_tasks(self):
        try:
            with open("tasks.json", "w") as f:
                json.dump(self.tasks, f)
            messagebox.showinfo("Success", "Tasks saved successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save tasks: {str(e)}")
    
    def load_tasks(self):
        if os.path.exists("tasks.json"):
            try:
                with open("tasks.json", "r") as f:
                    self.tasks = json.load(f)
                self.update_list()
            except:
                self.tasks = []

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
