import speech_recognition as sr

r = sr.Recognizer()
r.energy_threshold = 200  # 👈 lower value = more sensitive
r.dynamic_energy_threshold = True

print("Available microphones:")
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(index, name)

with sr.Microphone(device_index=5) as source:
    print("Calibrating...")
    r.adjust_for_ambient_noise(source, duration=2)
    print("Say something loudly...")
    audio = r.listen(source, phrase_time_limit=5)

print("Processing...")

try:
    text = r.recognize_google(audio)
    print("You said:", text)
except Exception as e:
    print("Error:", repr(e))