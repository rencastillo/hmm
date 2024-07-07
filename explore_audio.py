import os
from pydub import AudioSegment

def explore_librispeech_files(audio_base_path):
    speakers = os.listdir(audio_base_path)
    for speaker in speakers[:5]:  # Just sample 5 speakers
        speaker_path = os.path.join(audio_base_path, speaker)
        chapters = os.listdir(speaker_path)
        for chapter in chapters[:2]:  # Just sample 2 chapters per speaker
            chapter_path = os.path.join(speaker_path, chapter)
            audio_files = [f for f in os.listdir(chapter_path) if f.endswith('.flac')]
            for audio_file in audio_files[:2]:  # Just sample 2 files per chapter
                audio_path = os.path.join(chapter_path, audio_file)
                audio = AudioSegment.from_file(audio_path, format="flac")
                print(f"Loaded {audio_file}, Duration: {audio.duration_seconds} seconds")

if __name__ == "__main__":
    audio_base_path = 'data_set/LibriSpeech/dev-clean'
    explore_librispeech_files(audio_base_path)

