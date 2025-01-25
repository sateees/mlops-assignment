import os
import pandas as pd
from sklearn.datasets import make_classification
import random

def generate_random_data(n_samples):
    """Generate random data matching the required schema."""
    data = {
        "id": [random.randint(100000, 200000) for _ in range(n_samples)],
        "Gender": random.choices(["Male", "Female"], k=n_samples),
        "Age": [random.randint(18, 70) for _ in range(n_samples)],
        "HasDrivingLicense": random.choices([0, 1], k=n_samples),
        "RegionID": [random.randint(1, 50) for _ in range(n_samples)],
        "Switch": random.choices([0, 1], k=n_samples),
        "VehicleAge": random.choices(["< 1 Year", "1-2 Years", "> 2 Years"], k=n_samples),
        "PastAccident": random.choices(["Yes", "No", ""], k=n_samples),
        "AnnualPremium": [f"£{random.uniform(1000, 2000):,.2f}" for _ in range(n_samples)],
        "SalesChannelID": [random.randint(100, 200) for _ in range(n_samples)],
        "DaysSinceCreated": [random.randint(100, 300) for _ in range(n_samples)],
    }
    return pd.DataFrame(data)

def extract_data():
    """Process classification data based on the presence of insurance_data.csv."""
    file_path = "data/insurance_data.csv"

    # Check if the insurance_data.csv file exists
    if os.path.exists(file_path):
        print(f"Loading data from {file_path}")
        df = pd.read_csv(file_path)
    else:
        print(f"{file_path} not found. Generating random data...")
        df = generate_random_data(10000)  # Generate data with 10,000 rows

    # Add classification target (Result) to the data
    X, y = make_classification(
        n_samples=len(df),
        n_features=10,
        n_informative=8,
        n_redundant=2,
        n_classes=2,
        random_state=42,
    )
    df["Result"] = y

    # Split into train and test datasets
    train_data = df.iloc[:int(0.8 * len(df))]
    test_data = df.iloc[int(0.8 * len(df)):]

    # Ensure the data directory exists
    if not os.path.exists("data"):
        os.mkdir("data")

    # Save train and test data
    train_data.to_csv("data/train.csv", index=False)
    test_data.to_csv("data/test.csv", index=False)

    print("Data extraction and processing completed successfully!")

if __name__ == "__main__":
    extract_data()
