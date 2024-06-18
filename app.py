import streamlit as st
import random

# Importing the different sections of the app
from quiz import quiz_section
from story import story_section
from timeline import timeline_puzzle
from rpg import rpg_game

# List of background images
background_images = [
    "https://raw.githubusercontent.com/yourusername/yourrepository/main/image1.jpg",
    "https://raw.githubusercontent.com/yourusername/yourrepository/main/image2.jpg",
    "https://raw.githubusercontent.com/yourusername/yourrepository/main/image3.jpg",
    "https://raw.githubusercontent.com/yourusername/yourrepository/main/image4.jpg",
    "https://raw.githubusercontent.com/yourusername/yourrepository/main/image5.jpg"
]

# Function to set the background image
def set_background_image():
    page_index = {
        "main_menu": 0,
        "game_selection": 1,
        "quiz": 2,
        "interactive_story": 3,
        "timeline_puzzle": 4,
        "rpg_game": 5
    }.get(st.session_state.page, 0)
    
    bg_image = background_images[page_index % len(background_images)]
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("{bg_image}") no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    if 'page' not in st.session_state:
        st.session_state.page = "main_menu"
        st.session_state.progress = {"Quiz": False, "Interactive Story": False, "Timeline Puzzle": False, "RPG Game": False}

    set_background_image()  # Ensure background image is set whenever the page is changed

    if st.session_state.page == "main_menu":
        st.title("Sudan Conflict")
        if st.button("Play"):
            st.session_state.page = "game_selection"
            st.experimental_rerun()

    elif st.session_state.page == "game_selection":
        st.title("Select a Game")
        st.write("Choose one of the following games to learn more about the Sudan conflict.")
        
        if st.button("Quiz"):
            st.session_state.page = "quiz"
            st.experimental_rerun()

        if st.button("Interactive Story"):
            st.session_state.page = "interactive_story"
            st.experimental_rerun()

        if st.button("Timeline Puzzle"):
            st.session_state.page = "timeline_puzzle"
            st.experimental_rerun()

        if st.button("RPG Game"):
            st.session_state.page = "rpg_game"
            st.experimental_rerun()

        st.write("### Progress")
        total_games = len(st.session_state.progress)
        completed_games = sum(st.session_state.progress.values())
        st.progress(completed_games / total_games)

    elif st.session_state.page == "quiz":
        quiz_section()
        st.session_state.progress["Quiz"] = True

    elif st.session_state.page == "interactive_story":
        story_section()
        st.session_state.progress["Interactive Story"] = True

    elif st.session_state.page == "timeline_puzzle":
        timeline_puzzle()
        st.session_state.progress["Timeline Puzzle"] = True

    elif st.session_state.page == "rpg_game":
        rpg_game()
        st.session_state.progress["RPG Game"] = True

if __name__ == "__main__":
    main()
