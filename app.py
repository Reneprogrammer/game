import streamlit as st
import random
import streamlit.components.v1 as components
import pandas as pd
from quiz import quiz_section
from story import story_section
from rpg import rpg_section
from timeline import timeline_section

# Simulated database using dictionaries
users_db = {
    'user1': 'password1',
    'user2': 'password2'
}

messages_db = []

# Background images and articles
background_images = [
    "https://raw.githubusercontent.com/Reneprogrammer/game/main/image1.jpg",
    "https://raw.githubusercontent.com/Reneprogrammer/game/main/image2.jpg",
    "https://raw.githubusercontent.com/Reneprogrammer/game/main/image3.jpg",
    "https://raw.githubusercontent.com/Reneprogrammer/game/main/image4.jpg",
    "https://raw.githubusercontent.com/Reneprogrammer/game/main/image5.jpg"
]

articles = [
    {"title": "Article 1: Understanding the Roots of the Sudan Conflict", "link": "https://www.economist.com/leaders/2023/11/16/the-world-is-ignoring-war-genocide-and-famine-in-sudan"},
    {"title": "Article 2: The Impact of the Sudan Conflict on Civilians", "link": None},
    {"title": "Article 3: International Efforts in Sudan: A Historical Overview", "link": None},
    {"title": "Article 4: Key Figures in the Sudan Conflict", "link": None},
    {"title": "Article 5: Future Prospects for Peace in Sudan", "link": None}
]

def set_background_image():
    page_index = {
        "main_menu": 0,
        "game_selection": 1,
        "quiz": 2,
        "interactive_story": 3,
        "timeline_puzzle": 4,
        "rpg_game": 5,
        "rewards": 6,
        "community": 7
    }.get(st.session_state.page, 0)
    
    bg_image = background_images[page_index % len(background_images)]
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: white;
        }}
        .bg-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            min-height: 100vh;
            padding-top: 0px;
            margin-top: 0px;
        }}
        .main-content {{
            background: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 10px;
            max-width: 80%;
            color: black;
            margin-top: 0px;
        }}
        .main-content h1, .main-content h2, .main-content h3, .main-content p {{
            color: black;
        }}
        .main-content .stButton>button {{
            background-color: #f4a261;
            color: black;
            font-weight: bold;
            border-radius: 5px;
        }}
        .image-container {{
            margin-top: 20px;
        }}
        .image-container img {{
            width: 100%;
            height: auto;
            max-width: 600px;
        }}
        .stButton {{
            display: flex;
            justify-content: space-between;
        }}
        .rewards-button {{
            margin-left: auto;
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
    if 'page_index' in st.session_state:
        st.markdown(
            f"""
                </div>
                <div class="image-container">
                    <img src="{background_images[st.session_state.page_index % len(background_images)]}" alt="Background Image">
                </div>
            </div>
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

def trigger_confetti():
    confetti_script = """
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.4.0/dist/confetti.browser.min.js"></script>
    <script>
    function confetti() {
        var duration = 5 * 1000;
        var end = Date.now() + duration;

        (function frame() {
            confetti({
                particleCount: 3,
                angle: 60,
                spread: 55,
                origin: { x: 0 }
            });
            confetti({
                particleCount: 3,
                angle: 120,
                spread: 55,
                origin: { x: 1 }
            });

            if (Date.now() < end) {
                requestAnimationFrame(frame);
            }
        }());
    }
    confetti();
    </script>
    """
    components.html(confetti_script, height=0, width=0)

def display_discussion_board():
    st.title("Community Discussion Board")
    st.write("Share your thoughts and insights about the Sudan conflict here.")
    
    for message in messages_db:
        st.write(f"**{message['username']}**: {message['message']}")
    
    st.write("### Post a Message")
    new_message = st.text_area("Your message", "")
    if st.button("Post Message"):
        if new_message:
            message = {
                "username": st.session_state["username"],
                "message": new_message
            }
            messages_db.append(message)
            st.experimental_rerun()

def navigate_to(page):
    st.session_state.page = page
    st.session_state.page_index += 1
    st.experimental_rerun()

def main():
    if 'page' not in st.session_state:
        st.session_state.page = "main_menu"
        st.session_state.page_index = 0
        st.session_state.progress = {"Quiz": False, "Interactive Story": False, "Timeline Puzzle": False, "RPG Game": False}

    set_background_image()  # Ensure background image is set whenever the page is changed

    if 'username' not in st.session_state:
        st.title("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username in users_db and users_db[username] == password:
                st.session_state['username'] = username
                st.experimental_rerun()
            else:
                st.error("Invalid username or password")

    if 'username' in st.session_state:
        if st.session_state.page == "main_menu":
            st.title("Sudan Conflict")
            if st.button("Play"):
                navigate_to('game_selection')
            if st.button("Community"):
                navigate_to('community')

        elif st.session_state.page == "game_selection":
            st.title("Select a Game")
            st.write("Choose one of the following games to learn more about the Sudan conflict.")
            
            col1, col2 = st.columns([3,1])
            with col1:
                if st.button("Quiz"):
                    navigate_to('quiz')

                if st.button("Interactive Story"):
                    navigate_to('interactive_story')

                if st.button("Timeline Puzzle"):
                    navigate_to('timeline_puzzle')

                if st.button("RPG Game"):
                    navigate_to('rpg_game')
            with col2:
                if st.button("Rewards", key="rewards_button"):
                    navigate_to('rewards')

            st.write("### Progress")
            total_games = len(st.session_state.progress)
            completed_games = sum(st.session_state.progress.values())
            st.progress(completed_games / total_games)

            if completed_games > 0:
                trigger_confetti()
                st.success("Congratulations! You've made progress!")

        elif st.session_state.page == "quiz":
            quiz_section()
            if 'quiz_completed' in st.session_state and st.session_state.quiz_completed:
                st.session_state.progress["Quiz"] = True

        elif st.session_state.page == "interactive_story":
            story_section()
            st.session_state.progress["Interactive Story"] = True

        elif st.session_state.page == "timeline_puzzle":
            timeline_section()
            st.session_state.progress["Timeline Puzzle"] = True

        elif st.session_state.page == "rpg_game":
            rpg_section()
            st.session_state.progress["RPG Game"] = True

        elif st.session_state.page == "rewards":
            display_rewards()

        elif st.session_state.page == "community":
            display_discussion_board()

    close_background_image()

if __name__ == "__main__":
    main()
