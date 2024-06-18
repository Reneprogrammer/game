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

def quiz_section():
    st.header("Quiz: Test Your Knowledge")
    st.write("Answer the following questions about the Sudan conflict:")

    questions = load_questions()
    score = 0

    for i, question in enumerate(questions):
        st.write(f"### Question {i + 1}: {question['question']}")
        selected_option = st.radio("Select an option:", question["options"], key=f"q{i}")
        if st.button(f"Submit Answer for Question {i + 1}", key=f"submit{i}"):
            if check_answer(question, selected_option):
                st.success("Correct!")
                score += 1
            else:
                st.error(f"Incorrect. The correct answer is: {question['answer']}")

    if st.button("Show Final Score"):
        st.write(f"Your final score is: {score} out of {len(questions)}")

# Function to display the current story part and options
def display_story_part(story_part):
    st.write(story_part["text"])
    for option in story_part["options"]:
        if st.button(option["label"], key=option["next_part"]):
            return option["next_part"]
    return story_part["id"]

# Function to load the story parts
def load_story():
    return {
        "start": {
            "id": "start",
            "text": "You are a journalist covering the Sudan conflict. You have the opportunity to interview key figures. Who do you interview first?",
            "options": [
                {"label": "Government official", "next_part": "gov_official"},
                {"label": "Rebel leader", "next_part": "rebel_leader"},
                {"label": "Civilian", "next_part": "civilian"}
            ]
        },
        "gov_official": {
            "id": "gov_official",
            "text": "The government official explains their stance on the conflict, emphasizing the need for national unity. Do you...",
            "options": [
                {"label": "Ask about human rights abuses", "next_part": "hr_abuses"},
                {"label": "Inquire about economic policies", "next_part": "econ_policies"}
            ]
        },
        "rebel_leader": {
            "id": "rebel_leader",
            "text": "The rebel leader discusses their fight against oppression. Do you...",
            "options": [
                {"label": "Ask about their demands", "next_part": "rebel_demands"},
                {"label": "Inquire about their tactics", "next_part": "rebel_tactics"}
            ]
        },
        "civilian": {
            "id": "civilian",
            "text": "The civilian shares their experiences living through the conflict. Do you...",
            "options": [
                {"label": "Ask about daily challenges", "next_part": "daily_challenges"},
                {"label": "Inquire about their hopes for the future", "next_part": "future_hopes"}
            ]
        },
        # Add more parts as needed
        "hr_abuses": {
            "id": "hr_abuses",
            "text": "The official denies any human rights abuses, claiming they are propaganda. Do you...",
            "options": [
                {"label": "Challenge their claim", "next_part": "challenge_claim"},
                {"label": "Move to another topic", "next_part": "gov_official"}
            ]
        },
        "econ_policies": {
            "id": "econ_policies",
            "text": "The official outlines their economic policies aimed at stabilizing the country. Do you...",
            "options": [
                {"label": "Ask about foreign aid", "next_part": "foreign_aid"},
                {"label": "Inquire about infrastructure projects", "next_part": "infrastructure"}
            ]
        },
        # Continue to build out the story
    }

def story_section():
    st.header("Interactive Story: Experience the Sudan Conflict")
    st.write("Make choices to navigate through the story and learn about the Sudan conflict.")

    story = load_story()
    current_part_id = "start"

    while current_part_id:
        story_part = story[current_part_id]
        current_part_id = display_story_part(story_part)

def main():
    st.title("Learn About the Sudan Conflict")
    st.sidebar.title("Navigation")
    options = st.sidebar.radio("Go to", ["Quiz", "Interactive Story"])

    if options == "Quiz":
        quiz_section()
    elif options == "Interactive Story":
        story_section()

if __name__ == "__main__":
    main()

