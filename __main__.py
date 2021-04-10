import pyttsx3
import randfacts

# initiating pyttsx3 and setting properties
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

# saying the fact
engine.say(randfacts.getFact())

engine.runAndWait()
engine.stop()
