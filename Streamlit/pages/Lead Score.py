import streamlit as st
from sklearn.preprocessing import normalize
import pickle
import numpy as np
import time
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataframe
df_test_csv = pd.read_csv(r'C:\Users\Ana\OneDrive\Documents\Ironhack\Week 9\Final Project\Lead Score\Dataset\test.csv')  

st.markdown(
    """
    <style>
        .reportview-container {
            max-width: 100%;
        }
        .main .block-container {
            max-width: 100%;
        }
    </style>
    """,
    unsafe_allow_html=True,
)



st.title("Lead Conversion Prediction✨")

st.markdown(
    """
    <style>
        .custom-subheader {
            font-size: 1.2em;  # Adjust the font size as needed
        }
        .highlight {
            color: #0b92be;  # Adjust the color as needed
        }
    </style>
    <div class="custom-subheader">
        Fill in the following fields with <span class="highlight">information</span> about your lead:
    </div>
    """, 
    unsafe_allow_html=True
)
st.markdown("<br><br>", unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)

def get_model():
    # Ensure that the pickle file is uploaded and specify the correct path here
    return pickle.load(open(r'C:\Users\Ana\OneDrive\Documents\Ironhack\Week 9\Final Project\Lead Score\Dataset\final_model2.pkl', 'rb'))

model = get_model()

def get_prediction(features):
    features_reshaped = np.array(features).reshape(1, -1)
    run_model = model.predict(features_reshaped)
    prediction_probabilities = model.predict_proba(features_reshaped)
    return run_model, prediction_probabilities


with col1:
    email = st.selectbox("Want to receive emails?", options=[0, 1], help="0 for No and 1 for Yes")
    total_visits = st.slider("Total Visits", 0, 20)
    time_on_site = st.slider("Total Time Spent on Website (seconds)", 0, 2207)
    pages_views = st.slider("Page Views Per Visit (average)", 0.0, 7.5)

with col2:
    free_copy = st.selectbox('Free Copy', options=[0, 1], help="0 for No and 1 for Yes")
    lead_origin = st.selectbox('Lead Origin', options=["Landing Page", "Lead add", "Lead import", "Add Form"])
    lead_source = st.selectbox('Lead Source', options=["Facebook", "Google", "Chat", "Organic Search", "Other", "Reference", "Referral Sites", "Website"])

with col3:
    last_activity = st.selectbox('Last Activity', options=["Email Bounced", "Email Link Clicked", "Email Opened", "Form Submitted on Website", "Olark Chat Conversation", "Others", "Page Visited on Website", "SMS Sent"])
    especialization = st.selectbox('Specialization', options=["Business Administration", "E-Business", "E-COMMERCE", "Finance Management", "Healthcare Management", "Hospitality Management", "Human Resource Management", "IT Projects Management", "International Business", "Marketing Management", "Media and Advertising", "Operations Management", "Others", "Retail Management", "Rural and Agribusiness", "Services Excellence", "Supply Chain Management", "Travel and Tourism"])
    occupation = st.selectbox('Occupation', options=["Housewife", "Other", "Student", "Unemployed", "Working Professional"])

lead_origin_array=[]
if lead_origin == "Landing Page":
    lead_origin_array += [1,0,0,0]
elif lead_origin == "Lead add":
    lead_origin_array += [0,1,0,0]
elif lead_origin == "Lead import":
    lead_origin_array += [0,0,1,0]
elif lead_origin == "Add Form":
    lead_origin_array += [0,0,0,1]

lead_source_array=[]
if lead_source == "Facebook":
    lead_source_array += [1,0,0,0,0,0,0,0]
elif lead_source == "Google":
    lead_source_array += [0,1,0,0,0,0,0,0]
elif lead_source == "Chat":
    lead_source_array += [0,0,1,0,0,0,0,0]
elif lead_source == "Organic Search":
    lead_source_array += [0,0,0,1,0,0,0,0]
elif lead_source == "Other":
    lead_source_array += [0,0,0,0,1,0,0,0]
elif lead_source == "Reference":
    lead_source_array += [0,0,0,0,0,1,0,0]
elif lead_source == "Referral Sites":
    lead_source_array += [0,0,0,0,0,0,1,0]
elif lead_source == "Website":
    lead_source_array += [0,0,0,0,0,0,0,1]
        
last_activity_array=[]
if last_activity == "Email Bounced":
    last_activity_array += [1,0,0,0,0,0,0,0]
