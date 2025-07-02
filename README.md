# 🌾 Agriculture Cost & Yield Dashboard

An interactive web dashboard built using **Streamlit** to explore and visualize agriculture-related metrics such as crop yield, cost of cultivation, and production across different Indian states.

---

## 📌 Features

- 📤 Upload agriculture datasets in `.csv` format  
- 🌱 Filter by **Crop**
- 📊 Visualizations:
  - Yield by State (Bar chart)
  - Cost of Cultivation C2 (Bar chart)
  - Cost of Production vs Yield (Scatter plot)
- 📈 Summary statistics (mean, min, max, etc.)

---

## 🧠 Dataset Columns Explained

| Column Name                          | Description                                                  |
|--------------------------------------|--------------------------------------------------------------|
| `Crop`                               | Name of the crop (e.g., Rice, Wheat)                         |
| `State`                              | Indian state where crop is grown                             |
| `Season`                             | Season of cultivation (e.g., Kharif, Rabi)                   |
| `Year`                               | Year of cultivation                                          |
| `Yield (Quintal/ Hectare)`           | Yield per hectare                                            |
| `Cost of Cultivation (`/Hectare) C2` | Cost to cultivate 1 hectare (C2 method)                      |
| `Cost of Production (`/Quintal) C2`  | Cost to produce 1 quintal of crop                            |
| `Gross Value Output (`/Hectare)`     | Market value of output per hectare                           |

---

## 🚀 How to Run This Project

 ### 1. Clone the repository

    
    git clone https://github.com/your-username/agriculture-dashboard.git
    cd agriculture-dashboard

---

### 2. Install required Python libraries

Make sure Python and pip are installed, then run the following command to install the dependencies:

    
    pip install streamlit pandas matplotlib seaborn

 ### 3. Run the Streamlit app

After installing the dependencies, run the Streamlit app using the command below:

    python -m streamlit run agri_dashboard.py



## 📚 Learning Enhancements

This project helped strengthen the following skills:

- ✅ **Python for Data Analysis**: Hands-on experience with Pandas for filtering, grouping, and exploring real datasets.
- ✅ **Streamlit Framework**: Learned how to create a full-featured web dashboard using simple Python scripts.
- ✅ **Interactive UI Building**: Used dropdowns, file uploaders, and dynamic visualizations for user-driven analysis.
- ✅ **Data Visualization**: Used Matplotlib and Seaborn to build bar charts, scatter plots, and display trends.
- ✅ **Domain Knowledge in Agriculture**: Understood key agricultural metrics like Yield, Cost of Cultivation (C2), and Cost of Production.

---

## 🚀 Future Recommendations / Improvements

- 📅 Add **Year and Season Filters**
- 📍 Use **Map Visualizations** to show data state-wise
- 📤 Allow **Export of Filtered Data** as CSV
- 🌽 Compare **Multiple Crops Side-by-Side**
- 📈 Include **Profitability or ROI Calculations**
- ☁️ Deploy online via **Streamlit Cloud** or **HuggingFace Spaces**
- 🤖 Add **Machine Learning Models** for yield prediction or crop classification




