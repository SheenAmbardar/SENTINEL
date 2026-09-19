import pandas as pd


def load_data():
    """
    Load the defence incidents dataset.
    """

    df = pd.read_csv("data/defence_incidents.csv")

    return df


if __name__ == "__main__":

    data = load_data()

    print("Dataset Loaded Successfully!\n")

    print(data.head())