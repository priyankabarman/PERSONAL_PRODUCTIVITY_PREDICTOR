# modules/input_handler.py

def get_tasks():
    """
    Accepts user input for daily tasks and returns them as a list of dictionaries.
    """
    tasks = []
    while True:
        try:
            num_tasks_str = input("Enter the number of tasks for today: ")
            if not num_tasks_str: continue  # Handle empty input
            num_tasks = int(num_tasks_str)
            if num_tasks > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print("-" * 20)
    for i in range(num_tasks):
        print(f"--- Task {i + 1} ---")
        task_name = input("Enter task name: ")

        while True:
            try:
                hours = float(input(f"Enter hours spent on '{task_name}': "))
                if hours >= 0:
                    break
                else:
                    print("Hours cannot be negative.")
            except ValueError:
                print("Invalid input. Please enter a number for hours.")

        while True:
            try:
                weight = int(input(f"Enter importance weight for '{task_name}' (1-5): "))
                if 1 <= weight <= 5:
                    break
                else:
                    print("Weight must be between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a whole number between 1 and 5.")

        tasks.append({"name": task_name, "hours": hours, "weight": weight})
        print("-" * 20)

    return tasks
