import streamlit as st
import pandas as pd

st.set_page_config(page_title="Engineering Dashboard", layout="wide")

# Load data
students = pd.read_csv("students.csv")
results = pd.read_csv("results.csv")
units = pd.read_csv("delivery_units.csv")

st.title("🎓 Engineering Student Dashboard")

# Sidebar filters
unit_code = st.sidebar.selectbox("Select Unit", sorted(units["UNIT_CODE"].unique()))
student_id = st.sidebar.text_input("Enter Student ID (optional)")

# Class-level data
st.subheader(f"📊 Class Results for Unit: {unit_code}")
filtered_class = results[results["UNIT_CODE"] == unit_code]
st.dataframe(filtered_class)

# Individual student result
if student_id:
    student_results = results[results["STUDENT_ID"].astype(str) == student_id]
    st.subheader(f"🎯 Results for Student ID: {student_id}")
    if not student_results.empty:
        st.dataframe(student_results)
    else:
        st.warning("No data found for this student.")

# Download
st.download_button("📥 Download Unit Results", filtered_class.to_csv(index=False), file_name=f"{unit_code}_results.csv")
