import os
from pydub import AudioSegment

def normalize_audio(audio_path, output_path):
    audio = AudioSegment.from_wav(audio_path)
    normalized_audio = audio.apply_gain(-audio.max_dBFS)
    normalized_audio.export(output_path, format="wav")

def batch_normalize_audio(audio_base_path):
    for root, dirs, files in os.walk(audio_base_path):
        for file in files:
            if file.endswith('.wav'):
                wav_path = os.path.join(root, file)
                normalized_path = os.path.splitext(wav_path)[0] + '_normalized.wav'
                normalize_audio(wav_path, normalized_path)
                print(f"Normalized {wav_path} to {normalized_path}")

if __name__ == "__main__":
    audio_base_path = 'data_set/LibriSpeech/dev-clean'
    batch_normalize_audio(audio_base_path)
