import streamlit as st
from src.core.planner import TravelPlanner
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Traveller Planner")
st.title("AI Travel Itinerary Planner")
st.write("Plan your day trip itinerary by entering your city and interests")

with st.form("planner_form"):
    city=st.text_input("Enter the City name for your trip")
    interests=st.text_input("Enter your interests (comma separated)")
    submitted=st.form_submit_button("Generate Itinerary")

    if submitted:
        if city and interests:
            planner=TravelPlanner()
            planner.set_city(city)
            planner.set_interests(interests)
            itinerary=planner.create_itinerary()

            st.subheader("📄 Your Itinerary")
            st.markdown(itinerary)
        else:
            st.warning("Please fill City and Interests to move forward!")