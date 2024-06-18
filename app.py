import streamlit as st

# Function to load questions and answers
def load_questions():
    return [
        {
            "question": "What is the Sudan conflict primarily about?",
            "options": [
                "Religious differences",
                "Economic resources",
                "Political power struggle",
                "Border disputes"
            ],
            "answer": "Political power struggle"
        },
        {
            "question": "When did the recent conflict in Sudan begin?",
            "options": [
                "2011",
                "2013",
                "2019",
                "2021"
            ],
            "answer": "2019"
        },
        {
            "question": "Which two groups are primarily involved in the Sudan conflict?",
            "options": [
                "The Sudanese Armed Forces and the Rapid Support Forces",
                "The Government of Sudan and the South Sudan Liberation Movement",
                "The Janjaweed militia and the Sudan People's Liberation Army",
                "The Darfur rebels and the Sudanese government"
            ],
            "answer": "The Sudanese Armed Forces and the Rapid Support Forces"
        },
        {
            "question": "What is one of the major humanitarian impacts of the Sudan conflict?",
            "options": [
                "Massive displacement of people",
                "Economic prosperity",
                "Increased tourism",
                "Technological advancements"
            ],
            "answer": "Massive displacement of people"
        },
        {
            "question": "Which international organization has been actively involved in peacekeeping in Sudan?",
            "options": [
                "NATO",
                "UNAMID (United Nations-African Union Mission in Darfur)",
                "ASEAN",
                "OPEC"
            ],
            "answer": "UNAMID (United Nations-African Union Mission in Darfur)"
        }
    ]

# Function to check the answer
def check_answer(question, selected_option):
    return question["answer"] == selected_option

def main():
    st.title("Learn About the Sudan Conflict")
    st.write("Test your knowledge about the Sudan conflict by answering the following questions:")

    questions = load_questions()
    score = 0

    for i, question in enumerate(questions):
        st.write(f"### Question {i + 1}: {question['question']}")
        selected_option = st.radio("", question["options"], key=f"q{i}")
        if st.button(f"Submit Answer for Question {i + 1}", key=f"submit{i}"):
            if check_answer(question, selected_option):
                st.success("Correct!")
                score += 1
            else:
                st.error(f"Incorrect. The correct answer is: {question['answer']}")

    if st.button("Show Final Score"):
        st.write(f"Your final score is: {score} out of {len(questions)}")

if __name__ == "__main__":
    main()
