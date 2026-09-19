import os
import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_data


def create_state_bar_chart():

    df = load_data()

    state_counts = df["State"].value_counts()

    plt.figure(figsize=(8, 5))

    plt.bar(state_counts.index, state_counts.values)

    plt.title("Incidents by State")
    plt.xlabel("State")
    plt.ylabel("Number of Incidents")

    plt.xticks(rotation=20)

    plt.tight_layout()

    plt.savefig("images/state_analysis.png")

    plt.close()

    print("✅ Bar chart saved successfully!")


def create_monthly_trend_chart():

    df = load_data()

    # Convert Date column
    df["Date"] = pd.to_datetime(df["Date"])

    # Create month column
    df["Month"] = df["Date"].dt.to_period("M")

    # Count incidents per month
    monthly_counts = df["Month"].value_counts().sort_index()

    plt.figure(figsize=(10, 5))

    plt.plot(
        monthly_counts.index.astype(str),
        monthly_counts.values,
        marker="o"
    )

    plt.title("Monthly Defence Incident Trend")
    plt.xlabel("Month")
    plt.ylabel("Number of Incidents")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("images/monthly_trend.png")

    plt.close()

    print("✅ Monthly trend chart saved!")
def create_threat_pie_chart():

    df = load_data()

    threat_counts = df["Threat_Level"].value_counts()

    plt.figure(figsize=(7, 7))

    plt.pie(
        threat_counts.values,
        labels=threat_counts.index,
        autopct="%1.1f%%"
    )

    plt.title("Threat Level Distribution")

    plt.tight_layout()

    plt.savefig("images/threat_distribution.png")

    plt.close()

    print("✅ Threat pie chart saved!")
def create_response_time_histogram():

    df = load_data()

    plt.figure(figsize=(8, 5))

    plt.hist(
        df["Response_Time_Min"],
        bins=10
    )

    plt.title("Response Time Distribution")

    plt.xlabel("Response Time (Minutes)")

    plt.ylabel("Number of Incidents")

    plt.tight_layout()

    plt.savefig("images/response_time_distribution.png")

    plt.close()

    print("✅ Response time histogram saved!")
if __name__ == "__main__":

    create_state_bar_chart()

    create_monthly_trend_chart()

    create_threat_pie_chart()

    create_response_time_histogram()