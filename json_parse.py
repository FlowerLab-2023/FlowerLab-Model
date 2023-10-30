import openai
import requests
import json

def parse(text):
    result = json.loads(text)

    flower_list = result.get("flower")
    reason = result.get("reason")
    card_message = result.get("card_message")

    return flower_list, reason, card_message