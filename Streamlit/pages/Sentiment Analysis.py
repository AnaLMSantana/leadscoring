from io import BytesIO
import pyaudio
import wave
import azure.cognitiveservices.speech as speechsdk
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import streamlit as st
import plotly.graph_objects as go

st.markdown(
    """
    <style>
        .reportview-container {
            max-width: 100%;
            text-align: center;  # This line centers all content
        }
        .main .block-container {
            max-width: 100%;
            text-align: center;  # This line centers all content
        }
    </style>
    """,
    unsafe_allow_html=True,
)

def azure_transcribe(subscription_key, region, record_seconds=5):
    # Audio Recording
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("Start Recording")

    frames = []
    for i in range(0, int(RATE / CHUNK * record_seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording Done")
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save audio data to a file instead of a BytesIO object
    with open('audio.wav', 'wb') as f:
        wf = wave.open(f, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    # Azure Transcription
    # Set up the Azure Speech SDK
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
    audio_input = speechsdk.audio.AudioConfig(filename='audio.wav')

    # Create a speech recognizer
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

    # Transcribe
    result = speech_recognizer.recognize_once()

    # Check the result
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        return "No speech could be recognized"
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        return "Speech Recognition canceled: {}. Error details: {}".format(cancellation_details.reason, cancellation_details.error_details)

def analyze_sentiment_scores(subscription_key, region, record_seconds=5, show_transcription=False):
    # Step 1: Record and transcribe the audio
    transcription = azure_transcribe(subscription_key, region, record_seconds)
    
    # Step 2: Perform sentiment analysis on the transcription
    MODEL = "cardiffnlp/twitter-roberta-base-sentiment"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    
    encoded_text = tokenizer(transcription, return_tensors='pt')
    output = model(**encoded_text)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    
    scores_dict = {
        'roberta_neg': scores[0],
        'roberta_neu': scores[1],
        'roberta_pos': scores[2]
    }
    
    # Calculate sentiment score
    sentiment_score = (scores_dict['roberta_neu'] + scores_dict['roberta_pos']) - scores_dict['roberta_neg']
    
    if scores_dict['roberta_neg'] > 0.8:
        sentiment_label = "Very bad"
    elif scores_dict['roberta_neg'] > scores_dict['roberta_pos']:
        sentiment_label = "Bad"
    elif scores_dict['roberta_neu'] > scores_dict['roberta_pos'] and scores_dict['roberta_neu'] > scores_dict['roberta_neg']:
        sentiment_label = "Neutral"
    elif scores_dict['roberta_pos'] > 0.8:
        sentiment_label = "Very good"
    else:
        sentiment_label = "Good"
    
    result_string = f"Transcription of the recorded text: {transcription}\nSentiment: {sentiment_label}" if show_transcription else f"Sentiment: {sentiment_label}"
    
    return transcription, sentiment_label, sentiment_score, scores_dict

# Streamlit UI
st.title('Lead Sentiment Analysis🔉')
st.markdown(
    """
    <style>
        .custom-subheader {
            font-size: 1.2em;
        }
        .highlight {
            color: #0b92be;
        }
    </style>
    <div class="custom-subheader">
        Click the button below to <span class="highlight">start recording</span> and analyse the sentiment.
    </div>
    """, 
    unsafe_allow_html=True
)
st.markdown("----------------------------------")
# Define your Azure subscription key and region
subscription_key = "efb37ac3f0224c9eb9e58b588686a83f"
region = "eastus"


# Add a selectbox to allow the user to choose if they want to see the transcription
# show_transcription = st.checkbox('Do you want to see the transcription?', [True, False])
show_transcription = st.sidebar.checkbox('Do you want to see the transcription?', value=True)

    
if st.button('Start Recording'):
    transcription, sentiment_label, sentiment_score, scores_dict = analyze_sentiment_scores(subscription_key, region, show_transcription=show_transcription)
    
    color_map = {
        "Very good": "green",
        "Good": "green",
        "Neutral": "orange",
        "Bad": "red",
        "Very bad": "red"
    }
    
    if show_transcription:
        st.markdown(f"**Transcription:** {transcription}")
    
    st.markdown(f"**Sentiment:** <span style='color: {color_map[sentiment_label]};'>{sentiment_label}</span>", unsafe_allow_html=True)
    st.markdown("----------------------------------")
    # Display sentiment score
    st.markdown(
    """
    <style>
        .centered {
            display: block;
            margin: 0 auto;
        }
    </style>
    """, 
    unsafe_allow_html=True,
    )
    st.subheader(f'Display sentiment score')
    fig = go.Figure(go.Indicator(
        mode="number+delta",
        value=sentiment_score,
        delta={"reference": 0.5},
        title={"text": "Sentiment Score"},))

    st.plotly_chart(fig)