# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:

    site = "https://sbis.ru/"
    driver.maximize_window()
    driver.get(site)

    sleep(1)

    contacts = driver.find_element(By.LINK_TEXT, "Контакты")
    contacts.click()
    sleep(1)

    logo = driver.find_element(By.CSS_SELECTOR, '[title="tensor.ru"]')
    logo.click()
    driver.switch_to.window(driver.window_handles[-1])
    sleep(5)

    news_block = driver.find_element(By.CSS_SELECTOR, ".tensor_ru-Index__block4-content > .tensor_ru-Index__card-title")

    assert news_block.is_displayed(), 'Блока нет на странице'
    assert news_block.text == "Сила в людях"

    about_lnk = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg .tensor_ru-link')
    if news_block.location_once_scrolled_into_view:
        about_lnk.click()

    assert driver.current_url == "https://tensor.ru/about"

except AssertionError as e:
    raise e
except Exception as e:
    print(e)
finally:
    driver.quit()
