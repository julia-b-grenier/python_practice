def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()

def ask(lvl_voice,text):
    print(lvl_voice(text))
    
ask(shout, "Why?")

ask(whisper, "Why?")