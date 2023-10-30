import openai
import requests
import json

def gpt(messages):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=[{
            "name": "flower",
            "description": "주어진 상황에 어울리는 꽃다발 추천하기",
            "parameters": {
                "type": "object",
                "properties": {
                    "flower": {
                        "type": "string",
                        "description": "주어진 상황에 어울리는 꽃다발을 만들 꽃을 최소 3가지 추천해줘",
                    },
                    "reason": {
                        "type": "string",
                        "description": "주어진 상황에 어울리는 꽃 추천 이유",
                    },
                    "card_message": {
                        "type": "string",
                        "description": "주어진 상황에 어울리는 간단한 카드 메세지",
                    },
                },
                "required": ["flower", "reason", "card_message"],
            },
        }]
    )

    message = completion["choices"][0]["message"]
    try:
        assistant_content = completion.choices[0].message["function_call"]["arguments"]
    except:
        print("function_call 없음")
        print(message)
        assistant_content = message["content"].strip()

    return(assistant_content)