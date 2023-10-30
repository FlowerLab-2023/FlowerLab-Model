import openai
import json

my_openAI_key = 'key'
openai.api_key = my_openAI_key

from gpt_turbo import *
from json_parse import *
from translate import *
from dall_e_2 import *
from PIL import Image

# 상황 입력
prompt = input("꽃다발이 필요한 상황을 입력해주세요 : ")
messages = [{"role": "user", "content": prompt}]

# gpt한테 전달
text = gpt(messages)
#print(text)

# gpt출력값 파싱하기
flower_list, reason, card_message = parse(text)
print("꽃 종류 : ", flower_list)

flower_list = flower_list.split()
#print(flower_list)

# 꽃 종류 달리한테 전달하기 위해 번역
list = list()
for i in flower_list:
  t = trans(i)
  list.append(t)
#print(list)

flower = ', '.join(list)
#print(flower)

#달리한테 전송 / url받아서 이미지 보여주기 지금은 로컬이라 이렇게 해놨는데 웹에 바로 url전송해서 거기로 띄우면 될듯?
image_url = dalle(flower)
im = Image.open(requests.get(image_url, stream=True).raw)
im.show()

print("추천 이유 : ", reason)
print("카드 메세지 : ", card_message)