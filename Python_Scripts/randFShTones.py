from pydub import AudioSegment
from pydub.playback import play
import random
import os
from datetime import datetime

# Directory containing the audio files
audio_dir = "/Users/samanthaflores/Tones/FSh"
audio_files = ["FSh1.wav", "FSh2.wav", "FSh3.wav", "FSh4.wav", "FSh5.wav", "FSh6.wav", "FSh7.wav", "FSh8.wav"]

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
output_file_name = f"FSh_Scale{timestamp}.wav"

# Save the combined audio
combined.export(output_file_name, format="wav")

# Optionally play the combined sound
play(combined)

print(f"Saved randomized sounds to {output_file_name}")
