# main.py
import os
from datetime import datetime

from .modules.input_handler import get_tasks
from .modules.productivity_calculator import calculator_productivity
from .modules.trend_analyzer import analyze_trend
from .modules.predictor import predict_next_day
from .modules.optimizer import get_optimization_suggestion
from .modules.report_generator import generate_report, save_log, read_log


def ensure_data_directory():
    """Checks if the data directory exists and creates it if not."""
    if not os.path.exists('data'):
        os.makedirs('data')


def main():
    """Main function to run the productivity predictor application."""
    print("=" * 55)
    print("Welcome to your Personal Productivity & Performance Predictor!")
    print("=" * 55)

    ensure_data_directory()

    # --- Part 1: Input & Core Calculation ---
    tasks = get_tasks()
    score, total_hours, tasks_with_scores = calculator_productivity(tasks)

    # --- Part 2: Analysis & Prediction ---
    past_scores = read_log()

    # Analyze trend using scores from previous days
    _, _, slope, trend_status = analyze_trend(past_scores)

    # Predict based on today's score and the historical trend
    predicted_score, percent_change = predict_next_day(score, slope)

    optimization_tip = get_optimization_suggestion(tasks, total_hours)

    # --- Part 3: Reporting ---
    today_str = datetime.now().strftime("%Y-%m-%d")
    final_report = generate_report(
        today_str,
        tasks_with_scores,
        total_hours,
        score,
        trend_status,
        predicted_score,
        percent_change,
        optimization_tip
    )

    print("\n" + "=" * 55)
    print("               YOUR DAILY REPORT")
    print("=" * 55)
    print(final_report)

    save_message = save_log(today_str, score, total_hours)
    print(save_message)
    print("=" * 55)


if __name__ == "__main__":
    main()

