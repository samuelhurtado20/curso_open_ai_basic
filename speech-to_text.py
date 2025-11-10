from openai import OpenAI

client = OpenAI(api_key='tu_api_key')

# Convertir audio a texto
with open('speech.mp3', 'rb') as audio_file:
    transcript = client.audio.transcriptions.create(model='whisper-1', file=audio_file)
    print(transcript['text'])
