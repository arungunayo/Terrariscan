import streamlit as st

def show_overview():
    st.subheader("Terrascansi Overview")
    st.write(
        """
        Vision
            Build a system that uses satellite imagery + AI to:
               1.  Detect existing green spaces
               2. Track how they change over time
               3. Actively suggest where new green spaces should be created to maximize environmental impact
        """
)