from flask import Flask, request, jsonify
import os
import speech_recognition as sr
from werkzeug.utils import secure_filename
import pickle
from hmmlearn import hmm
import librosa
import numpy as np

app = Flask(__name__)

# Path for file uploads
upload_path = 'uploads/'

# Path to your dataset
dataset_path = 'data_set/LibriSpeech/dev-clean'

# Ensure upload directory exists
os.makedirs(upload_path, exist_ok=True)

# Load HMM models
models_path = os.path.join('models', 'hmm_models.pkl')
with open(models_path, 'rb') as f:
    hmm_models = pickle.load(f)

# Function to perform speech recognition
def recognize_speech(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)  # Record the audio from the file
    try:
        # Use Google Web Speech API to perform recognition
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Web Speech API; {e}"

# Function to extract features
def extract_features(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return mfccs

# Function to match recognized text with HMM models
def match_with_hmm(audio_path):
    best_match = None
    best_score = float('-inf')
    
    mfccs = extract_features(audio_path)
    
    print(f"Extracted MFCCs for {audio_path}: {mfccs.shape}")
    
    for model_path, model in hmm_models.items():
        try:
            score = model.score(mfccs.T)
            print(f"Score for model {model_path}: {score}")
            if score > best_score:
                best_score = score
                best_match = model_path
        except Exception as e:
            print(f"Error scoring model {model_path}: {e}")
    
    print(f"Best match: {best_match} with score {best_score}")
    return best_match

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        # Get the filename of the uploaded file
        uploaded_filename = file.filename

        # Save the file to upload_path
        filename = secure_filename(uploaded_filename)  # Use secure_filename to sanitize the filename
        file_path = os.path.join(upload_path, filename)
        file.save(file_path)

        # Perform speech recognition on the uploaded file
        recognized_text = recognize_speech(file_path)

        # Check if recognized text matches any HMM model in the dataset
        match = match_with_hmm(file_path)

        # Respond with recognized text, match status, and file details
        response_data = {
            "status": "Speech recognized successfully.",
            "recognized_text": recognized_text,
            
        }
        return jsonify(response_data), 200

if __name__ == "__main__":
    app.run(debug=True)
