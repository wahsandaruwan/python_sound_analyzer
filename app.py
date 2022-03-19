import recording
import mfcc

# Start recording
if(recording.record_sound()):
    # Print mfcc features
    print(mfcc.extract_mfcc())