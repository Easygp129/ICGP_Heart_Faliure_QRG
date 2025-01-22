import streamlit as st

def main():
    st.title("Heart Failure Assessment Tool")
    st.write("Answer the following questions to assess your condition and receive personalized recommendations.")

    user_responses = {}

    with st.form("heart_failure_form"):
        st.subheader("Symptoms")
        user_responses["breathlessness"] = st.radio(
            "Do you experience breathlessness, especially during physical activity or while lying flat?",
            ["Yes", "No"],
        )
        user_responses["swelling"] = st.radio(
            "Have you noticed any swelling in your ankles or feet?", ["Yes", "No"]
        )
        user_responses["fatigue"] = st.radio(
            "Do you feel unusually fatigued, even after minimal effort?", ["Yes", "No"]
        )

        st.subheader("Medical History")
        user_responses["ischemic_history"] = st.radio(
            "Do you have a history of ischemic heart disease or high blood pressure?", ["Yes", "No"]
        )
        user_responses["diuretics"] = st.radio(
            "Are you currently taking diuretics?", ["Yes", "No"]
        )
        user_responses["diabetes"] = st.radio(
            "Have you been diagnosed with diabetes?", ["Yes", "No"]
        )

        st.subheader("Physical Examination")
        user_responses["weight_gain"] = st.radio(
            "Have you experienced rapid weight gain (e.g., 2 kg in 3 days)?", ["Yes", "No"]
        )
        user_responses["palpitations"] = st.radio(
            "Have you experienced dizziness, palpitations, or fainting spells?", ["Yes", "No"]
        )
        user_responses["persistent_cough"] = st.radio(
            "Do you have persistent coughing or wheezing?", ["Yes", "No"]
        )

        submitted = st.form_submit_button("Submit")

    if submitted:
        st.subheader("Results")
        results = []

        if user_responses["breathlessness"] == "Yes" and user_responses["swelling"] == "Yes" and user_responses["fatigue"] == "Yes":
            results.append("You may have symptoms suggestive of heart failure. Please consult a healthcare provider.")

        if user_responses["ischemic_history"] == "Yes" or user_responses["diabetes"] == "Yes":
            results.append("Your medical history indicates risk factors for heart failure. Regular monitoring is advised.")

        if user_responses["weight_gain"] == "Yes" or user_responses["palpitations"] == "Yes" or user_responses["persistent_cough"] == "Yes":
            results.append("Physical signs suggest potential heart failure. Further diagnostic tests, such as an echocardiogram, may be required.")

        if not results:
            st.write("Your responses do not strongly indicate heart failure. However, consult a healthcare provider if symptoms persist or worsen.")
        else:
            for result in results:
                st.write(f"- {result}")

if __name__ == "__main__":
    main()

