# akhbaar padhke sunao

from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice")

# speak.Speak("aditya, ik, chutiya, insaan, hey")
speak.Speak("how does one spell nutella?")