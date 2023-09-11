import streamlit as st



st.markdown(
    """
    <style>
        .reportview-container {
            max-width: 100%;
            background-color: #f0f0f0;  # Adding a light background color
        }
        .main .block-container {
            max-width: 100%;
            padding: 20px;  # Adding some padding
        }
        h1 {
            color: #fffff;  # Styling the title color
            text-align: center;
        }
        p {
            font-size: 1.1em;  # Increasing the font size for paragraphs
        }
        ul {
            list-style-type: square;  # Changing the bullet style
        }
    </style>
    """,
    unsafe_allow_html=True,
)


st.title("📌 About")
st.write(
    """
   ##### <span style='color:#0b92be'>Data Analist</span>  📈 Bootcamp Final Project
    """
 , unsafe_allow_html=True
)
st.markdown('---')  # This will create a horizontal line


st.subheader("🔑Key Concepts:")

st.write(
    """
    ##### <span style='color:#0b92be'>Leads</span>
    <p>Refer to potential customers who have shown some level of interest in your product or service but have not yet made a purchase. They can originate from various sources such as marketing campaigns, social media, or referrals. The process of managing leads includes:
    <ul>
    <li><b>Acquisition:</b> Gathering leads from various sources.
    <li><b>Qualification:</b> Assessing leads based on their potential to become customers.
    <li><b>Scoring:</b> Ranking leads according to their likelihood of converting to a sale.
    <li><b>Nurturing:</b> Engaging leads with relevant information to encourage a purchase.
    <li><b>Conversion:</b> Turning leads into paying customers.
    </ul>
    """
    , unsafe_allow_html=True
)

st.subheader("🎯Lead Scoring:")
st.write(
    """

    <p>Lead scoring is a methodology used for ranking sales leads objectively. </p>
    <p>This process not only helps in aligning the appropriate follow-ups based on the inquiries but also assists marketing and sales professionals in identifying the stages prospects are at in the buying process.</p>
    <p>An integral aspect of this approach is the Intent Score, which signifies a lead's likelihood to make a purchase. 
    This score is derived from intent data, a collection of behaviors that indicate a lead's interest and engagement level.</p>
    
    #### Benefits of Lead Scoring:
    <ul>
    <li>Lead scoring facilitates a harmonized approach between sales and marketing teams.
    <li>Establishes a common language and framework to understand leads.
    <li>Helps pinpoint actual prospects, bridging gaps between marketing and sales efforts.
    <li>Results in numerous company benefits, including:
    <ul>
    <li>Improved Return on Investment (ROI)
    <li>Higher conversion rates
    <li>Increased sales productivity and effectiveness.
    </ul>
    </p>
    """
            , unsafe_allow_html=True
)


st.subheader("Database:")
st.write("""
    <p> The data used in this project was obtained from the following sources:
    <a href="https://www.kaggle.com/datasets/amritachatterjee09/lead-scoring-dataset" target="_blank"><b><i>link</i></b></a>
    </p>
    
         """
, unsafe_allow_html=True
)

    
