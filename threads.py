import openai

client = openai.Client(api_key='your-api-key')
assistant_id = 'your-assistant-id'

# Creación del hilo
thread = client.beta.threads.create(
    assistant_id=assistant_id
)

thread_id = thread.id

# Agregar mensaje al hilo
client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content="¿Cuánto es 2+2?"
)

# Ejecutar el run
run = client.beta.threads.runs.create(
    thread_id=thread_id,
    assistant_id=assistant_id
)

# Esperar hasta que se complete el run
import time

while True:
    run_status = client.beta.threads.runs.get(
        thread_id=thread_id,
        run_id=run.id
    ).status

    if run_status == 'completed':
        break

    time.sleep(1)

# Recuperar pasos del run
steps = client.beta.threads.runs.steps.list(
    thread_id=thread_id,
    run_id=run.id
)

# Mostrar cada paso del código
for step in steps:
    if 'tool_calls' in step.details:
        for tool_call in step.details['tool_calls']:
            if tool_call['type'] == 'code_prompt':
                print("Código Python generado:")
                print(tool_call['input'])
