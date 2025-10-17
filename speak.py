from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import subprocess

load_dotenv()  # take environment variables

client = OpenAI()
speech_file_path = Path(__file__).parent / "say_cheese.wav"

curr_dir = Path(__file__).parent

audio_path = curr_dir / "audio"

# Take input from the user and generate speech
while True:
    user_input = input("Say: ")
    audio_prefix = user_input.strip().replace(" ", "_")[:4]
    print(f"Generating speech for: {user_input}")
    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="coral",
        input="Gosh. You're the prettiest flesh blob of H20 and Carbon that I've ever seen. Say cheese!",
        instructions="Speak in a cheerful and positive tone.",
        response_format="wav",
    ) as response:
        response.stream_to_file(speech_file_path)

    print(f"Speech saved to: {speech_file_path}")
    print(f"Playing speech...")

    subprocess.run(["aplay", str(speech_file_path)])
