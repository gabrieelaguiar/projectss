from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep  
import re
import os


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1920,1080', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    return driver

try:
    driver = iniciar_driver()
    driver.get('https://lista.mercadolivre.com.br/tv#D[A:tv]')
    sleep(3)

    produtos = driver.find_elements(By.XPATH, '//*[@class="ui-search-item__title shops__item-title"]')
    precos = driver.find_elements(By.XPATH, '//*[@class="andes-money-amount ui-search-price__part shops__price-part ui-search-price__part--medium andes-money-amount--cents-superscript"]')

    with open('tvs.csv', 'a', encoding='utf-8', newline='') as arquivo:
        for produto, preco in zip(produtos, precos):
            valor_preco = re.search(r'(\d+)\sreais', preco.text).group(1)
            arquivo.write(f'{produto.text};{valor_preco}{os.linesep}')
except Exception as e:
    print(f"Ocorreu um erro: {e}")
finally:
    input("Fim")
