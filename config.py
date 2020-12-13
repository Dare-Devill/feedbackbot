import os

class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
      API_ID = int(os.environ.get("API_ID", 12345))
      API_HASH = os.environ.get("API_HASH" , "")
      OWNER = [os.environ.get("OWNER_ID",  "@pratham_vai")]
      PASS = os.environ.get("PASSWORD", "mishra")
      RULES = os.environ.get("RULES", "")
      START = os.environ.get("START", "I am a feedback bot for Pratham. you can send feed back or ask for pm in this bot.")
      SEND = []
      LOGIN = []
      feedback = []
