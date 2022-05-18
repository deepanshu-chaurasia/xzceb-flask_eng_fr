import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ["apikey"]
url = os.environ["url"]
print(apikey)
print(url)

# Translator Instance and Authentication
authenticator = IAMAuthenticator("55cG3hhvVqEUFhRjrymHkYaw6RzvobpVLXA6FY8IDpYv")
language_translator = LanguageTranslatorV3(version = "2018-05-01", authenticator = authenticator)
language_translator.set_service_url("https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/edb5e844-e53c-4094-ad92-a35e080fcc4e")

def english_to_french(english_text):
    """
    Translate English to French
    """

    translation = language_translator.translate(text = english_text, model_id = "en-fr").get_result()
    french_text = translation["translations"][0]["translation"]
    return french_text

def french_to_english(french_text):
    """
    Translates French to English
    """

    translation = language_translator.translate(text = french_text, model_id = "fr-en").get_result()
    english_text = translation["translations"][0]["translation"]
    return english_text