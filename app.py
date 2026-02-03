import streamlit as st
import time

# --- CONFIGURATION (THE LOOK) ---
st.set_page_config(page_title="SECURE TERMINAL", page_icon="🔒")

# --- CUSTOM CSS (BLACK SCREEN / GREEN TEXT) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
        color: #00ff41;
        font-family: 'Courier New', Courier, monospace;
    }
    input {
        background-color: #111 !important;
        color: #00ff41 !important;
        border: 1px solid #00ff41 !important;
    }
    div[data-testid="stHeader"] {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE (MEMORY) ---
if 'step' not in st.session_state:
    st.session_state.step = 1

# --- THE TERMINAL LOGIC ---

# STEP 1: ACCESS CODE
if st.session_state.step == 1:
    st.title("> SYSTEM LOCKED")
    st.write("ENTER ACCESS KEY TO PROCEED:")
    code = st.text_input("KEY:", key="access_code")
    
    if st.button("AUTHENTICATE"):
        if code == "GHOST-77-ALPHA":
            with st.spinner("DECRYPTING PROTOCOL..."):
                time.sleep(2)  # Fake loading for effect
            st.session_state.step = 2
            st.rerun()
        else:
            st.error("> ACCESS DENIED. TERMINATING.")

# STEP 2: THE INTERROGATION
elif st.session_state.step == 2:
    st.title("> IDENTITY PROTOCOL")
    
    with st.form("vetting_form"):
        st.write("1. DEFINE TARGET ASSET CLASS (UNOBTAINABLE ONLY):")
        q1 = st.text_input("INPUT_1")
        
        st.write("2. LIQUIDITY STATUS (T+7 DAYS):")
        q2 = st.text_input("INPUT_2")
        
        st.write("3. WHY SHOULD THE ARCHITECT TRUST YOU?")
        q3 = st.text_area("INPUT_3")
        
        submit = st.form_submit_button("TRANSMIT DATA")
        
        if submit:
            if len(q1) > 2 and len(q3) > 5:
                st.session_state.step = 3
                st.rerun()
            else:
                st.warning("> ERROR: INSUFFICIENT DATA.")

# STEP 3: SUCCESS
elif st.session_state.step == 3:
    st.balloons()
    st.title("> TRANSMISSION COMPLETE")
    st.success("Dossier created. The Architect will signal you if parameters match.")
    st.write("Connection closing in 3... 2... 1...")
