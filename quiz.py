import streamlit as st

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

def check_answer(question, selected_option):
    return question["answer"] == selected_option

def quiz_section():
    st.header("Quiz: Test Your Knowledge")
    st.write("Answer the following questions about the Sudan conflict:")

    questions = load_questions()

    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
        st.session_state.score = 0

    current_question = st.session_state.current_question

    if current_question < len(questions):
        question = questions[current_question]
        st.write(f"### Question {current_question + 1}: {question['question']}")
        selected_option = st.radio(f"Select an option for question {current_question + 1}:", question["options"], key=f"q{current_question}")
        if st.button(f"Submit Answer for Question {current_question + 1}", key=f"submit{current_question}"):
            if check_answer(question, selected_option):
                st.success("Correct!")
                st.session_state.score += 1
            else:
                st.error(f"Incorrect. The correct answer is: {question['answer']}")
            
            st.session_state.current_question += 1
            st.experimental_rerun()
    else:
        st.write(f"Your final score is: {st.session_state.score} out of {len(questions)}")
        if st.button("Back to Menu"):
            del st.session_state.current_question
            del st.session_state.score
            st.session_state.page = "game_selection"
            st.experimental_rerun()
