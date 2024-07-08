from flask import Flask, request, jsonify
import os
import speech_recognition as sr
from werkzeug.utils import secure_filename
import pickle
from hmmlearn import hmm
import librosa
import numpy as np

app = Flask(__name__)


upload_path = 'uploads/'


dataset_path = 'data_set/LibriSpeech/dev-clean'


os.makedirs(upload_path, exist_ok=True)

models_path = os.path.join('models', 'hmm_models.pkl')
with open(models_path, 'rb') as f:
    hmm_models = pickle.load(f)


def recognize_speech(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)  
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Web Speech API; {e}"

def extract_features(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return mfccs

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
        
        uploaded_filename = file.filename

        
        filename = secure_filename(uploaded_filename)  
        file_path = os.path.join(upload_path, filename)
        file.save(file_path)

       
        recognized_text = recognize_speech(file_path)

       
        match = match_with_hmm(file_path)

       
        response_data = {
            "status": "Speech recognized successfully.",
            "recognized_text": recognized_text,
            
        }
        return jsonify(response_data), 200

if __name__ == "__main__":
    app.run(debug=True)
