import streamlit as st
import openai
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from streamlit_folium import folium_static
import folium
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
import base64
from io import BytesIO
from PIL import Image
import time
import random

# Set up OpenAI client
openai.api_key = os.getenv("AIML_API_KEY")
openai.api_base = "https://api.aimlapi.com"

# Streamlit app layout
st.set_page_config(layout="wide", page_title="EcoSphere 🌍")

# Define language options with full names and emoji flags
LANGUAGES = {
    "en": "🇬🇧 English",
    "es": "🇪🇸 Español",
    "fr": "🇫🇷 Français",
    "de": "🇩🇪 Deutsch",
    "it": "🇮🇹 Italiano",
    "pt": "🇵🇹 Português",
    "hi": "🇮🇳 हिन्दी",
    "th": "🇹🇭 ไทย"
}

# Initialize session state for language preference
if 'language' not in st.session_state:
    st.session_state.language = "en"

# Create a function for language selection
def language_selector():
    selected_language = st.sidebar.selectbox(
        "🌐 Select Language",
        options=list(LANGUAGES.keys()),
        format_func=lambda x: LANGUAGES[x],
        index=list(LANGUAGES.keys()).index(st.session_state.language)
    )
    if selected_language != st.session_state.language:
        st.session_state.language = selected_language
        st.rerun()

# Use st.session_state.language throughout the app instead of asking for language selection multiple times

# Initialize session state variables
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "You are an AI assistant specializing in the circular economy. You provide insightful, practical, and innovative solutions to enhance sustainability and resource efficiency. You communicate in a clear and engaging manner, making complex topics easy to understand."}
    ]
if 'resources' not in st.session_state:
    st.session_state['resources'] = []

# Define functions
def generate_multilingual_response(prompt, language, model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo"):
    """
    Generate a multilingual response from the AI model based on the given prompt and language.

    Args:
        prompt (str): The user input prompt.
        language (str): The desired language code (e.g., "en", "es", "fr").
        model (str): The model to use for generating the response.

    Returns:
        str: The AI-generated response in the specified language.
    """
    try:
        # Add language instruction to the system message
        language_instruction = f"Please respond in {language}."
        st.session_state['messages'][0]["content"] += f" {language_instruction}"

        # Add user message to the conversation history
        st.session_state['messages'].append({"role": "user", "content": prompt})

        # Generate response from the AI
        response = openai.ChatCompletion.create(
            model=model,
            messages=st.session_state['messages']
        )

        # Extract the AI response
        ai_response = response.choices[0].message['content']

        # Add AI response to the conversation history
        st.session_state['messages'].append({"role": "assistant", "content": ai_response})

        # Remove the language instruction from the system message
        st.session_state['messages'][0]["content"] = st.session_state['messages'][0]["content"].replace(language_instruction, "")

        return ai_response
    except Exception as e:
        st.error("An error occurred while generating the response. Please try again.")
        print(f"Error: {e}")
        return None
        
def autonomous_waste_management(waste_level, threshold):
    """Autonomous decision making for waste management using Llama"""
    prompt = f"""
    Current waste level: {waste_level:.2f}
    Threshold: {threshold}
    
    Based on this information, provide a detailed waste management decision. Include:
    1. Whether action is needed
    2. Specific steps to take if action is needed
    3. Recommendations for future waste reduction
    4. Any relevant circular economy principles that apply to this situation
    
    Provide your response in {LANGUAGES[st.session_state.language].split()[1]}.
    """
    return generate_multilingual_response(prompt, st.session_state.language)

def learn_from_interaction(interaction_history):
    """Learn from user interactions using Llama"""
    interactions = "".join(interaction_history[-10:])  # Consider last 10 interactions
    prompt = f"""
    Analyze the following user interactions related to circular economy:
    
    {interactions}
    
    Based on these interactions:
    1. Identify the most common topics or concerns
    2. Suggest three ways to improve our circular economy solutions
    3. Propose a new feature or service that would address user needs
    4. Explain how these insights align with circular economy principles
    
    Provide your analysis in {LANGUAGES[st.session_state.language].split()[1]}.
    """
    return generate_multilingual_response(prompt, st.session_state.language)

def adaptive_resource_allocation(resources, demand):
    """Adaptive resource allocation using Llama"""
    prompt = f"""
    Available Resources:
    {resources}
    
    Current Demand:
    {demand}
    
    Based on this information:
    1. Allocate resources optimally, considering circular economy principles
    2. Explain the rationale behind your allocation
    3. Suggest strategies to better balance supply and demand in the future
    4. Identify any potential circular economy opportunities in this scenario
    
    Provide your analysis and recommendations in {LANGUAGES[st.session_state.language].split()[1]}.
    """
    return generate_multilingual_response(prompt, st.session_state.language)
    
# Sidebar
with st.sidebar:
    language_selector()
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "Waste Management", "Interaction Analysis", "Resource Allocation", "Chat", "Data Visualization"],
        icons=["house", "trash", "gear", "diagram-3", "chat-dots", "graph-up"],
        menu_icon="cast",
        default_index=0,
    )

