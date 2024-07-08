import os
import librosa
import numpy as np
import pickle

def extract_features(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return mfccs

if __name__ == "__main__":
    audio_base_path = 'data_set/LibriSpeech/dev-clean'
    speakers = os.listdir(audio_base_path)
    
    features_dict = {}
    
    for speaker in speakers:
        speaker_path = os.path.join(audio_base_path, speaker)
        chapters = os.listdir(speaker_path)
        for chapter in chapters:
            chapter_path = os.path.join(speaker_path, chapter)
            audio_files = [f for f in os.listdir(chapter_path) if f.endswith('_normalized.wav')]
            for audio_file in audio_files:
                normalized_path = os.path.join(chapter_path, audio_file)
                mfccs = extract_features(normalized_path)
                features_dict[normalized_path] = mfccs
    
    os.makedirs('models', exist_ok=True)
    features_path = os.path.join('models', 'features.pkl')
    with open(features_path, 'wb') as f:
        pickle.dump(features_dict, f)
    print(f"Extracted features and saved to {features_path}")
