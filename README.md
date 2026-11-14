# TP de AI Engineering — Extracción de información técnica

El pipeline recibe un log o una descripción de arquitectura y devuelve un objeto
Pydantic con las tecnologías mencionadas, la criticidad y un resumen en español.

## Ejecutar en PowerShell

Con Python 3.10 o superior, desde esta carpeta:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Completá `OPENAI_API_KEY` en tu copia local de `.env`. Podés configurar
`OPENAI_MODEL` si usás otro modelo compatible con el modo JSON.

```powershell
.\.venv\Scripts\python.exe demo.py
```

## Cómo funciona

1. `schemas.py` define el contrato de salida. El nivel puede ser `baja`,
   `media`, `alta` o `indeterminada` si falta evidencia.
2. `chain.py` encadena el prompt y el modelo con `with_structured_output`.
   El modo JSON deja que LangChain y Pydantic comprueben el resultado.
3. `process_text` ejecuta la cadena con `ainvoke`. Ante un error de parseo
   o validación, `with_retry` vuelve a ejecutar la cadena hasta un máximo de
   tres intentos totales. Los logs indican el resultado de cada intento.
4. `demo.py` ejecuta un ejemplo y muestra el JSON validado.
