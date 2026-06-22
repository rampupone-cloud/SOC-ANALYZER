import streamlit as st
from analyzer import analyze_logs

st.set_page_config(page_title="AI SOC Analyzer")

st.title("🔐 AI SOC Log Analyzer")

uploaded_file = st.file_uploader("Upload log file")

if uploaded_file:
    try:
        logs = uploaded_file.read().decode("utf-8")

        st.subheader("📂 Raw Logs")
        st.text(logs)

        if st.button("Analyze Logs"):
            result = analyze_logs(logs)

            st.subheader("🚨 Analysis Report")
            st.write(result)

    except Exception as e:
        st.error(f"Error occurred: {e}")