from selenium import common
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests, urllib3 

def login():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')

    browser = webdriver.Chrome(options=options)
    browser.get("https://net.cuc.edu.cn/")

    try:
        username_='xxx'
        password_='xxx'
        # 输入用户名,密码
        username = browser.find_element_by_xpath('//*[@id="username"]')
        password = browser.find_element_by_xpath('//*[@id="password"]')
        username.clear()
        username.send_keys(username_)
        password.clear()
        password.send_keys(password_)

        login_btn = browser.find_element_by_xpath('//*[@id="login-account"]')
        # login_btn.click()
        # 无头游览器时,CUC的版权信息会遮挡住loginbtn
        browser.execute_script('arguments[0].click()', login_btn)
        try:
            # 页面一直循环，直到 id="myDynamicElement" 出现
            element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="logout-dm"]'))
            )
            print('ok!')
        finally:
            browser.quit()
            send2bark()

    except common.exceptions.NoSuchElementException:
        browser.quit()
        return "认证已完成，无需再次认证"

    except common.exceptions.StaleElementReferenceException:
        # 这个错误一般是因为已经认证完成而导致的页面跳转发生的无法找到对应元素
        browser.quit()
        return "认证已完成，无需再次认证"

    except common.exceptions.TimeoutException:
        # 这个错误一般是由于网站经常会响应比较慢，或者还没加载完全就返回空白页，导致程序经常检测不到元素卡死
        # 可以修改此处，让程序重复执行或者放弃执行
        browser.quit()
        return "响应超时，放弃本次认证"

    browser.quit()

def send2bark():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    try:
        link = 'https://api.day.app/xxx/网络连接/网络已成功重连!'
        res = requests.get(link, verify=False)
    except Exception as e:
        print('Reason:', e)
        return
    return

if __name__ == '__main__':
    print(login())
    pass


