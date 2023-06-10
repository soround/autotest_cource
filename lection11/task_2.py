# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import platform
from os import getenv
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:

    driver.get("https://fix-online.sbis.ru/")
    sleep(5)

    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(getenv("login") + Keys.ENTER)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(getenv("password") + Keys.ENTER)
    sleep(5)

    assert driver.current_url == "https://fix-online.sbis.ru/", 'Неверный адрес сайта'
    print("Авторизовались")

    sleep(5)

    accordion_contacts = driver.find_element(By.XPATH,
                                             '//*[@id="wasaby-content"]/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div/div/div/div[2]/a[1]/span[3]')
    accordion_contacts.click()
    sleep(1)
    contacts = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"] .NavigationPanels-SubMenu__headTitle')
    contacts.click()

    sleep(5)

    self_name = driver.find_element(By.CSS_SELECTOR,
                                    '[data-qa="Моя страница"] span[data-qa="NavigationPanels-Accordion__title"]').text
    add_btn = driver.find_element(By.CSS_SELECTOR, '[data-name="sabyPage-addButton"] .controls-icon')
    add_btn.click()
    sleep(5)

    search_input = driver.find_element(By.CSS_SELECTOR, '[templatename="Addressee/popup:Stack"] input')
    search_input.send_keys(self_name)
    search_input.send_keys(Keys.ENTER)

    sleep(5)

    myself = driver.find_element(By.CSS_SELECTOR, 'span[data-qa="person-Information__fio"]')
    myself.click()

    sleep(5)

    text_input = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    sleep(1)
    text_input.send_keys('Привет' + Keys.ENTER)

    driver.find_element(By.CSS_SELECTOR, '[title="Отправить"]').click()
    sleep(1)

    message_title = driver.find_element(By.CSS_SELECTOR,
                                        '.msg-dialogs-item__title [title="Тестирование Производительности"]')
    message_text = driver.find_element(By.CSS_SELECTOR, '.msg-entity-content_outgoing p')
    assert message_text.text == "Привет"
    assert message_text.is_displayed()

    print("Отправили сообщение самому себе")

    messages_count = len(driver.find_elements(By.CSS_SELECTOR, '.msg-entity-content_outgoing p'))

    sleep(5)
    actions = ActionChains(driver)
    actions.context_click(message_title)
    actions.perform()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, '[title="Перенести в удаленные"]').click()
    sleep(5)

    elements = driver.find_elements(By.CSS_SELECTOR, '.my-element')

    assert messages_count != len(driver.find_elements(By.CSS_SELECTOR, '.msg-entity-content_outgoing p'))
    print("Удалили сообщение")

except Exception as e:
    raise e
finally:
    driver.quit()
