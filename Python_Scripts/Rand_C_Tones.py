from pydub import AudioSegment
from pydub.playback import play
import random
import os
from datetime import datetime

# Directory containing the audio files
audio_dir = "/Users/samanthaflores/Tones/C"
audio_files = ["C1.wav", "C2.wav", "C3.wav", "C4.wav", "C5.wav", "C6.wav", "C7.wav", "C8.wav"]

# Shuffle the list of audio files
random.shuffle(audio_files)

# Concatenate audio files
combined = AudioSegment.empty()
for file_name in audio_files:
    file_path = os.path.join(audio_dir, file_name)
    print(f"Trying to open: {file_path}")  # Debugging line
    if os.path.isfile(file_path):
        sound = AudioSegment.from_wav(file_path)
        combined += sound
    else:
        print(f"File not found: {file_path}")

# Generate a unique file name with a timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file_name = f"C_Scale{timestamp}.wav"

# Save the combined audio
combined.export(output_file_name, format="wav")

# Optionally play the combined sound
play(combined)

print(f"Saved randomized sounds to {output_file_name}")
