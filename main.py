import re
import streamlit as st

st.markdown("""<style>
    body {
        background-color: yellow;
    }
    .stButton > button {
        background-color: blue;
        color: white;
    }
    .stButton > button:hover {
        background-color: purple;
        color: pink;
    }
</style>""", unsafe_allow_html=True)

st.markdown("""<h1 style="color:blue;text-align:center">🔏 Secure Password Manager</h1>""",unsafe_allow_html=True)

st.write("Enter Your password below to check its security level 🔎")

def password_check(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")


    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password must include both uppercase [A-Z] and lowercase [a-z].")


    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include at least one number (0-9).")


    if re.search(r"[!@#$%^&*(){}[\]]", password):
        score += 1
    else:
        feedback.append("❌ Password should include a special character (!@#$%^&*(){}[]).")

 
    if score == 4:
        st.success("✅ Strong Password! Your password is secure.")
    elif score == 3:
        st.info("⚠️ Moderate Password. Consider adding more features like a special character or number.")
    else:
        st.error("❌ Weak Password. Follow the suggestions below.")
        if feedback:
            with st.expander("Improve your password"):
                for item in feedback:
                    st.write(item)

password = st.text_input("Enter Your Password", type="password", help="Ensure your password is strong.")

if st.button("Check Strength"):
    if password:
        password_check(password)
    else:
        st.warning("⚠️ Please enter a password first.")





