from googletrans import Translator
import requests
from flask import current_app
from flask_babel import _


def translat(text, source_language, dest_language):
   
    trans=Translator()
    body=text
    translated=trans.translate(body,src=source_language, dest=dest_language)
    return  translated.text