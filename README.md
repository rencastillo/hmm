# HMM - Sistema de reconocimiento de voz

Este repositorio contiene una implementación de un sistema de **reconocimiento de voz a texto** utilizando **Modelos Ocultos de Markov (HMM)**.
El proyecto está enfocado únicamente en el uso de HMM para procesar archivos de audio en formato `.flac` y generar la transcripción en texto.

## Requisitos

* Python 3.7+
* Librerías necesarias: `flask`, `speechrecognition`, `librosa`, `numpy`, `hmmlearn`, `pydub`, `werkzeug`

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

## Uso

1. Ejecuta la aplicación Flask:

```bash
python app.py
```

2. Sube un archivo de audio en formato `.flac` al endpoint `/upload`.
   Puedes usar herramientas como `curl` o Postman.

Ejemplo con `curl`:

```bash
curl -X POST -F 'file=@ruta/a/tu/audio.flac' http://127.0.0.1:5000/upload
```

3. El sistema procesará el audio con HMM y devolverá un JSON con el texto reconocido.

### Ejemplo de salida

```json
{
  "status": "Reconocimiento exitoso.",
  "recognized_text": "ejemplo de transcripción"
}
```

## Estructura del repositorio

```
hmm/
├── app.py                # API principal en Flask
├── train_hmm.py          # Entrenamiento del modelo HMM
├── extract_features.py   # Extracción de características (MFCC)
├── models/               # Modelos HMM entrenados
├── uploads/              # Archivos de audio subidos
└── requirements.txt
```

---
