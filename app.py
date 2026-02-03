import streamlit as st
import time
import requests

# --- CONFIGURATION ---
st.set_page_config(page_title="SILENT TERMINAL LIVE", page_icon="🔒")
# --- https://formspree.io/f/mqelnqzb ---
# Example: "https://formspree.io/f/mqkvojzb"
DATABASE_LINK = "https://formspree.io/f/mqelnqzb"

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
                time.sleep(1)
            st.session_state.step = 2
            st.rerun()
        else:
            st.error("> ACCESS DENIED.")

# --- STEP 2: THE INTERROGATION ---
elif st.session_state.step == 2:
    st.title("> IDENTITY PROTOCOL")
    
    with st.form("vetting_form"):
        st.write("**1. TARGET ASSET:**")
        q1 = st.text_input("Target Asset")
        
        st.write("**2. LIQUIDITY:**")
        q2 = st.text_input("Liquidity")
        
        st.write("**3. REASONING:**")
        q3 = st.text_area("Reasoning")
        
        submit = st.form_submit_button("TRANSMIT DATA")
        
        if submit:
            if len(q1) > 2:
                with st.spinner("UPLOADING TO VAULT..."):
                    try:
                        # Send data to Formspree
                        response = requests.post(
                            DATABASE_LINK, 
                            data={"Asset": q1, "Liquidity": q2, "Reason": q3}
                        )
                        
                        if response.status_code == 200:
                            st.session_state.step = 3
                            st.rerun()
                        else:
                            st.error(f"UPLOAD FAILED. CODE: {response.status_code}")
                            st.write("CHECK: Did you paste the correct link?")
                            
                    except Exception as e:
                        st.error(f"SYSTEM CRASH: {e}")

# --- STEP 3: SUCCESS ---
elif st.session_state.step == 3:
    st.title("> TRANSMISSION COMPLETE")
    st.success("Dossier securely vaulted.")
