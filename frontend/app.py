import streamlit as st
import requests

API = "http://127.0.0.1:8000"

st.title("DevConnect Pro")

menu = st.sidebar.selectbox("Menu", ["Register", "Post Project", "View Projects"])

# Register
if menu == "Register":
    st.subheader("User Registration")

    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["developer", "company"])

    if st.button("Register"):
        data = {
            "name": name,
            "email": email,
            "password": password,
            "role": role
        }
        r = requests.post(f"{API}/register", json=data)
        st.success("Registered Successfully")


# Post Project
elif menu == "Post Project":
    st.subheader("Create Project")

    title = st.text_input("Title")
    description = st.text_area("Description")
    skills = st.text_input("Skills (comma separated)")
    budget = st.number_input("Budget")

    if st.button("Create"):
        data = {
            "title": title,
            "description": description,
            "skills": skills,
            "budget": int(budget)
        }
        requests.post(f"{API}/create_project", json=data)
        st.success("Project Created")


# View Projects
elif menu == "View Projects":
    st.subheader("Available Projects")

    r = requests.get(f"{API}/projects")
    projects = r.json()

    for p in projects:
        st.write(p["title"])
        st.write(p["description"])
        st.write("Skills:", p["skills"])
        st.write("Budget:", p["budget"])
        st.markdown("---")
