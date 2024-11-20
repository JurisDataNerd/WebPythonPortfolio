import streamlit as st
import time
from PIL import Image
from datetime import datetime
import requests
from io import BytesIO

# Page configuration
st.set_page_config(page_title="Fauzan's Portfolio", page_icon=":sparkles:")

# Typing animation for the title
title_text = "Fauzan Arisanto | Innovator in Technology & Law"
title_placeholder = st.empty()
animation_speed = 0.1  

# Display the title with typing effect
for i in range(len(title_text) + 1):
    title_placeholder.title(title_text[:i])
    time.sleep(animation_speed)

# Year for Copyright
current_year = datetime.now().year

# Helper function to fetch image from GitHub
def fetch_image_from_github(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

# Base GitHub raw URL
base_url = "https://raw.githubusercontent.com/JurisDataNerd/WebPythonPortfolio/main/WebPythonProjects/assets/"

# Display profile image and About Me section
col1, col2 = st.columns([2, 1])  
with col2:
    img_url = base_url + "Fauzan%20User%20CV.jpeg"
    img = fetch_image_from_github(img_url)
    st.image(img, width=150)

with col1:
    st.write("About Me")
    st.write("""
    Hi! I'm a double degree student in Informatics and Law. I am passionate about technology and its applications in everyday life.
    """)

time.sleep(0.5) 

# Tabs for sections
tabs = st.tabs(["Experience", "Education", "Organization", "Projects", "Certifications", "Languages", "Skills & Interest", "Contact"])

# Experience Tab
with tabs[0]:
    st.header("Experience")
    time.sleep(0.3) 
    st.write("""
     - Dormitory, Manager 
     Pandega Padma Residence by Mamikos  

     - SNIXSNAP, Company Owner
     Shoe Cleaning Service
    
    - TBB Kebab & Coffee, Headbar
    Restaurant & Coffee
    """)

# Education Tab
with tabs[1]:
    st.header("Education")
    time.sleep(0.3) 
    st.write("""
     - Bachelor of Law 
       Universitas Terbuka  
       Expected Graduation: 2025 (GPA: 3.26/4.00)

     - Bachelor of Informatics
       Universitas Nahdlatul Ulama Yogyakarta  
       Expected Graduation: 2026 (GPA: 3.92/4.00)
    """)

# Organization Tab
with tabs[2]:
    st.header("Organizations")
    time.sleep(0.3) 
    st.write("""
     - Informatics Student Association  
       Universitas Nahdlatul Ulama Yogyakarta  
       Vice Treasurer (2024-2025)
    """)

# Projects Tab
with tabs[3]:
    st.header("Projects")
    st.write("### 3D Environmental Awareness Campaign: Jogja Waste Management Solutions")
    st.write("by Fauzan Arisanto")
    
    video_url = base_url + "Fauzan%20Blender3D.mp4"
    st.video(video_url)

# Certifications Tab
with tabs[4]:
    st.header("Certifications")
    time.sleep(0.3) 
    st.write("""
    Here are a few certifications that showcase my skills and interests:

    - TOEFL Prediction Test, Scored 620 – Daily Bahasa Inggris. 
    - Learning the Basics of Artificial Intelligence (AI) - Dicoding Indonesia.
    - Structured Query Language (SQL) Basics for Beginners - Dicoding Indonesia.		
    - Data Visualization for Beginners - Dicoding Indonesia.
    - Getting Started with Python Programming - Dicoding Indonesia.
    - Learning the Basics of DevOps - Dicoding Indonesia.
    """)

    certificate_images = [
        {"path": "TOEFL%20Prediction.jpeg", "title": "TOEFL Prediction"},
        {"path": "Dasar%20AI.png", "title": "Artificial Intelligence"},
        {"path": "Dasar%20SQL.png", "title": "Structured Query Language"},
        {"path": "Visualisasi%20Data.png", "title": "Data Visualization"},
        {"path": "Memulai%20Pemrograman%20Python.png", "title": "Python Programming"},
        {"path": "Belajar%20Dasar%20Devops.png", "title": "DevOps"},
    ]
    
    cols = st.columns(3)
    for i, cert in enumerate(certificate_images):
        with cols[i % 3]:
            cert_url = base_url + cert["path"]
            cert_image = fetch_image_from_github(cert_url)
            st.image(cert_image, caption=cert["title"], use_column_width=True)

# Languages Tab
with tabs[5]:
    st.header("Languages")
    time.sleep(0.3) 
    st.write("""
    - Indonesian (Native)
    - English (Proficient)
    """)

# Skills Tab
with tabs[6]:
    time.sleep(0.2)
    st.header("Skills & Interest")

    skill_images = [
        "python.png",
        "judge.png",
        "oracle.png",
        "vscode.png",
        "github.png",
        "blender.png",
    ]
    
    cols = st.columns(6)
    for i, skill in enumerate(skill_images):
        with cols[i]:
            skill_url = base_url + skill
            skill_image = fetch_image_from_github(skill_url)
            st.image(skill_image)

# Contact Tab
with tabs[7]:
    st.header("Contact Me")
    time.sleep(0.3) 
    st.write("""
    Feel free to reach out through the following channels:
    
    - Email: [arisantofauzan@gmail.com](mailto:arisantofauzan@gmail.com)
    - LinkedIn: [Fauzan Arisanto](https://www.linkedin.com/in/fauzanarisanto/)
    - GitHub: [JurisDataNerd](https://github.com/JurisDataNerd)
    """)

# Footer
st.markdown("---")  
st.write(f"© {current_year} PrinceOfDarkness. All rights reserved.")
