from data_loader import load_data


def basic_statistics():

    df = load_data()

    print("\n========== SENTINEL ANALYTICS ==========\n")

    print("Total Incidents :", len(df))

    print("\nIncidents by State")
    print(df["State"].value_counts())

    print("\nThreat Level")
    print(df["Threat_Level"].value_counts())

    print("\nIncident Types")
    print(df["Incident_Type"].value_counts())

    print("\nAverage Response Time")
    print(round(df["Response_Time_Min"].mean(), 2), "minutes")

    print("\nAverage Personnel Deployed")
    print(round(df["Personnel_Deployed"].mean(), 2))


if __name__ == "__main__":
    basic_statistics()