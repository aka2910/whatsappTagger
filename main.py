import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':

    PATH = "chromedriver.exe"  # Location of the webdriver file
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(15)
    driver.get('https://web.whatsapp.com')
    groupName = input("Enter name of group: ")
    driver.find_element_by_css_selector("span[title='" + groupName + "']").click()
    time.sleep(4)
    n = len(driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[2]/span').text.split(',')) - 1
    print("participants", n + 1)

    inputStringAt = "@"
    initialString = "[@everyone {}] ".format(groupName)

    inputTextElement = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    inputTextElement.send_keys(initialString)
    inputTextElement.send_keys('\u200b' * 4000)

    newLineAction = ActionChains(driver).key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)
    newLineAction.perform()
    newLineAction.perform()
    inputTextElement.send_keys(inputStringAt)

    driver.implicitly_wait(15)
    elementList = driver.find_elements_by_class_name("_2zNFv")
    driver.implicitly_wait(15)
    start_time = time.time()
    for i in range(n):
        ActionChains(driver).send_keys(Keys.DOWN * i).send_keys(Keys.ENTER).perform()
        if i != n - 1:
            newLineAction.perform()
            newLineAction.perform()
            inputTextElement.send_keys(inputStringAt)
        print("progress =", round((i + 1) / n * 100, 2))
    print("time taken = {}s".format(round(time.time() - start_time, 2)))
