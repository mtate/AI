import pandas as pd


def predict_failure(model, training_columns, machine_type, air_temperature, process_temperature,
                    rotational_speed, torque, tool_wear):
    """Create a feature row matching the training columns and return a prediction summary."""
    if machine_type not in {"L", "M", "H"}:
        raise ValueError("machine_type must be one of 'L', 'M', or 'H'.")

    feature_row = {
        "Air temperature": air_temperature,
        "Process temperature": process_temperature,
        "Rotational speed": rotational_speed,
        "Torque": torque,
        "Tool wear": tool_wear,
    }

    for column in training_columns:
        if column == "Type_L":
            feature_row[column] = 1 if machine_type == "L" else 0
        elif column == "Type_M":
            feature_row[column] = 1 if machine_type == "M" else 0
        elif column == "Type_H":
            feature_row[column] = 1 if machine_type == "H" else 0

    feature_df = pd.DataFrame([feature_row], columns=training_columns)

    probability = model.predict_proba(feature_df)[0, 1]
    prediction = int(model.predict(feature_df)[0])

    if probability >= 0.70:
        risk_tier = "HIGH"
    elif probability >= 0.40:
        risk_tier = "MEDIUM"
    else:
        risk_tier = "LOW"

    return prediction, probability, risk_tier
