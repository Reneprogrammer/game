import streamlit as st
import random

# Importing the different sections of the app
from quiz import quiz_section
from story import story_section
from timeline import timeline_puzzle
from rpg import rpg_game

# List of background images
background_images = [
    "https://raw.githubusercontent.com/Reneprogrammer/game/main/image1.jpg",
    "https://raw.githubusercontent.com/Reneprogrammer/game/main/image2.jpg",
    "https://raw.githubusercontent.com/Reneprogrammer/game/main/image3.jpg",
    "https://raw.githubusercontent.com/Reneprogrammer/game/main/image4.jpg",
    "https://raw.githubusercontent.com/Reneprogrammer/game/main/image5.jpg"
]

# List of articles
articles = [
    {"title": "Article 1: Understanding the Roots of the Sudan Conflict", "link": "https://www.economist.com/leaders/2023/11/16/the-world-is-ignoring-war-genocide-and-famine-in-sudan"},
    {"title": "Article 2: The Impact of the Sudan Conflict on Civilians", "link": None},
    {"title": "Article 3: International Efforts in Sudan: A Historical Overview", "link": None},
    {"title": "Article 4: Key Figures in the Sudan Conflict", "link": None},
    {"title": "Article 5: Future Prospects for Peace in Sudan", "link": None}
]

# Function to set the background image
def set_background_image():
    page_index = {
        "main_menu": 0,
        "game_selection": 1,
        "quiz": 2,
        "interactive_story": 3,
        "timeline_puzzle": 4,
        "rpg_game": 5,
        "rewards": 6
    }.get(st.session_state.page, 0)
    
    bg_image = background_images[page_index % len(background_images)]
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: #0e1117;
        }}
        .bg-container {{
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            background-image: url({bg_image});
            background-size: contain;
            background-repeat: no-repeat;
            background-position: top right;
        }}
        .main-content {{
            background: rgba(0, 0, 0, 0.7);
            padding: 20px;
            border-radius: 10px;
            max-width: 80%;
            color: white;
        }}
        .main-content h1, .main-content h2, .main-content h3, .main-content p {{
            color: white;
        }}
        .main-content .stButton>button {{
            background-color: #f4a261;
            color: black;
            font-weight: bold;
            border-radius: 5px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        f"""
        <div class="bg-container">
            <div class="main-content">
        """,
        unsafe_allow_html=True
    )

def close_background_image():
    st.markdown("</div></div>", unsafe_allow_html=True)

def display_rewards():
    st.title("Rewards")
    st.write("Complete the games to unlock free articles about the Sudan conflict.")
    
    unlocked_articles = 0
    for key in st.session_state.progress:
        if st.session_state.progress[key]:
            unlocked_articles += 1
    
    st.write(f"### Progress: {unlocked_articles}/4 games completed")
    
    # Display articles
    for i, article in enumerate(articles):
        if i < unlocked_articles or (unlocked_articles == 4 and i < 3):
            if article["link"]:
                st.write(f"**Unlocked**: [{article['title']}]({article['link']})")
            else:
                st.write(f"**Unlocked**: {article['title']}")
        else:
            st.write(f"**Locked**: {article['title']}")
    
    if st.button("Back to Menu"):
        st.session_state.page = "game_selection"
        st.experimental_rerun()

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

        if st.button("Rewards"):
            st.session_state.page = "rewards"
            st.experimental_rerun()

        st.write("### Progress")
        total_games = len(st.session_state.progress)
        completed_games = sum(st.session_state.progress.values())
        st.progress(completed_games / total_games)

    elif st.session_state.page == "quiz":
        quiz_section()
        if 'quiz_completed' in st.session_state and st.session_state.quiz_completed:
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

    elif st.session_state.page == "rewards":
        display_rewards()

    close_background_image()

if __name__ == "__main__":
    main()
