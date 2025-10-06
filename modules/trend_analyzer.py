# modules/trend_analyzer.py
import math


def analyze_trend(daily_scores):
    """
    Analyzes a list of past scores to find the mean, standard deviation, and trend slope.
    """
    n = len(daily_scores)
    if n < 2:
        return None, None, None, "Not enough data for trend analysis."

    # Mean
    mean = sum(daily_scores) / n

    # Standard Deviation
    variance = sum([(score - mean) ** 2 for score in daily_scores]) / n
    std_dev = math.sqrt(variance)

    # Simple Linear Regression Slope
    x = list(range(1, n + 1))
    y = daily_scores

    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum([xi * yi for xi, yi in zip(x, y)])
    sum_x_sq = sum([xi ** 2 for xi in x])

    numerator = n * sum_xy - sum_x * sum_y
    denominator = n * sum_x_sq - sum_x ** 2

    slope = 0 if denominator == 0 else numerator / denominator

    # Determine trend status
    if slope > 0.1:
        trend_status = "Improving 📈"
    elif slope < -0.1:
        trend_status = "Declining 📉"
    else:
        trend_status = "Stable 📊"

    return mean, std_dev, slope, trend_status

