import whisper
import datetime

model = whisper.load_model('base')

# guarda antes de la transcripción
t1 = datetime.datetime.now()
print(f"started at {t1}")

audio_file = ''
# hace la transcripción
output = model.transcribe(audio_file)

# muestra cuando cuando se completó y cuanto demoró
t2 = datetime.datetime.now()
print(f"ended at {t2}")
print(f"time elapsed: {t2 - t1}")


for segment in output['segments']:
  print(segment)
  second = int(segment['start'])
  second = second - (second % 5)
  print(second)