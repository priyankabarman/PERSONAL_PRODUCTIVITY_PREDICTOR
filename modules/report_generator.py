
# modules/report_generator.py

LOG_FILE = "data/productivity_log.txt"

def generate_report(date_str, tasks_with_scores, total_hours, productivity_score, trend_status, predicted_score, percent_change, optimization_tip):
    """
    Formats all calculated data into a single, readable string report.
    """
    report = [
        "--- Personal Productivity & Performance Predictor ---",
        f"Date: {date_str}",
        "-" * 55,
        f"{'Task':<20} {'Hours':>10} {'Weight':>10} {'Weighted Score':>15}",
        "-" * 55
    ]

    for task in tasks_with_scores:
        report.append(f"{task['name']:<20} {task['hours']:>10.1f} {task['weight']:>10} {task['weighted_score']:>15.1f}")
    
    report.extend([
        "-" * 55,
        f"Total Hours: {total_hours:.1f}",
        f"Productivity Score: {productivity_score:.1f} / 10.0",
        ""
    ])

    if trend_status:
        report.append(f"Trend: {trend_status}")
    if predicted_score is not None:
        sign = "+" if percent_change >= 0 else ""
        report.append(f"Predicted Next Day Score: {predicted_score:.1f} ({sign}{percent_change:.1f}%)")
    
    report.append(f"Optimization Tip: {optimization_tip}")
    
    return "\n".join(report)

def save_log(date_str, productivity_score, total_hours):
    """
    Appends the daily summary to the log file.
    """
    try:
        # The 'a' stands for append mode
        with open(LOG_FILE, "a") as f:
            f.write(f"{date_str},{productivity_score:.2f},{total_hours:.2f}\n")
        return f"\nReport saved to {LOG_FILE}"
    except IOError as e:
        return f"\nError: Could not save log file. {e}"

def read_log():
    """
    Reads the log file and returns a list of past productivity scores.
    """
    scores = []
    try:
        with open(LOG_FILE, "r") as f:
            for line in f:
                try:
                    # Line format: YYYY-MM-DD,score,total_hours
                    parts = line.strip().split(',')
                    scores.append(float(parts[1]))
                except (ValueError, IndexError):
                    continue # Skip malformed lines
    except FileNotFoundError:
        pass # It's okay if the file doesn't exist yet
    return scores

