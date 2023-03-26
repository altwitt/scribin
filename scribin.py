import whisper
from datetime import date

# dd/mm/YY H:M:S
dt_string = date.today()
# whisper has multiple models that you can load as per size and requirements
model = whisper.load_model("medium.en")

# path to the audio file you want to transcribe
audio = "cold.webm"
cut_audio = audio.rsplit('.', 1)[0]
file_name = f'{dt_string}-cut_audio.txt'
result = model.transcribe(audio, fp16=False)

with open(file_name, 'a') as f:
    f.write(result["text"])
