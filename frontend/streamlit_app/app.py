import streamlit as st
import requests
import os
from langchain_community.llms import CTransformers

# ✅ Load Model Once & Cache It
@st.cache_resource
def load_model():
    MODEL_PATH = "models/llama-2-7b-chat.Q4_K_M.gguf"

    if not os.path.exists(MODEL_PATH):
        st.error("❌ ERROR: Model file not found.")
        st.stop()

    try:
        llm = CTransformers(
            model=MODEL_PATH,
            model_type="llama",
            config={
                "max_new_tokens": 100,
                "temperature": 0.1,
                "context_length": 128,
                "batch_size": 16,
                "stream": True
            }
        )
        st.success("✅ LLaMA 2 Model Loaded & Cached!")
        return llm
    except Exception as e:
        st.error(f"❌ ERROR: Failed to load LLaMA model! {str(e)}")
        st.stop()

# ✅ Load Model
llm = load_model()

# ✅ API Base URL
API_BASE_URL = "http://127.0.0.1:8000/api"

# ✅ User Authentication Functions
def register(username, email, password, confirm_password):
    response = requests.post(f"{API_BASE_URL}/register/", json={
        "username": username,
        "email": email,
        "password": password,
        "confirm_password": confirm_password
    })
    return response

def login(username, password):
    response = requests.post(f"{API_BASE_URL}/login/", json={"username": username, "password": password})
    if response.status_code == 200:
        user_data = response.json()
        st.session_state["token"] = user_data["token"]
        st.session_state["username"] = user_data["username"]
        st.session_state["page"] = "generate"  # ✅ Redirect to blog page
        st.success("✅ Login Successful!")
        st.rerun()
    else:
        st.error("❌ Invalid Credentials")

def logout():
    st.session_state.clear()
    st.rerun()

# ✅ Sidebar for Authentication & Navigation
st.sidebar.title("🔑 User Authentication")

if "token" not in st.session_state:
    tab1, tab2 = st.sidebar.tabs(["Login", "Register"])

    with tab1:
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")
        if st.button("Login"):
            login(username, password)

    with tab2:
        reg_username = st.text_input("Username", key="reg_username")
        reg_email = st.text_input("Email", key="reg_email")
        reg_password = st.text_input("Password", type="password", key="reg_password")
        reg_confirm_password = st.text_input("Confirm Password", type="password", key="reg_confirm_password")
        if st.button("Register"):
            response = register(reg_username, reg_email, reg_password, reg_confirm_password)
            if response.status_code == 201:
                st.success("✅ Registration Successful! Please log in.")
            else:
                st.error(response.json().get("error", "❌ Registration Failed!"))

    st.stop()

st.sidebar.write(f"✅ Logged in as: {st.session_state['username']}")
if st.sidebar.button("Logout"):
    logout()

# ✅ Sidebar History (Saved Blogs)
st.sidebar.subheader("📜 Saved Blogs")
if "page" not in st.session_state:
    st.session_state["page"] = "generate"  # ✅ Default to blog generator page

headers = {"Authorization": f"Bearer {st.session_state['token']}"}
response = requests.get(f"{API_BASE_URL}/blogs/", headers=headers)

if response.status_code == 200:
    blogs = response.json()
    if not blogs:
        st.sidebar.info("No saved blogs yet!")
    else:
        for blog in blogs:
            if st.sidebar.button(blog["title"], key=f"blog_{blog['id']}"):
                st.session_state["page"] = f"blog_{blog['id']}"
                st.session_state["selected_blog"] = blog  # ✅ Store selected blog
                st.rerun()
else:
    st.sidebar.error("❌ Failed to fetch saved blogs.")

# ✅ Page Handling
if st.session_state["page"].startswith("blog_"):
    blog = st.session_state["selected_blog"]
    st.title("📜 Saved Blog")
    st.subheader(f"📌 Title: {blog['title']}")
    
    st.write("---")  # Separator
    st.write(blog["content"])  # ✅ Display only the blog content

    if st.button("⬅️ Back to Generator"):
        st.session_state["page"] = "generate"
        st.rerun()


elif st.session_state["page"] == "generate":
    # ✅ Blog Generation UI
    st.header("📝 AI Blog Generator")

    title = st.text_input("📌 Blog Title")
    word_count = st.slider("📝 Word Count", 100, 1000, 500)
    audience = st.selectbox("🎯 Target Audience", ["General", "Researchers", "Travellers", "Content Creators", "Tech Enthusiasts", "Students", "Professionals"])

    @st.cache_data
    def generate_blogs(title, audience, word_count):
        blogs = []
        for i in range(3):  
            prompt = f"Variation {i+1}: Write a {word_count}-word blog for {audience} about {title}."
            response = llm.invoke(prompt)
            blogs.append(response if response.strip() else "❌ Error: No valid content generated.")
        return blogs

    if st.button("Generate Blog"):
        st.session_state["generated_blogs"] = generate_blogs(title, audience, word_count)
        st.session_state["blog_saved"] = False  # ✅ Reset save flag

    if "generated_blogs" in st.session_state:
        blogs = st.session_state["generated_blogs"]
        st.write("### ✨ AI Generated Blogs")

        for idx, blog in enumerate(blogs):
            with st.container():
                st.write(f"#### Blog Option {idx+1}")
                st.write(blog)

                # ✅ Allow only ONE blog to be saved
                if not st.session_state.get("blog_saved"):
                    if st.button(f"💾 Save Blog {idx+1}", key=f"save_{idx}"):
                        headers = {"Authorization": f"Bearer {st.session_state['token']}"}
                        save_response = requests.post(
                            f"{API_BASE_URL}/save-blog/",
                            json={"title": title, "content": blog, "word_count": word_count, "target_audience": audience},
                            headers=headers
                        )

                        if save_response.status_code == 201:
                            st.success("✅ Blog saved successfully!")
                            st.session_state["blog_saved"] = True  # ✅ Mark as saved
                            st.rerun()
                        else:
                            st.error(f"❌ Failed to save blog. Response: {save_response.text}")

    else:
        st.error("❌ No blog content generated.")