elif last_activity == "Email Link Clicked":
    last_activity_array += [0,1,0,0,0,0,0,0]
elif last_activity == "Email Opened":
    last_activity_array += [0,0,1,0,0,0,0,0]
elif last_activity == "Form Submitted on Website":
    last_activity_array += [0,0,0,1,0,0,0,0]
elif last_activity == "Olark Chat Conversation":
    last_activity_array += [0,0,0,0,1,0,0,0]
elif last_activity == "Others":
    last_activity_array += [0,0,0,0,0,1,0,0]
elif last_activity == "Page Visited on Website":
    last_activity_array += [0,0,0,0,0,0,1,0]
elif last_activity == "SMS Sent":
    last_activity_array += [0,0,0,0,0,0,0,1]
    
especialization_array=[]        
if especialization == "Business Administration":
    especialization_array += [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
elif especialization == "E-Business":
    especialization_array += [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
elif especialization == "E-COMMERCE":
    especialization_array += [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
elif especialization == "Finance Management":
    especialization_array += [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
elif especialization == "Healthcare Management":
    especialization_array += [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
elif especialization == "Hospitality Management":
    especialization_array += [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
elif especialization == "Human Resource Management":
    especialization_array += [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
elif especialization == "IT Projects Management":
    especialization_array += [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
elif especialization == "International Business":
    especialization_array += [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
elif especialization == "Marketing Management":
    especialization_array += [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
elif especialization == "Media and Advertising":
    especialization_array += [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
elif especialization == "Operations Management":
    especialization_array += [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
elif especialization == "Others":
    especialization_array += [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
elif especialization == "Retail Management":
    especialization_array += [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
elif especialization == "Rural and Agribusiness":
    especialization_array += [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
elif especialization == "Services Excellence":
    especialization_array += [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
elif especialization == "Supply Chain Management":
    especialization_array += [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
elif especialization == "Travel and Tourism":
    especialization_array += [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
    
occupation_array=[]    
if occupation == "Housewife":
    occupation_array += [1,0,0,0,0]
elif occupation == "Other":
    occupation_array += [0,1,0,0,0]
elif occupation == "Student":
    occupation_array += [0,0,1,0,0]
elif occupation == "Unemployed":
    occupation_array += [0,0,0,1,0]
elif occupation == "Working Professional":
    occupation_array += [0,0,0,0,1]

features = [email, total_visits, time_on_site, pages_views, free_copy]
features.extend(lead_origin_array)
features.extend(lead_source_array)
features.extend(last_activity_array)
features.extend(especialization_array)
features.extend(occupation_array)

# Making Prediction
st.markdown('<style>div.row-widget.stButton{text-align: center;}</style>', unsafe_allow_html=True)
if st.button('Show Prediction :point_up_2:'):

    run_model, prediction_probabilities = get_prediction(features)
    
    if run_model[0] == 1:
        st.success('Probability of converting: High ✅')
        # st.write(f'Probability of conversion : {prediction_probabilities[0][1]*100:.2f}%')
    else:
        st.error('Probability of converting: Low ❌')
        # st.write(f'Probability of conversion : {prediction_probabilities[0][0]*100:.2f}%')

    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0)
    st.text(progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)  # Adjust the time as needed
        my_bar.progress(percent_complete + 1)
        

    # Displaying the score in a cool way
    st.subheader("➡️Prediction Result:")
    st.markdown(f"The lead has a {'<b style=color:green;>high</b>' if run_model[0] == 1 else '<b style=color:red;>low</b>'} chance of converting, with a probability of {max(prediction_probabilities[0])*100:.2f}%.", unsafe_allow_html=True)



st.sidebar.subheader("Get Leads with High Conversion Probability")
x = st.sidebar.number_input('Enter the number of records to fetch:', min_value=1, value=5)
if st.sidebar.button('Get Leads'):
    df_test_csv = df_test_csv.rename(columns={'prob_1': 'score'})  # Renaming 'prob_1' column to 'score'
    high_score_leads = df_test_csv[df_test_csv['score'] > 90].head(x)
    #drop "convertion" and prob_0 columns
    high_score_leads = high_score_leads.drop(['prob_0', 'Convertion'], axis=1)
    high_score_leads.drop('Unnamed: 0', axis=1, inplace=True)
    st.dataframe(high_score_leads)



