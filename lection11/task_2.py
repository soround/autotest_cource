# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from os import getenv
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:

    driver.get("https://fix-online.sbis.ru/")
    sleep(1)
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(getenv("login") + Keys.ENTER)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(getenv("password") + Keys.ENTER)
    sleep(5)

    assert driver.current_url == "https://fix-online.sbis.ru/", 'Неверный адрес сайта'
    print("Авторизовались")

    sleep(1)

    accordion_contacts = driver.find_element(By.CSS_SELECTOR, 'a[href="/page/dialogs"]')
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

    sleep(1)

    myself = driver.find_element(By.CSS_SELECTOR, 'span[data-qa="person-Information__fio"]')
    myself.click()

    sleep(1)

    text_input = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    sleep(1)

    user_message = 'Привет'

    text_input.send_keys(user_message + Keys.ENTER)
    driver.find_element(By.CSS_SELECTOR, '[title="Отправить"]').click()
    sleep(1)

    message_title = driver.find_element(By.CSS_SELECTOR,
                                        '.msg-dialogs-item__title [title="Тестирование Производительности"]')
    message_text = driver.find_element(By.CSS_SELECTOR, '.msg-entity-content_outgoing p')
    assert message_text.text == user_message
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
