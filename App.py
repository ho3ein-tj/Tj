import streamlit as st
import numpy as np

# Page Configuration
st.set_page_config(page_title="TAB - Guitar Tools", page_icon="🎸", layout="centered")

# Custom CSS for Dark Lightning Aesthetic
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #000000 0%, #001f3f 100%);
        color: #ffffff;
    }
    h1 {
        text-align: center;
        color: #00d4ff;
        text-shadow: 2px 2px 15px #ffffff;
        font-family: 'Courier New', monospace;
        letter-spacing: 5px;
    }
    .stButton>button {
        width: 100%;
        background-color: transparent;
        border: 2px solid #00d4ff;
        color: #00d4ff;
        box-shadow: 0 0 10px #00d4ff;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #00d4ff;
        color: black;
        box-shadow: 0 0 25px #ffffff;
    }
    .tab-box {
        background-color: rgba(0, 212, 255, 0.1);
        border-left: 5px solid #00d4ff;
        padding: 20px;
        font-family: 'Courier New', monospace;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>TAB PROJECT</h1>")
st.write("---")

# Navigation Tabs
tab1, tab2 = st.tabs(["⚡ Fast Tuner", "🎼 Get Tablature"])

# --- TAB 1: GUITAR TUNER ---
with tab1:
    st.subheader("Guitar Tuner (Standard E)")
    st.info("Check your string pitch below:")
    
    col1, col2, col3 = st.columns(3)
    notes = {"E2": 82.41, "A2": 110.00, "D3": 146.83, "G3": 196.00, "B3": 246.94, "E4": 329.63}
    
    # Simple Visual feedback for tuning
    target_note = st.selectbox("Select String to Tune:", list(notes.keys()))
    current_freq = st.slider("Detected Frequency (Hz)", 70.0, 350.0, 100.0)
    
    diff = current_freq - notes[target_note]
    
    if abs(diff) < 0.5:
        st.success(f"Perfect! {target_note} is in tune. ⚡")
    elif diff < 0:
        st.warning("Too Low (Flat) - Tighten the string.")
    else:
        st.error("Too High (Sharp) - Loosen the string.")

# --- TAB 2: TABLATURE RECEIVER ---
with tab2:
    st.subheader("Request Tablature")
    song_name = st.text_input("Enter Song Name or Artist:", placeholder="e.g. Nothing Else Matters")
    
    if st.button("Generate Tab"):
        if song_name:
            st.write(f"Showing results for: **{song_name}**")
            # Simulated Tablature View
            tab_content = """
            E|---------------------------------|
            B|-------0---------------0---------|
            G|-----0---0-----------0---0-------|
            D|---4-------4-------4-------4-----|
            A|-7-----------7---7-----------7---|
            E|---0-----------0---0-----------0-|
            """
            st.markdown(f'<div class="tab-box"><pre>{tab_content}</pre></div>', unsafe_allow_html=True)
            st.download_button("Download PDF Tab", data=tab_content, file_name="tab.txt")
        else:
            st.error("Please enter a song name first.")

# Footer
st.markdown("<br><hr><p style='text-align: center; opacity: 0.5;'>Powered by Lightning & Steel</p>", unsafe_allow_html=True)
