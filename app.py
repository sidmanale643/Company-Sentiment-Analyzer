import streamlit as st
import requests

st.title("Company Sentiment Analyzer")

company_name = st.text_input("Enter Company Name", "Tesla")
model_provider = st.selectbox("LLM Model Provider", options=["Ollama", "Groq"])
tts_provider = st.selectbox("TTS Provider", options=["ElevenLabs", "Indic Parler TTS"])

if st.button("Fetch Sentiment Data"):
    api_url = (
        f"http://localhost:8000/home?"
        f"company_name={company_name}&model_provider={model_provider}&tts_provider={tts_provider}"
    )

    try:
        response = requests.get(api_url)
        response.raise_for_status()

        data = response.json()

        st.subheader("Sentiment Analyzer Output")
        st.write(data)
        
        # st.subheader("Company Name")
        # st.write(data.get("company_name"))

        # st.subheader("Final Report")
        # st.write(data.get("final_report"))

        st.subheader("🔊 Audio Output")
        audio_file = "output.mp3"
        if audio_file:
            st.audio(audio_file)

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
