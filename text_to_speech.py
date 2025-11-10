from openai import OpenAI

client = OpenAI(api_key='tu_api_key')

# Generar audio a partir de texto
with client.audio.speech.stream() as response:
    response.tts('Aloy', input_text='Me despierto y hay nuevos avances en tecnología')
    with open('speech.mp3', 'wb') as f:
        f.write(response.content)
