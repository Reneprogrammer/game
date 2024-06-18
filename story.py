import streamlit as st

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
        # Add more story parts here
    }

def display_story_part(story, current_part_id):
    story_part = story[current_part_id]
    st.write(story_part["text"])
    for option in story_part["options"]:
        if st.button(option["label"], key=f"{current_part_id}_{option['next_part']}"):
            st.session_state.current_part_id = option["next_part"]
            st.experimental_rerun()

def story_section():
    st.header("Interactive Story: Experience the Sudan Conflict")
    st.write("Make choices to navigate through the story and learn about the Sudan conflict.")

    story = load_story()
    if 'current_part_id' not in st.session_state:
        st.session_state.current_part_id = "start"

    display_story_part(story, st.session_state.current_part_id)

    if st.button("Back to Menu"):
        del st.session_state.current_part_id
        st.session_state.page = "game_selection"
        st.experimental_rerun()
