import os
import pickle
import numpy as np
from hmmlearn import hmm

def train_hmm(features_dict):
    models = {}
    
    for audio_path, mfccs in features_dict.items():
        model = hmm.GaussianHMM(n_components=5, covariance_type='diag', n_iter=1000)
        model.fit(mfccs.T)  # Transpose to fit the shape (n_samples, n_features)
        models[audio_path] = model
    
    return models

if __name__ == "__main__":
    os.makedirs('models', exist_ok=True)
    features_path = os.path.join('models', 'features.pkl')
    models_path = os.path.join('models', 'hmm_models.pkl')
    
    with open(features_path, 'rb') as f:
        features_dict = pickle.load(f)
    
    hmm_models = train_hmm(features_dict)
    
    with open(models_path, 'wb') as f:
        pickle.dump(hmm_models, f)
    print(f"Trained HMM models and saved to {models_path}")
