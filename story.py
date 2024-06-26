import streamlit as st

def display_story_part(story, current_part_id):
    story_part = story[current_part_id]
    st.write(story_part["text"])
    for option in story_part["options"]:
        if st.button(option["label"], key=f"{current_part_id}_{option['next_part']}"):
            st.session_state.current_part_id = option["next_part"]
            st.experimental_rerun()

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
        "hr_abuses": {
            "id": "hr_abuses",
            "text": "The official denies any human rights abuses, claiming they are propaganda. Do you...",
            "options": [
                {"label": "Challenge their claim", "next_part": "challenge_claim"},
                {"label": "Move to another topic", "next_part": "econ_policies"}
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
        "foreign_aid": {
            "id": "foreign_aid",
            "text": "The official discusses the role of foreign aid in supporting the government's efforts. Do you...",
            "options": [
                {"label": "Ask about the sources of aid", "next_part": "sources_of_aid"},
                {"label": "Move to another topic", "next_part": "infrastructure"}
            ]
        },
        "infrastructure": {
            "id": "infrastructure",
            "text": "The official highlights various infrastructure projects aimed at improving the country's economy. Do you...",
            "options": [
                {"label": "Ask about the impact on local communities", "next_part": "impact_on_communities"},
                {"label": "Move to another topic", "next_part": "gov_official"}
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
        "rebel_demands": {
            "id": "rebel_demands",
            "text": "The rebel leader lists their demands for peace and justice. Do you...",
            "options": [
                {"label": "Ask about their negotiation strategies", "next_part": "negotiation_strategies"},
                {"label": "Inquire about international support", "next_part": "international_support"}
            ]
        },
        "rebel_tactics": {
            "id": "rebel_tactics",
            "text": "The rebel leader explains the tactics used in their struggle. Do you...",
            "options": [
                {"label": "Ask about the impact on civilians", "next_part": "impact_on_civilians"},
                {"label": "Inquire about their future plans", "next_part": "future_plans"}
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
        "daily_challenges": {
            "id": "daily_challenges",
            "text": "The civilian describes the daily challenges they face, including access to food and water. Do you...",
            "options": [
                {"label": "Ask about community support", "next_part": "community_support"},
                {"label": "Inquire about safety concerns", "next_part": "safety_concerns"}
            ]
        },
        "future_hopes": {
            "id": "future_hopes",
            "text": "The civilian expresses their hopes for a peaceful and stable future. Do you...",
            "options": [
                {"label": "Ask about their vision for peace", "next_part": "vision_for_peace"},
                {"label": "Inquire about their plans if peace is achieved", "next_part": "plans_for_peace"}
            ]
        },
        # Continue to build out the story
        "challenge_claim": {
            "id": "challenge_claim",
            "text": "You challenge the government's claim about human rights abuses. They respond defensively. Do you...",
            "options": [
                {"label": "Press further", "next_part": "press_further"},
                {"label": "Move to another topic", "next_part": "econ_policies"}
            ]
        },
        "press_further": {
            "id": "press_further",
            "text": "You press further on the human rights abuses. The official reluctantly admits some issues. Do you...",
            "options": [
                {"label": "Ask about steps to address the abuses", "next_part": "address_abuses"},
                {"label": "Move to another topic", "next_part": "foreign_aid"}
            ]
        },
        "address_abuses": {
            "id": "address_abuses",
            "text": "The official outlines the steps being taken to address human rights abuses. Do you...",
            "options": [
                {"label": "Thank them for their time", "next_part": "end"},
                {"label": "Move to another topic", "next_part": "econ_policies"}
            ]
        },
        "negotiation_strategies": {
            "id": "negotiation_strategies",
            "text": "The rebel leader discusses their strategies for negotiation. Do you...",
            "options": [
                {"label": "Ask about their allies", "next_part": "allies"},
                {"label": "Inquire about potential compromises", "next_part": "compromises"}
            ]
        },
        "international_support": {
            "id": "international_support",
            "text": "The rebel leader talks about the international support they receive. Do you...",
            "options": [
                {"label": "Ask about the types of support", "next_part": "types_of_support"},
                {"label": "Inquire about their future plans", "next_part": "future_plans"}
            ]
        },
        "impact_on_civilians": {
            "id": "impact_on_civilians",
            "text": "The rebel leader admits that civilians are affected by their tactics. Do you...",
            "options": [
                {"label": "Ask about measures to protect civilians", "next_part": "protect_civilians"},
                {"label": "Inquire about their future plans", "next_part": "future_plans"}
            ]
        },
        "future_plans": {
            "id": "future_plans",
            "text": "The rebel leader outlines their future plans. Do you...",
            "options": [
                {"label": "Ask about potential obstacles", "next_part": "obstacles"},
                {"label": "Thank them for their time", "next_part": "end"}
            ]
        },
        "community_support": {
            "id": "community_support",
            "text": "The civilian talks about how the community supports each other during these times. Do you...",
            "options": [
                {"label": "Ask about the role of NGOs", "next_part": "role_of_ngos"},
                {"label": "Inquire about safety concerns", "next_part": "safety_concerns"}
            ]
        },
        "safety_concerns": {
            "id": "safety_concerns",
            "text": "The civilian shares their safety concerns and how they try to protect themselves. Do you...",
            "options": [
                {"label": "Ask about the role of security forces", "next_part": "role_of_security"},
                {"label": "Inquire about their future hopes", "next_part": "future_hopes"}
            ]
        },
        "vision_for_peace": {
            "id": "vision_for_peace",
            "text": "The civilian describes their vision for peace. Do you...",
            "options": [
                {"label": "Ask about steps to achieve this vision", "next_part": "steps_for_peace"},
                {"label": "Inquire about community involvement", "next_part": "community_involvement"}
            ]
        },
        "plans_for_peace": {
            "id": "plans_for_peace",
            "text": "The civilian shares their plans if peace is achieved. Do you...",
            "options": [
                {"label": "Ask about potential challenges", "next_part": "potential_challenges"},
                {"label": "Thank them for their time", "next_part": "end"}
            ]
        },
        "end": {
            "id": "end",
            "text": "Thank you for exploring the story. You have completed this path.",
            "options": []
        }
    }

def story_section():
    st.header("Interactive Story: Experience the Sudan Conflict")
    st.write("Make choices to navigate through the story and learn about the Sudan conflict.")

    story = load_story()
    if 'current_part_id' not in st.session_state:
        st.session_state.current_part_id = "start"

    display_story_part(story, st.session_state.current_part_id)