# Main content
st.title(f"EcoSphere 🌍 - {LANGUAGES[st.session_state.language]}")

if selected == "Home":
    st.write("Welcome to EcoSphere, the Circular Economy AI Agent. Select a function from the sidebar to get started.")
    
    # Add some introductory information about circular economy
    st.markdown("""
    ## What is Circular Economy?
    The circular economy is an economic model designed to eliminate waste and maximize resource use. It follows three principles:
    1. Design out waste and pollution
    2. Keep products and materials in use
    3. Regenerate natural systems
    
    Use the navigation menu on the left to explore our AI-powered tools for circular economy management.
    """)

elif selected == "Waste Management":
    # Your existing code for waste management
    st.header("🗑️ Autonomous Waste Management")

    col1, col2 = st.columns(2)
    with col1:
        waste_level = st.number_input("Current Waste Level (tons)", min_value=0.0, value=100.0, step=0.1)
    with col2:
        threshold = st.slider("Waste Threshold (tons)", 0, 200, 150)

    if st.button("Analyze Waste Scenario"):
        with st.spinner("Analyzing waste management scenario..."):
            decision = autonomous_waste_management(waste_level, threshold)
        st.success("Analysis Complete!")
        st.write(decision)

    # Add a visual representation of waste level using graph_objects
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=waste_level,
        title={"text": "Current Waste Level"},
        gauge={"axis": {"range": [0, 200]}}
        ))

    st.plotly_chart(fig)


elif selected == "Interaction Analysis":
    st.header("⚙️ Learning from Interactions")
    
    if 'interaction_history' not in st.session_state:
        st.session_state.interaction_history = []
    
    user_input = st.text_area("Enter your query about circular economy:", height=100)
    if st.button("Submit Query"):
        st.session_state.interaction_history.append(user_input)
        st.success("Query submitted!")
    
    if st.button("Analyze Recent Interactions"):
        if len(st.session_state.interaction_history) > 0:
            with st.spinner("Analyzing recent interactions..."):
                insights = learn_from_interaction(st.session_state.interaction_history)
            st.write(insights)
        else:
            st.warning("No interactions to analyze yet. Please submit some queries first.")
    
    # Display recent interactions
    if st.session_state.interaction_history:
        st.subheader("Recent Interactions")
        for i, interaction in enumerate(st.session_state.interaction_history[-5:], 1):
            st.text(f"{i}. {interaction}")

elif selected == "Resource Allocation":
    st.header("⚖️ Adaptive Resource Allocation")
    
    resources = {'Water': 100, 'Energy': 200, 'Raw Materials': 150}
    
    st.subheader("Available Resources")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Water", f"{resources['Water']} units")
    with col2:
        st.metric("Energy", f"{resources['Energy']} units")
    with col3:
        st.metric("Raw Materials", f"{resources['Raw Materials']} units")
    
    st.subheader("Set Resource Demand")
    demand = {}
    col1, col2, col3 = st.columns(3)
    with col1:
        demand['Water'] = st.slider("Water Demand", 0, 100, 50)
    with col2:
        demand['Energy'] = st.slider("Energy Demand", 0, 200, 100)
    with col3:
        demand['Raw Materials'] = st.slider("Raw Materials Demand", 0, 150, 75)
    
    if st.button("Generate Allocation Plan"):
        with st.spinner("Generating resource allocation plan..."):
            allocation_plan = adaptive_resource_allocation(resources, demand)
        st.success("Allocation Plan Generated!")
        st.write(allocation_plan)
    
    # Visualize resource allocation
    fig = px.bar(x=list(demand.keys()), y=list(demand.values()), title="Resource Demand")
    st.plotly_chart(fig)

elif selected == "Chat":
    st.header("💬 Chat with AI Assistant")
    
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What would you like to know about circular economy?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            for response in generate_multilingual_response(prompt, st.session_state.language):
                full_response += response
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

elif selected == "Data Visualization":
    st.header("📊 Circular Economy Data Visualization")
    
    # Sample data for visualization
    data = pd.DataFrame({
        'Category': ['Recycling', 'Reuse', 'Repair', 'Reduce'],
        'Percentage': [40, 30, 20, 10]
    })
    
    # Pie chart
    fig1 = px.pie(data, values='Percentage', names='Category', title='Circular Economy Activities')
    st.plotly_chart(fig1)
    
    # Line chart (simulated time series data)
    time_data = pd.DataFrame({
        'Date': pd.date_range(start='2023-01-01', periods=12, freq='M'),
        'Waste Reduction': np.random.randint(50, 100, 12)
    })
    fig2 = px.line(time_data, x='Date', y='Waste Reduction', title='Waste Reduction Over Time')
    st.plotly_chart(fig2)

# Footer
st.sidebar.markdown("---")
st.sidebar.info(f"Current Language: {LANGUAGES[st.session_state.language]}")
