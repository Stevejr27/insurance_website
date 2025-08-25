import streamlit as st

# Page setup
st.set_page_config(page_title="Insurance Portal", layout="wide")

# Sidebar navigation
st.sidebar.title("Insurance Website")
page = st.sidebar.radio("Navigate", ["🏠 Home", "📋 Policies", "💰 Premium Calculator", "📞 Contact"])

# --- Home Page ---
if page == "🏠 Home":
    st.title("Welcome to SafeLife Insurance 🛡️")
    st.write("""
    We provide trusted insurance plans to secure your future.  
    Choose from a wide range of policies including health, life, motor, and travel insurance.
    """)

    st.image("https://images.unsplash.com/photo-1605902711622-cfb43c4437d1", use_column_width=True)

# --- Policies Page ---
elif page == "📋 Policies":
    st.header("Our Insurance Policies")
    st.subheader("1. Health Insurance 🏥")
    st.write("Covers hospitalization, medical bills, and emergencies.")
    
    st.subheader("2. Life Insurance ❤️")
    st.write("Secure your family’s future with our life cover plans.")
    
    st.subheader("3. Motor Insurance 🚗")
    st.write("Covers accidents, damages, and third-party liabilities.")
    
    st.subheader("4. Travel Insurance ✈️")
    st.write("Stay worry-free while traveling abroad.")

# --- Premium Calculator ---
elif page == "💰 Premium Calculator":
    st.header("Insurance Premium Calculator")
    
    policy_type = st.selectbox("Select Policy Type", ["Health", "Life", "Motor", "Travel"])
    age = st.slider("Enter Your Age", 18, 70, 30)
    coverage = st.number_input("Coverage Amount (₹)", min_value=100000, step=50000)
    
    if st.button("Calculate Premium"):
        base_rate = 0.01  # 1% base rate
        if policy_type == "Health":
            rate = base_rate + 0.002 * (age / 10)
        elif policy_type == "Life":
            rate = base_rate + 0.003 * (age / 10)
        elif policy_type == "Motor":
            rate = base_rate + 0.005
        else:  # Travel
            rate = base_rate + 0.002
        
        premium = coverage * rate
        st.success(f"Estimated Premium: ₹ {premium:,.2f} per year")

# --- Contact Page ---
elif page == "📞 Contact":
    st.header("Contact Us")
    st.write("📍 Address: 123 Insurance Street, Kochi, India")  
    st.write("📧 Email: support@safelife.com")  
    st.write("📞 Phone: +91-9876543210")  
    
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")
    
    if st.button("Submit"):
        st.success(f"Thank you {name}, our team will reach out to you at {email}.")