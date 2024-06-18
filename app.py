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
            background: url("{bg_image}") no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

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
 
