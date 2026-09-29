import os
import time
import io
import sounddevice as sd
from scipy.io import wavfile
import speech_recognition as sr
import ollama
import pyttsx3



def listen_to_user(duration=4, fs=44100):
    """Records audio from microphone using sounddevice and processes it with SpeechRecognition."""
    print(f"\n🎤 Recording for {duration} seconds... Speak now!")
    
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  
    print("🤖 Processing speech...")

    wav_io = io.BytesIO()
    wavfile.write(wav_io, fs, recording)
    wav_io.seek(0)

    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_io) as source:
        audio_data = recognizer.record(source)
        try:
            user_text = recognizer.recognize_google(audio_data)
            print(f"👤 You said: {user_text}")
            return user_text
        except sr.UnknownValueError:
            print("❌ System could not understand the audio.")
            return None
        except sr.RequestError:
            print("❌ Speech service down.")
            return None

def generate_voice_assistant_response(prompt):
    """Sends text to your local Ollama instance for a fast, free offline response."""
    print("🧠 Local AI is thinking...")
    try:
        # Query your local open-source Llama model
        response = ollama.chat(
            model='llama3.2:1b',
            messages=[
                {
                    'role': 'system',
                    'content': 'You are a helpful conversational voice assistant. Keep answers brief, under 2 sentences.'
                },
                {
                    'role': 'user',
                    'content': prompt
                }
            ]
        )
        
        ai_text = response['message']['content']
        if ai_text:
            print(f"🤖 AI Answer: {ai_text}")
            print("🔊 Speaking...")
            
            # --- FIX: Initialize, speak, and close the engine freshly each time ---
            local_tts = pyttsx3.init()
            local_tts.setProperty('rate', 175)
            local_tts.say(ai_text)
            local_tts.runAndWait()
            del local_tts  # Safely clear the audio instance from memory
            # ---------------------------------------------------------------------
            
        else:
            print("🤖 AI replied, but text was empty.")
            
    except Exception as e:
        print(f"❌ Local Engine Error: {e}")

def main():
    print("=== 100% Free Offline Local AI Voice Assistant Initialized ===")
    while True:
        user_input = listen_to_user(duration=4)
        
        if user_input:
            if "exit" in user_input.lower() or "stop" in user_input.lower():
                print("Goodbye!")
                tts_engine = pyttsx3.init()
                tts_engine.setProperty('rate', 175) 
                tts_engine.say("Goodbye!")
                tts_engine.runAndWait()
                break
                
            generate_voice_assistant_response(user_input)
        
        time.sleep(1)

if __name__ == "__main__":
    main()
