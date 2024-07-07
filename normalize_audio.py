import os
from pydub import AudioSegment

def normalize_audio(audio_path, output_path):
    audio = AudioSegment.from_wav(audio_path)
    normalized_audio = audio.apply_gain(-audio.max_dBFS)
    normalized_audio.export(output_path, format="wav")

if __name__ == "__main__":
    audio_base_path = 'data_set/LibriSpeech/dev-clean'
    speakers = os.listdir(audio_base_path)
    
    for speaker in speakers[:5]:
        speaker_path = os.path.join(audio_base_path, speaker)
        chapters = os.listdir(speaker_path)
        for chapter in chapters[:2]:
            chapter_path = os.path.join(speaker_path, chapter)
            audio_files = [f for f in os.listdir(chapter_path) if f.endswith('.wav')]
            for audio_file in audio_files[:2]:
                wav_path = os.path.join(chapter_path, audio_file)
                normalized_path = os.path.splitext(wav_path)[0] + '_normalized.wav'
                normalize_audio(wav_path, normalized_path)
                print(f"Normalized {wav_path} to {normalized_path}")
