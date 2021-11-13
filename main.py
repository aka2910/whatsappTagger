import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

if __name__ == '__main__':

    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    driver.get('https://web.whatsapp.com')
    while True:
        groupName = input("Enter name of group: ")
        search_box = WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')))
        search_box.clear()
        search_box.send_keys(groupName)
        search_box.send_keys(Keys.ENTER)

        WebDriverWait(driver, 6).until(ec.text_to_be_present_in_element
                                       ((By.XPATH, '//*[@id="main"]/header/div[2]/div[2]/span'), ','))

        members = driver.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div[2]/span').text.split(', ')

        n = len(driver.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div[2]/span').text.split(', ')) - 1

        print("participants", n + 1)
        initialHeader = f"[@everyone {groupName}]"
        inputTextElement = WebDriverWait(driver, 6).until(ec.presence_of_element_located(
            (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')))
        inputTextElement.send_keys(initialHeader)
        inputTextElement.send_keys('\u200b' * 4000)

        ActionChains(driver).key_down(Keys.LEFT_SHIFT).send_keys(Keys.ENTER, Keys.ENTER).key_up(Keys.LEFT_SHIFT).perform()
        inputTextElement.send_keys('@')
        start_time = time.time()
        for i in range(n):
            # ActionChains(driver).send_keys(Keys.DOWN * i).send_keys(Keys.ENTER).perform()
            inputTextElement.send_keys(members[i])
            inputTextElement.send_keys(Keys.TAB)
            if i != n - 1:
                # newLineAction.perform()
                ActionChains(driver).key_down(Keys.LEFT_SHIFT).send_keys(Keys.ENTER).key_up(
                    Keys.LEFT_SHIFT).perform()
                inputTextElement.send_keys('\u200F', '\u200E')
                inputTextElement.send_keys('@')
            print("progress =", round((i + 1) / n * 100, 2))
        print("time taken = {}s".format(round(time.time() - start_time, 2)))
