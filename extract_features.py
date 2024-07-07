import os
import librosa
import numpy as np

def extract_features(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mel_spectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
    return mfccs, mel_spectrogram

if __name__ == "__main__":
    audio_base_path = 'data_set/LibriSpeech/dev-clean'
    speakers = os.listdir(audio_base_path)
    
    for speaker in speakers[:5]:
        speaker_path = os.path.join(audio_base_path, speaker)
        chapters = os.listdir(speaker_path)
        for chapter in chapters[:2]:
            chapter_path = os.path.join(speaker_path, chapter)
            audio_files = [f for f in os.listdir(chapter_path) if f.endswith('_normalized.wav')]
            for audio_file in audio_files[:2]:
                normalized_path = os.path.join(chapter_path, audio_file)
                mfccs, mel_spectrogram = extract_features(normalized_path)
                print(f"Extracted MFCCs and Mel spectrogram from {normalized_path}")
