app.py
import streamlit as st

st.set_page_config(page_title="AI Risk Radar", page_icon="⚖️")

st.title("⚖️ AI Compliance & Risk Radar")
st.write("Determine your project's risk category under the **2026 EU AI Act**.")

# User Input
use_case = st.text_input("Enter your AI Use Case (e.g., 'Hiring tool', 'Social Scoring', 'Chatbot')")

if use_case:
    # Logic for Risk Categorization
    risk_level = "Minimal"
    color = "green"
    explanation = "This use case likely falls under minimal risk with no specific transparency obligations."

    # Identify High Risk
    high_risk_keywords = ["hiring", "credit", "education", "law enforcement", "biometric"]
    unacceptable_keywords = ["social scoring", "behavioral manipulation", "real-time biometric"]

    if any(word in use_case.lower() for word in unacceptable_keywords):
        risk_level = "UNACCEPTABLE"
        color = "red"
        explanation = "PROHIBITED: This use case is banned under Article 5 of the EU AI Act."
    elif any(word in use_case.lower() for word in high_risk_keywords):
        risk_level = "HIGH"
        color = "orange"
        explanation = "HIGH RISK: Requires strict conformity assessments, human oversight, and logging (Article 6)."
    elif "chatbot" in use_case.lower() or "generative" in use_case.lower():
        risk_level = "LIMITED"
        color = "blue"
        explanation = "LIMITED RISK: Transparency obligations apply. Users must know they are interacting with AI."

    # Display Result
    st.subheader(f"Risk Assessment: :{color}[{risk_level}]")
    st.info(explanation)

st.divider()
st.caption("Developed by Daniel Barr | 2026 AI Governance Portfolio")
