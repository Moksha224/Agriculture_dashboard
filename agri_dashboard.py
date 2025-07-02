import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Agri Dashboard", layout="wide")
st.title("Agriculture Cost & Yield Dashboard")

# File upload
uploaded_file = st.file_uploader("Upload your agriculture dataset (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip()  # Clean any extra spaces

    st.subheader("📄 Raw Data")
    st.dataframe(df)

    # Show crop selector
    crops = df["Crop"].unique()
    selected_crop = st.selectbox("Select Crop", crops)

    crop_df = df[df["Crop"] == selected_crop]

    # Yield by State
    st.subheader(f"📊 Yield by State for {selected_crop}")
    fig1, ax1 = plt.subplots()
    sns.barplot(data=crop_df, x="State", y="Yield (Quintal/ Hectare)", ax=ax1)
    plt.xticks(rotation=45)
    st.pyplot(fig1)

    # Cost of Cultivation C2
    st.subheader(f"💰 Cost of Cultivation (C2) in Each State")
    fig2, ax2 = plt.subplots()
    sns.barplot(data=crop_df, x="State", y="Cost of Cultivation (`/Hectare) C2", ax=ax2)
    plt.xticks(rotation=45)
    st.pyplot(fig2)

    # Scatter: Cost vs Yield
    st.subheader("📍 Cost of Production vs Yield")
    fig3, ax3 = plt.subplots()
    sns.scatterplot(
        data=crop_df,
        x="Cost of Production (`/Quintal) C2",
        y="Yield (Quintal/ Hectare)",
        hue="State",
        s=100,
        ax=ax3
    )
    st.pyplot(fig3)

    # Summary statistics
    st.subheader("📈 Summary Statistics")
    st.write(crop_df.describe())
