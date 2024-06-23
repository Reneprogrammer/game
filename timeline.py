import streamlit as st
import random

def load_events():
    return [
        {"event": "The Sudanese Armed Forces and the Rapid Support Forces clashed", "year": 2019},
        {"event": "Sudan gained independence from Britain", "year": 1956},
        {"event": "Omar al-Bashir was ousted from power", "year": 2019},
        {"event": "South Sudan became independent", "year": 2011},
        {"event": "The Comprehensive Peace Agreement was signed", "year": 2005},
    ]

def check_order(selected_order, correct_order):
    return selected_order == correct_order

def timeline_section():
    st.header("Timeline Puzzle: Sudan Conflict")
    st.write("Arrange the events in the correct chronological order:")

    events = load_events()
    random.shuffle(events)  # Shuffle events to randomize their order

    if 'selected_order' not in st.session_state:
        st.session_state.selected_order = [None] * len(events)
    
    for i, event in enumerate(events):
        options = [None] + [e["event"] for e in events]
        st.session_state.selected_order[i] = st.selectbox(
            f"Select the event for year {event['year']}:",
            options,
            index=options.index(st.session_state.selected_order[i]) if st.session_state.selected_order[i] else 0,
            key=f"select_{i}"
        )

    if st.button("Submit"):
        correct_order = [event["event"] for event in sorted(events, key=lambda x: x["year"])]
        if check_order(st.session_state.selected_order, correct_order):
            st.success("Correct! The events are in the correct chronological order.")
        else:
            st.error("Incorrect. Try again.")
            st.write("Correct Order:")
            for event in sorted(events, key=lambda x: x["year"]):
                st.write(f"{event['year']}: {event['event']}")
