🧩Análisis de E-Commerce con ChatGPT (LLMs + Excel)

🎯 PROPÓSITO

💡 Transformar datos reales de un e-commerce (desde Excel) en insights y decisiones.

 🎯 Meta final: decidir dónde invertir para aumentar ventas el próximo mes.

💻 1️⃣ CARGA Y EXPLORACIÓN DEL ARCHIVO

📂 Carga el Excel: → Clic en el ícono ➕ “Agregar archivo”. → Seleccioná tu reporte de ventas.

👁️ Vista previa automática:

Sheet productos 🧺
Sheet clientes 👥
Sheet transacciones 💸
🧮 Nota: ChatGPT ve valores calculados, no fórmulas. 📆 Ejemplo: una venta del 26-feb-2024 se clasifica en febrero.

🧠 2️⃣ ELECCIÓN DEL ROL

🎭 Define el enfoque con un “rol” en el prompt:

🧑‍💻 Analista de datos: explorar, resumir, detectar patrones.
🧬 Data scientist: calcular, limpiar, modelar, graficar.
💼 Experto en marketing/ventas: interpretar resultados y proponer acciones.
🗣️ Prompt base:

“Actúa como analista de datos. Lee el Excel y cuéntame qué encuentras.”

⚙️ 3️⃣ CÓMO RAZONA EL LLM

🧩 Proceso interno:

1️⃣ Entiende tu instrucción en lenguaje natural.

2️⃣ Genera código (Python/SQL).

3️⃣ Ejecuta el código y muestra resultados.

✅ Resultado: métricas exactas + gráficas precisas + interpretación.

📊 4️⃣ PEDÍ MÉTRICAS Y GRÁFICAS CORRECTAS

🎯 Sé concreto y detallado:

Métrica: revenue, ticket promedio, ventas por producto.
Origen: sheet transacciones.
Ejemplo de prompt: “Crea una gráfica de tendencia de ventas 2024 por revenue.”
⚠️ Revisá siempre: una tendencia por conteo ≠ una tendencia real de ventas.

⏸️ 5️⃣ SI EL ANÁLISIS SE DETIENE

😶 A veces el proceso se “pausa”.

✔️ Paso 1: clic en pausa.

🔄 Paso 2: clic en Try again.

➡️ GPT-5 reinicia y completa el análisis.
