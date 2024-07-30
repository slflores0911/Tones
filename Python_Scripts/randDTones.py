from pydub import AudioSegment
from pydub.playback import play
import random
import os
from datetime import datetime

# Directory containing the audio files
audio_dir = "/Users/samanthaflores/Tones/D"
audio_files = ["D1.wav", "D2.wav", "D3.wav", "D4.wav", "D5.wav", "D6.wav", "D7.wav", "D8.wav"]

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
output_file_name = f"D_Scale{timestamp}.wav"

# Save the combined audio
combined.export(output_file_name, format="wav")

# Optionally play the combined sound
play(combined)

print(f"Saved randomized sounds to {output_file_name}")
