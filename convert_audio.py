import os
from pydub import AudioSegment

def convert_flac_to_wav(flac_path, wav_path):
    audio = AudioSegment.from_file(flac_path, format="flac")
    audio.export(wav_path, format="wav")

if __name__ == "__main__":
    audio_base_path = 'data_set\LibriSpeech\dev-clean'
    speakers = os.listdir(audio_base_path)
    
    for speaker in speakers[:5]:
        speaker_path = os.path.join(audio_base_path, speaker)
        chapters = os.listdir(speaker_path)
        for chapter in chapters[:2]:
            chapter_path = os.path.join(speaker_path, chapter)
            audio_files = [f for f in os.listdir(chapter_path) if f.endswith('.flac')]
            for audio_file in audio_files[:2]:
                flac_path = os.path.join(chapter_path, audio_file)
                wav_path = os.path.splitext(flac_path)[0] + '.wav'
                convert_flac_to_wav(flac_path, wav_path)
                print(f"Converted {flac_path} to {wav_path}")
