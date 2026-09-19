import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Page configuration
st.set_page_config(
    page_title="SENTINEL Defence Analytics",
    layout="wide"
)


# Load dataset
@st.cache_data
def load_data():

# Sidebar
st.sidebar.title("🛡️ SENTINEL")

page = st.sidebar.selectbox(
    "Navigation",
    [
        "Dashboard",
        "Incident Data"
    ]
)
    df = pd.read_csv(
        "data/defence_incidents.csv"
    )

    return df


df = load_data()


# Title
if page == "Dashboard":

    st.title("🛡️ SENTINEL Defence Analytics Dashboard")
st.write(
    "Strategic Event & National Threat Intelligence Evaluation Log"
)


# KPI Section

col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        "Total Incidents",
        len(df)
    )


with col2:
    st.metric(
        "Average Response Time",
        f"{round(df['Response_Time_Min'].mean(),2)} min"
    )


with col3:
    st.metric(
        "High Threat Incidents",
        len(
            df[df["Threat_Level"]=="High"]
        )
    )

st.divider()
# ===============================
# Charts Section
# ===============================

st.subheader("📊 Incident Analytics")


col1, col2 = st.columns(2)


# State Chart
with col1:

    state_counts = df["State"].value_counts()

    fig, ax = plt.subplots(figsize=(6,4))

    ax.bar(
        state_counts.index,
        state_counts.values
    )

    ax.set_title("Incidents by State")

    ax.set_ylabel("Incidents")

    plt.xticks(rotation=45)

    st.pyplot(fig)



# Threat Chart
with col2:

    threat_counts = df["Threat_Level"].value_counts()

    fig, ax = plt.subplots(figsize=(6,4))

    ax.pie(
        threat_counts.values,
        labels=threat_counts.index,
        autopct="%1.1f%%"
    )

    ax.set_title("Threat Distribution")

    st.pyplot(fig)
    # ===============================
# Equipment Analysis
# ===============================

st.subheader("📡 Equipment Usage Analysis")


equipment_counts = df["Equipment_Used"].value_counts()


fig, ax = plt.subplots(figsize=(8,4))


ax.bar(
    equipment_counts.index,
    equipment_counts.values
)


ax.set_title("Equipment Used in Incidents")

ax.set_xlabel("Equipment")

ax.set_ylabel("Count")


plt.xticks(rotation=30)


st.pyplot(fig)
# Divider
st.divider()


# Filters

st.subheader("🔍 Incident Filters")


selected_state = st.selectbox(
    "Select State",
    ["All"] + list(df["State"].unique())
)


if selected_state != "All":

    filtered_df = df[
        df["State"] == selected_state
    ]

else:

    filtered_df = df


# Display table

st.subheader("📋 Incident Records")

st.dataframe(
    filtered_df,
    use_container_width=True
)
# ===============================
# Download Data
# ===============================

st.subheader("📥 Export Data")


csv = filtered_df.to_csv(index=False)


st.download_button(
    label="Download Filtered Dataset",
    data=csv,
    file_name="filtered_defence_incidents.csv",
    mime="text/csv"
)if page == "Incident Data":

    st.title("📋 Defence Incident Database")

    st.dataframe(
        df,
        use_container_width=True
    )