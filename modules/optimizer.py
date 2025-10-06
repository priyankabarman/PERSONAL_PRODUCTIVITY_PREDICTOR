
def get_optimization_suggestion(tasks, total_hours):
    """
    Analyzes tasks to find an inefficient time allocation and suggests an improvement.
    """
    if len(tasks) < 2 or total_hours == 0:
        return "Not enough data for an optimization tip."

    # Find the task with the lowest weight that has substantial time spent on it
    low_priority_task = None
    max_hours_on_low_priority = 0.5 # Must spend at least 30 mins
    for task in tasks:
        if task['weight'] <= 2 and task['hours'] > max_hours_on_low_priority:
            max_hours_on_low_priority = task['hours']
            low_priority_task = task

    # Find a task with high weight
    high_priority_task = None
    for task in tasks:
        if task['weight'] >= 4:
            high_priority_task = task
            break

    if low_priority_task and high_priority_task:
        time_to_move = 0.5 # Suggest moving 30 minutes
        
        # Calculate the potential score gain
        # Gain is based on the change in weighted points, divided by total hours, and scaled to /10
        gain = (time_to_move * (high_priority_task['weight'] - low_priority_task['weight'])) / total_hours * 2
        
        return (f"Reduce '{low_priority_task['name']}' by 30 minutes and reallocate to "
                f"'{high_priority_task['name']}' for a potential gain of +{gain:.1f} points.")
        
    return "Your time allocation seems balanced."

