import pandas as pd
import random
from datetime import datetime, timedelta

states = [
    "Jammu & Kashmir",
    "Punjab",
    "Rajasthan",
    "Gujarat",
    "Arunachal Pradesh"
]

sectors = [
    "Alpha",
    "Bravo",
    "Charlie",
    "Delta",
    "Echo"
]

incident_types = [
    "Drone Activity",
    "Infiltration",
    "Smuggling",
    "Ceasefire Violation",
    "Cyber Threat"
]

threat_levels = [
    "Low",
    "Medium",
    "High"
]

equipment = [
    "Radar",
    "Drone",
    "Thermal Camera",
    "Night Vision",
    "UAV"
]

status = [
    "Resolved",
    "Monitoring",
    "Under Investigation"
]


def generate_random_date():
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2025, 12, 31)

    days = (end_date - start_date).days
    random_days = random.randint(0, days)

    return start_date + timedelta(days=random_days)


def generate_incident(incident_number):

    incident = {
        "Incident_ID": f"INC{incident_number:05d}",
        "Date": generate_random_date().strftime("%Y-%m-%d"),
        "State": random.choices(
            states,
            weights=[40, 20, 15, 15, 10],
            k=1
        )[0],
        "Sector": random.choice(sectors),
        "Incident_Type": random.choices(
            incident_types,
            weights=[25, 35, 15, 20, 5],
            k=1
        )[0],
        "Threat_Level": random.choices(
            threat_levels,
            weights=[20, 35, 45],
            k=1
        )[0],
        "Personnel_Deployed": random.randint(10, 60),
        "Equipment_Used": random.choice(equipment),
        "Response_Time_Min": random.randint(5, 60),
        "Status": random.choice(status)
    }

    return incident
# Create an empty list
incident_list = []

# Generate 1000 incidents
for i in range(1, 1001):
    incident = generate_incident(i)
    incident_list.append(incident)

# Convert list into DataFrame
df = pd.DataFrame(incident_list)

# Save dataset
df.to_csv("data/defence_incidents.csv", index=False)

print("✅ Dataset created successfully!")
print(df.head())