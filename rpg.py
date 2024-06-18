import streamlit as st

def rpg_game():
    st.title("RPG Game: Understanding the Sudan Conflict")
    st.write("""
    Welcome to this educational RPG game where you'll learn about the Sudan conflict through different scenarios.
    You will choose a character and make decisions that will help you understand the complexities of the conflict.
    """)

    st.header("Choose Your Character")
    character = st.radio("Select a character", ('Journalist', 'Humanitarian Worker', 'Local Citizen'), key='character_selection')

    st.write(f"You have chosen to be a {character}.")

    st.header("Scenarios")

    def scenario_1():
        st.write("Scenario 1: You are covering a story in a conflict zone.")
        decision_1 = st.radio("Do you:", ('Interview locals to get their perspective', 'Visit the front lines to report on the conflict'), key='scenario_1')
        if decision_1 == 'Interview locals to get their perspective':
            st.write("You gather valuable stories from the locals, highlighting the human impact of the conflict.")
            st.write("Educational Info: The Sudan conflict has deeply affected the local population, leading to widespread displacement and humanitarian crises.")
        else:
            st.write("You provide a gripping report from the front lines, but it is dangerous.")
            st.write("Educational Info: Reporting from conflict zones is perilous, and journalists often face significant risks to bring news to the world.")

    def scenario_2():
        st.write("Scenario 2: There is a humanitarian crisis in the region.")
        decision_2 = st.radio("Do you:", ('Coordinate with local NGOs to distribute aid', 'Set up a medical camp to assist the injured'), key='scenario_2')
        if decision_2 == 'Coordinate with local NGOs to distribute aid':
            st.write("You ensure that aid reaches the most vulnerable populations.")
            st.write("Educational Info: Humanitarian efforts in Sudan are critical, as many people depend on aid for survival due to the conflict.")
        else:
            st.write("You provide medical assistance to many injured people, saving lives.")
            st.write("Educational Info: Medical aid is crucial in conflict zones, where healthcare facilities are often overwhelmed or destroyed.")

    def scenario_3():
        st.write("Scenario 3: As a local citizen, you need to ensure the safety of your family.")
        decision_3 = st.radio("Do you:", ('Stay in your home and wait for the conflict to subside', 'Move to a refugee camp for safety'), key='scenario_3')
        if decision_3 == 'Stay in your home and wait for the conflict to subside':
            st.write("You manage to stay safe, but it is a stressful and uncertain time.")
            st.write("Educational Info: Many Sudanese people have to make difficult decisions to ensure their safety during the conflict.")
        else:
            st.write("You find safety in a refugee camp, but the conditions are tough.")
            st.write("Educational Info: Refugee camps provide safety, but living conditions are often harsh, and there is a constant need for resources.")

    if character == 'Journalist':
        scenario_1()
    elif character == 'Humanitarian Worker':
        scenario_2()
    else:
        scenario_3()

    st.header("Conclusion")
    st.write("""
    Thank you for playing this RPG game. Through these scenarios, we hope you have gained a better understanding of the complexities and human impact of the Sudan conflict.
    For more information and ways to help, please visit reputable sources and organizations working in the region.
    """)

    if st.button("Back to Menu"):
        st.session_state.page = "game_selection"
        st.experimental_rerun()
