import webbrowser


def Buy():
    browser = webbrowser.Chrome()
    browser.get("https://www.taobao.com")
    browser.find_element_by_link_text("亲，请登录").click()
    print("请扫码")
    browser.get("https://cart.taobao.com/cart.htm")