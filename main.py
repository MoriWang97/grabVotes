# This is a sample Python script.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


import os
import openai

os.environ['OPENAI_API_KEY'] = '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'

def testOpenAiAPI():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Image.create(
        prompt="Young, short hair, girl with bangs, inner double, round face, innocent type, wearing glasses and white skirt",
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    #
    # response = openai.Completion.create(
    #     model="text-davinci-003",
    #     prompt='从前在一个村子里有个非常淘气的小男孩，他喜欢撒谎，他每天都会去山上放羊。有一天他觉得很没有意思，就想着捉弄村民找点乐子，于是他就大喊:"狼来了!狼来了!" 善良的村民们此时正在地里干活，听到小男孩的喊声，就扛着锄头跑着去救他了。可是他们到了小男孩放羊的那里，小男孩却说:"没有狼，我跟你们开玩笑的。"。这时候村民都很生气，回到田里继续干活。不一会，小男孩又大喊:狼来了!狼来了!"村民又回来了，却再次被小男孩欺骗没有狼。男孩开心地大笑，村民们说:"你撒谎骗我们，我们再也不会相信你了。"后来狼真的来了。男孩十分害怕。 "狼来了!狼来了!"他大声呼喊，"救命啊!救命!"但是村民没人来，后来这个淘气的男孩被狼吃了。 生成英文概要',
    #     temperature=0.9,
    #     max_tokens=150,
    #     top_p=1,
    #     frequency_penalty=0.0,
    #     presence_penalty=0.6,
    #     stop=[" Human:", " AI:"]
    # )
    print(image_url)

def Buy():
    browser = webdriver.Edge()
    browser.get("https://www.jd.com")
    time.sleep(3)
    browser.find_element(By.LINK_TEXT, "你好，请登录").click()
    print("请扫码")
    time.sleep(8)
    browser.get("https://cart.jd.com/cart_index")
    time.sleep(5)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Buy()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
