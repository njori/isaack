from googletrans import Translator

trans=Translator()
body="hello world"
translated=trans.translate(body,dest="es")
print(translated.text)