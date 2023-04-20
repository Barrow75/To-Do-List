# To do list in python

# stores the tasks in a list
To_Do = []

# opens and reads the text file line by line that saves the items in the list
with open("To Do List.txt", "r") as f:
    for line in f:
        task = line.strip()
        if task:
            To_Do.append(task)
while True:
    command = input("Enter add or remove to add or remove a task from the list: ")
    # adds a task to the to do list in the text file
    if command == "add":
        task = input("Enter a task to add to the list: ")
        To_Do.append(task)
        print(f"{task} added to the list!")
        with open("To Do List.txt", "w") as f:
            for task in To_Do:
                f.write(task + '\n')
    # removes task in the list and file
    elif command == "remove":
        task = input("Enter the task you would like to remove: ")
        if task in To_Do:
            To_Do.remove(task)
            print(f"{task} is removed off the list!")
            with open("To Do List.txt", "w") as f:
                for task in To_Do:
                    f.write(task + '\n')

        elif task not in To_Do:
            print(f"{task} is not found in list")
    # exits the To Do List
    elif command == "exit":
        break

# prints out the list
print("To Do List:")
for task in To_Do:
    print(task)
