from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\Programming\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")


def main():
    driver.implicitly_wait(5)

    Counter = driver.find_element_by_id("cookies")
    cookie = driver.find_element_by_id("bigCookie")
    storePrices = [driver.find_element_by_id("productPrice" + str(i)) for i in range(5)]

    actions = ActionChains(driver)
    actions.click(cookie)

    while 1:
        for i in range(6):
            actions.perform()
            try:
                if int(Counter.text.split(' ')[0]) > int(storePrices[i].text):
                    upgrade_action = ActionChains(driver)
                    upgrade_action.move_to_element(driver.find_element_by_id("product" + str(i)))
                    upgrade_action.click()
                    upgrade_action.perform()
            except:
                pass


main()