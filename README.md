# Speech Recognition System

This repository contains a comprehensive implementation of a speech recognition system using advanced data science methodologies. The system is designed to accurately convert speech to text by leveraging the LibriSpeech dataset, spectrogram analysis, and deep learning models including Hidden Markov Models (HMMs).

## Key Features

- **Audio File Upload**: Upload audio files through a Flask API for processing and recognition.
- **Feature Extraction**: Extract MFCC features from audio files for model training and recognition.
- **Hidden Markov Models**: Train and use HMMs for recognizing and matching audio files.
- **Real-time Application**: Optimized for speed and efficiency to handle real-time audio recognition.
- **Robust Error Handling**: Comprehensive error handling to ensure reliability and robustness.
- **Compatibility**: Supports diverse speech patterns and languages.

## Directory Structure
speech-recognition-system/
├── app.py
├── convert_audio.py
├── explore_audio.py
├── extract_features.py
├── normalize_audio.py
├── train_hmm.py
├── uploads/
├── models/
│ ├── hmm_models.pkl
│ └── features.pkl
└── data_set/
    └── LibriSpeech/
        └── dev-clean/


## Getting Started

### Prerequisites

- Python 3.7+
- Required Python libraries: `flask`, `speechrecognition`, `librosa`, `numpy`, `hmmlearn`, `pydub`, `werkzeug`

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Er-rajas/speech-recognition-system.git
    cd speech-recognition-system
    ```

2. Install the required Python libraries:
    ```sh
    pip install -r requirements.txt
    ```

3. Download and place the LibriSpeech dataset in the `data_set/LibriSpeech/dev-clean` directory.

### Usage

1. **Convert Audio Files**:
    ```sh
    python convert_audio.py
    ```

2. **Explore Audio Files**:
    ```sh
    python explore_audio.py
    ```

3. **Normalize Audio Files**:
    ```sh
    python normalize_audio.py
    ```

4. **Extract Features**:
    ```sh
    python extract_features.py
    ```

5. **Train HMM Models**:
    ```sh
    python train_hmm.py
    ```

6. **Run the Flask Application**:
    ```sh
    python app.py
    ```

7. **Upload Audio Files**:
    - Use tools like Postman or `curl` to upload `.flac` files to the `/upload` endpoint.

    Example using `curl`:
    ```sh
    curl -X POST -F 'file=@path/to/your/audio.flac' http://127.0.0.1:5000/upload
    ```

## Example Output

Upon uploading an audio file, the API will return a JSON response with the recognized text and the best match from the dataset, if any:

```json
{
  "status": "Speech recognized successfully.",
  "recognized_text": "example of recognized speech",
  
  
}
```
## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.


---

This `README.md` provides a clear overview of the project, instructions for setup and usage, and example outputs to help users understand how to work with your speech recognition system. Feel free to modify it according to your specific needs.

