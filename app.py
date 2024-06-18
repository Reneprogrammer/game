import streamlit as st
import random
import streamlit.components.v1 as components
import pandas as pd

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
        "rewards": 6
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
            align-items: center;
            justify-content: center;
            height: 100vh;
            background-image: url({bg_image});
            background-size: contain;
            background-repeat: no-repeat;
            background-position: top right;
        }}
        .main-content {{
            background: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 10px;
            max-width: 80%;
            color: black;
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

def main():
    if 'page' not in st.session_state:
        st.session_state.page = "main_menu"
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
                st.session_state.page = "game_selection"
                st.experimental_rerun()
            if st.button("Community"):
                st.session_state.page = "community"
                st.experimental_rerun()
            # Add chatbot section
            st.header("Ask the Chatbot")
            user_input = st.text_input("Ask a question about the Sudan conflict:")
            if user_input:
                response = get_chatbot_response(user_input)
                st.write(f"Chatbot: {response}")

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
            timeline_puzzle()
            st.session_state.progress["Timeline Puzzle"] = True

        elif st.session_state.page == "rpg_game":
            rpg_game()
            st.session_state.progress["RPG Game"] = True

        elif st.session_state.page == "rewards":
            display_rewards()

        elif st.session_state.page == "community":
            display_discussion_board()

    close_background_image()

if __name__ == "__main__":
    main()
