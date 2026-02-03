import streamlit as st
import time
import requests  # This helps us send the email

# --- CONFIGURATION ---
st.set_page_config(page_title="SECURE TERMINAL", page_icon="🔒")

# --- REPLACE THIS WITH YOUR EMAIL ---
# The answers will be sent here.
MY_EMAIL = "kevin@visioneliteassets.xyz" 

# --- CUSTOM CSS (THE LOOK) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
        color: #00ff41;
        font-family: 'Courier New', Courier, monospace;
    }
    input, textarea {
        background-color: #111 !important;
        color: #00ff41 !important;
        border: 1px solid #00ff41 !important;
    }
    div[data-testid="stHeader"] {visibility: hidden;}
    footer {visibility: hidden;}
    button {
        background-color: #00ff41 !important;
        color: #000000 !important;
        border: none !important;
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE ---
if 'step' not in st.session_state:
    st.session_state.step = 1

# --- STEP 1: LOGIN ---
if st.session_state.step == 1:
    st.title("> SYSTEM LOCKED")
    st.write("ENTER ACCESS KEY TO PROCEED:")
    code = st.text_input("KEY:", key="access_code", type="password")
    
    if st.button("AUTHENTICATE"):
        if code == "GHOST-77-ALPHA":
            with st.spinner("DECRYPTING PROTOCOL..."):
                time.sleep(1.5)
            st.session_state.step = 2
            st.rerun()
        else:
            st.error("> ACCESS DENIED. TERMINATING.")

# --- STEP 2: THE INTERROGATION ---
elif st.session_state.step == 2:
    st.title("> IDENTITY PROTOCOL")
    st.write("ANSWER THE FOLLOWING TO DETERMINE ELIGIBILITY.")
    
    with st.form("vetting_form"):
        st.write("**1. DEFINE TARGET ASSET CLASS (UNOBTAINABLE ONLY):**")
        q1 = st.text_input("Target Asset")
        
        st.write("**2. LIQUIDITY STATUS (T+7 DAYS):**")
        q2 = st.text_input("Liquidity")
        
        st.write("**3. WHY SHOULD THE ARCHITECT TRUST YOU?**")
        q3 = st.text_area("Reasoning")
        
        submit = st.form_submit_button("TRANSMIT DATA")
        
        if submit:
            if len(q1) > 2 and len(q3) > 5:
                # --- SEND EMAIL LOGIC ---
                with st.spinner("ENCRYPTING & TRANSMITTING..."):
                    try:
                        response = requests.post(
                            f"https://formsubmit.co/{MY_EMAIL}", 
                            data={"Asset": q1, "Liquidity": q2, "Reason": q3, "_captcha": "false"}
                        )
                        st.session_state.step = 3
                        st.rerun()
                    except:
                        st.error("CONNECTION ERROR. RETRY.")
            else:
                st.warning("> ERROR: INSUFFICIENT DATA.")

# --- STEP 3: SUCCESS ---
elif st.session_state.step == 3:
    st.title("> TRANSMISSION COMPLETE")
    st.success("Dossier created. The Architect will signal you if parameters match.")
    st.write("Connection closing...")
