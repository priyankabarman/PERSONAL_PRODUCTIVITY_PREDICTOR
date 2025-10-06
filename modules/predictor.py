#modules / predictor.py


def predict_next_day(last_score, slope):
    """
    Predicts the next day's score using the last score and the trend slope.
    """
    if last_score is None or slope is None:
        return None, None

    predicted_score = last_score + slope
    # Ensure the predicted score stays within the valid range [0, 10]
    predicted_score = max(0, min(10, predicted_score))

    if last_score == 0:
        percent_change = 0.0
    else:
        percent_change = ((predicted_score - last_score) / last_score) * 100

    return predicted_score, percent_change
