import speaker_verification_toolkit.tools as svt
import librosa

# Function for extrating mfcc features
def extract_mfcc():
    # Load the sound clip 
    data, cps = librosa.load('sound.wav', sr=None, mono=False)
    # Cut off silence parts from the signal audio data
    data = svt.rms_silence_filter(data)
    # Compute MFCC features from an audio signal
    data = svt.extract_mfcc(data, cps)
    return data