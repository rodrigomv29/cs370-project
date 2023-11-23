import whisper
model = whisper.load_model("base")
result = model.transcribe("C:/Users/rodri/Documents/edu/njit/cs370/final_project/mp3/kamala-harris.mp3")
print(result["text"])

