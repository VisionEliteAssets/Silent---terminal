import streamlit as st
import time
import requests

# --- CONFIGURATION ---
st.set_page_config(page_title="SECURE TERMINAL", page_icon="🔒")

# --- YOUR FORMSPREE LINK ---
# Keep your link exactly as it is!
DATABASE_LINK = "https://hook.eu1.make.com/byospolentn6xc129k6m3sginx9api1f"
# --- CUSTOM CSS ---
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
        
        st.write("**2. LIQUIDITY STATUS:**")
        q2 = st.text_input("Liquidity")
        
        st.write("**3. WHY SHOULD THE ARCHITECT TRUST YOU?**")
        q3 = st.text_area("Reasoning")

        # --- NEW FIELD ADDED HERE ---
        st.write("**4. SECURE RETURN SIGNAL (EMAIL / ID):**")
        q4 = st.text_input("Contact Info")
        
        submit = st.form_submit_button("TRANSMIT DATA")
        
        if submit:
            # We now require q4 (Contact Info) to be filled out
            if len(q1) > 2 and len(q4) > 5:
                with st.spinner("UPLOADING TO VAULT..."):
                    try:
                        response = requests.post(
                            DATABASE_LINK, 
                            data={
                                "Asset": q1, 
                                "Liquidity": q2, 
                                "Reason": q3,
                                "Contact_Signal": q4  # <--- Sends the identity to Formspree
                            }
                        )
                        
                        if response.status_code == 200:
                            st.session_state.step = 3
                            st.rerun()
                        else:
                            st.error(f"UPLOAD FAILED. CODE: {response.status_code}")
                            
                    except Exception as e:
                        st.error(f"SYSTEM CRASH: {e}")
            else:
                st.warning("> ERROR: INSUFFICIENT DATA. IDENTITY REQUIRED.")

# --- STEP 3: SUCCESS ---
elif st.session_state.step == 3:
    st.title("> TRANSMISSION COMPLETE")
    st.success("Dossier securely vaulted.")
