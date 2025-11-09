import os
from dotenv import load_dotenv
from openai import OpenAI
import base64

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

messages = [
    {
        "role": "system",
        "content": "Eres un asistente que analiza las imágenes a gran detalle."
    },
    {
        "role": "user",
        "content": [
            {
                "type": "input_text",
                "text": "Hola, ¿Puedes analizar esta imagen?"
            },
            {
                "type": "input_image",
                "image_url": f"data:image/png;base64,{encode_image_to_base64('./image.png')}"
            }
        ]
    }
]

response = client.responses.create(
    model="gpt-4o",
    input=messages
)

print("Respuesta del análisis de la imagen")
print(response.output_text)
