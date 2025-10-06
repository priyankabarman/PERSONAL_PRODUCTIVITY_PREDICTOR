import productivity_calculator as calculator

calculator.py


def calculate_productivity(tasks):
    """
    Calculates the daily productivity score based on a time-weighted average of task importance.
    Returns the score (scaled to /10), total hours, and tasks with their individual scores.
    """
    if not tasks:
        return 0, 0, []

    total_hours = 0
    total_weighted_points = 0
    tasks_with_scores = []

    for task in tasks:
        total_hours += task["hours"]
        weighted_score = task["hours"] * task["weight"]
        total_weighted_points += weighted_score

        task_data = task.copy()
        task_data["weighted_score"] = weighted_score
        tasks_with_scores.append(task_data)

    if total_hours == 0:
        raw_score = 0
    else:
        # Calculate the weighted average of weights (result is on a 1-5 scale)
        raw_score = total_weighted_points / total_hours

    # Scale the score to be out of 10
    scaled_score = raw_score * 2

    return scaled_score, total_hours, tasks_with_scores

