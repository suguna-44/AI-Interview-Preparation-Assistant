import streamlit as st

st.set_page_config(page_title="AI Interview Preparation Assistant")

st.title("🤖 AI Interview Preparation Assistant")

role = st.selectbox(
    "Select Job Role",
    ["QA Tester", "Java Developer", "Python Developer", "Data Analyst"]
)

questions = {
    "QA Tester": [
        "What is Software Testing?",
        "What is Manual Testing?",
        "What is Automation Testing?",
        "What is Selenium?",
        "What is Regression Testing?"
    ],
    "Java Developer": [
        "What is OOP?",
        "What is Inheritance?",
        "What is Polymorphism?",
        "What is Exception Handling?",
        "What is Multithreading?"
    ],
    "Python Developer": [
        "What is Python?",
        "What is a List?",
        "What is a Dictionary?",
        "What is OOP in Python?",
        "What are Modules?"
    ],
    "Data Analyst": [
        "What is Data Analysis?",
        "What is SQL?",
        "What is Pandas?",
        "What is Data Cleaning?",
        "What is Data Visualization?"
    ]
}

if st.button("Generate Questions"):
    st.subheader("Interview Questions")
    for q in questions[role]:
        st.write("✅", q)

st.markdown("---")

st.subheader("Answer Evaluation")

question = st.text_input("Enter Question")
answer = st.text_area("Enter Your Answer")

if st.button("Evaluate Answer"):

    length = len(answer)

    if length < 30:
        score = 3
        strengths = "Basic answer provided"
        weaknesses = "Answer is too short"
        suggestion = "Add definition, explanation and example."

    elif length < 80:
        score = 6
        strengths = "Good start"
        weaknesses = "Needs more details"
        suggestion = "Add examples and key points."

    else:
        score = 9
        strengths = "Well explained answer"
        weaknesses = "Minor improvements possible"
        suggestion = "Add real-world examples."

    st.success("Evaluation Completed")

    st.subheader("AI Evaluation Report")
    st.write(f"⭐ Score: {score}/10")
    st.write("### Strengths")
    st.write(strengths)
    st.write("### Weaknesses")
    st.write(weaknesses)
    st.write("### Suggested Improvement")
    st.write(suggestion)

st.markdown("---")
st.caption("Developed using Python & Streamlit")