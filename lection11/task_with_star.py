# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def get_current_work_directory() -> str:
    return str(Path.cwd())


def convert_bytes(size):
    """ Convert bytes to KB, or MB or GB"""
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0


options = Options()
options.add_experimental_option("prefs", {
    "download.default_directory": get_current_work_directory(),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
})

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://sbis.ru/")
    sleep(5)
    footer = driver.find_element(By.CSS_SELECTOR, '.sbisru-Footer')
    driver.execute_script("return arguments[0].scrollIntoView(true);", footer)
    download_sbis = driver.find_element(By.LINK_TEXT, 'Скачать СБИС')
    download_sbis.click()
    sleep(5)
    plugin_link = driver.find_element(By.CSS_SELECTOR, 'div[data-id="plugin"]')
    plugin_link.click()

    # platform_name = platform.system()
    platform_name = "Windows"

    match platform_name:
        case "Darwin":
            tab_selector = 'div[data-id="macos"]'
            link_selector = 'a[href="https://update.sbis.ru/Sbis3Plugin/master/arm64/darwin/sbis3plugin-setup.pkg"]'
        case "Linux":
            tab_selector = 'div[data-id="linux"]'
            link_selector = 'a[href="https://update.sbis.ru/Sbis3Plugin/master/linux/sabyapps-setup"]'
        case _:
            tab_selector = '[data-for="plugin"] [sbisname="TabButtons"] div[data-id="default"]'
            link_selector = 'a[href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]'

    tab = driver.find_element(By.CSS_SELECTOR, tab_selector)
    tab.click()
    download_link = driver.find_element(By.CSS_SELECTOR, link_selector)
    download_link.click()

    sleep(5)

    file_path = Path('sbisplugin-setup-web.exe')

    assert file_path.is_file()
    print(f"Файл {file_path}  скачался")
    print(f"Файл {file_path} весит {convert_bytes(file_path.stat().st_size)}")


except Exception as e:
    print(e)
finally:
    driver.quit()
