import streamlit as st
from PIL import Image
from st_pages import Page, add_page_title, show_pages

# Declarando as páginas no seu app:
show_pages(
    [
        Page("Home.py", "Home", "🏠"),
        Page("pages\About.py", "About", "📌"),
        Page("pages\Lead Score.py", "Lead Score", "📈"),
        Page("pages\Sentiment Analysis.py", "Sentiment Analysis", "💟"),        
    ]
)

# add_page_title()  # Método opcional para adicionar título e ícone à página atual


st.markdown(
    """
    <style>
        .welcome-text {
            font-size: 2.5em; 
            color: #01052d; 
            font-weight: bold; 
            margin-bottom: 0px; 
            text-align: center; 
        }
        .subheader-text {
            font-size: 1.1em; 
            color: #01052d; 
            font-weight: normal; 
            margin-bottom: 20px; 
            text-align: center; 
        }
        .highlight-text {
            color: #0b92be; 
        }
    </style>
    <div class="welcome-text">
        Welcome to Score.it ✨
    </div>
    <div class="subheader-text">
        The Lead Score App that helps you to 
        <span class="highlight-text">connect with your customers</span>
    </div>
    """, 
    unsafe_allow_html=True
)
st.markdown("<br><br>", unsafe_allow_html=True)


# Space for Logo (Replace 'path/to/your/logo.png' with the actual path to your logo)
img = Image.open(r'C:\Users\Ana\OneDrive\Documents\Ironhack\Week 9\Final Project\Streamlit\Images\logo_h.png')
st.image(img, use_column_width=False, width=700)
st.markdown("<br><br>", unsafe_allow_html=True)


st.markdown(
    """
    <style>
        .feature-section {
            display: flex;
            justify-content: space-between;
            margin-bottom: 30px;
        }
        .feature-rectangle {
            background-color: #0b92be; /* Background color for the rectangles */
            padding: 20px;
            width: 45%; /* Adjust width as necessary */
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Optional: Adding a shadow effect */
            color: white; /* Making the rest of the text white */
        }
        .feature-rectangle a {
            color: #01052d; /* Color for the links */
            text-decoration: underline;
            display: block; /* Makes the link occupy the whole line */
            margin-top: 10px; /* Adds some space above the link */
        }
        .feature-title {
            color: #ffd12e; /* Color for the titles */
            font-weight: bold; /* Making the titles bold */
        }
    </style>
    <div class="feature-section">
        <div class="feature-rectangle">
            <span class="feature-title">🎯Lead Score:</span> Based on your lead profile, you will get a score that indicates the probability of conversion.
        </div>
        <div class="feature-rectangle">
            <span class="feature-title">💛Sentiment Analysis:</span> After contact with the lead, its possible to analyse the consumer sentiment about this contact.
        </div>
    </div>
    """, 
    unsafe_allow_html=True
)


st.subheader("Description:")
st.markdown(
    """
    <div style="text-align: justify;"> 
    <p style="text-indent: 1em;"><b>Score.</b><b><i>it</i></b> is an intelligent tool designed to calculate lead scores for potential customers based on their activity attributes and intentions.
    
    <p style="text-indent: 1em;"> By utilizing machine learning techniques, I have developed a model that aims to maximize profits. 
    </div>
    """, 
    unsafe_allow_html=True
)

    
c1, c2, c3 = st.columns(3)
with c1:
   st.info('**Email: [@click to send](mailto:ola@anasantana.pt)**', icon="📥")
with c2:
    st.info('**GitHub: [@check here](https://github.com/AnaLMSantana)**', icon="👩‍💻")
with c3:
    st.info('**Linkedin: [My profile](https://www.linkedin.com/in/ana-r-santana/)**',icon="🔍")



