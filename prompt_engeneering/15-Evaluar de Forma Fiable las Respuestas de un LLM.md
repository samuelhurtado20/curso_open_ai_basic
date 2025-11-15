🧠Evaluar de Forma Fiable las Respuestas de un LLM

🎯 Objetivo

Automatizar sin errores midiendo la calidad de las respuestas de un modelo de lenguaje (LLM) con 4 criterios clave:

🔹 Consistencia

🔹 Precisión

🔹 Relevancia

🔹 Claridad

🧩 1. Decide el Tipo de Evaluación

⚖️ Dos enfoques principales:

1️⃣ Criterios propios → tú defines cómo medir la calidad.

2️⃣ Un LLM evalúa a otro LLM → solo si tienes criterios claros y objetivos definidos.

🧠 ¿Qué tipo de tarea tienes?

🔸 Tarea única → Ejemplo: consultar una ley.

🔸 Tarea recurrente → Ejemplo: redactar asuntos de correos semanales.

👉 En tareas recurrentes, la estabilidad del prompt es lo más importante.

✅ Recomendaciones

🕵️ Tareas únicas: validación puntual + revisión humana.
🔁 Tareas recurrentes: diseño sólido + pruebas repetidas + monitoreo continuo.
⚙️ 2. Los 4 Criterios para Evaluar un Prompt

🧭 A. CONSISTENCIA

📌 Prueba el prompt 10 veces con distintos contenidos.

📊 Evalúa si cubre todos los casos de uso.

🎯 Meta: alcanzar 10/10 antes de automatizar.

⚠️ Valida manualmente los resultados.

💡 Más consistencia = menos retrabajo.

🎯 B. PRECISIÓN

🔹 Secundaria en tareas creativas (cuentos, ideas).

🔹 Crítica en análisis de contenido, reportes o extracción de datos. 🧪 Cada modificación del prompt → probar con 10 ejemplos diferentes. 🔄 Confirmar consistencia antes de automatizar.

💡 La precisión define la confiabilidad.

🔍 C. RELEVANCIA

📌 El modelo debe enfocarse solo en lo pedido. 🚫 Evitar información irrelevante o divagaciones. 🔁 Repite la prueba 10 veces y revisa que responda al punto exacto.

💡 Evalúa si el modelo “va al grano”.

🗣️ D. CLARIDAD

📏 Respeta límites: longitud, tono, estilo y formato. 🧾 Comprueba que mantenga coherencia visual y textual. 🕒 Revisa el prompt cada semana.

⚠️ Los modelos cambian sin avisar (GPT-4, GPT-5, Opus, Sonnet…) 👀 Tu tarea: vigilar, ajustar y mantener el control.

🔄 3. Validación Cruzada entre Modelos (Gemini + ChatGPT)

💡 Objetivo: Reducir errores y alucinaciones comparando respuestas entre LLMs.

🧱 Ejemplo práctico: búsqueda legal

Tema: Custodia de la información en la Ley de Instituciones de Crédito.

🔹 Paso 1: En Gemini

📂 Carga los documentos.

⚖️ Indica que actúe como asistente legal.

📜 Pide que responda solo con base en los archivos adjuntos.

❌ Si no tiene datos, debe avisar. → Gemini responde: “No encuentra información”.

🔹 Paso 2: En ChatGPT

📥 Sube los mismos documentos.

✍️ Reformula sin ambigüedad:

“¿Existe alguna ley sobre custodia de la información?” ✅ ChatGPT confirma que sí y ubica la normativa. 📑 Ofrece extraer los artículos relevantes.

🔹 Paso 3: Vuelta a Gemini

📋 Pega la respuesta de ChatGPT.

📖 Pide que verifique la información comparándola con los artículos 124 y 79.

🔍 Gemini confirma que la información es correcta.

💬 Beneficios de la Validación Cruzada

✨ No depende de palabras literales.

🚨 Detecta alucinaciones o errores.

⏱️ Ahorra tiempo de lectura.

 🧰 Complementa (no reemplaza) técnicas de prompting restrictivas.
