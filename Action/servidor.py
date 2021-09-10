import pandas as pd
import time
import requests
import wget
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

enlace = "https://testhector.users.earthengine.app/view/enginepoligonos"

def getDriver(enlace):
    
    options = Options()
    options.log.level = "trace"
    options.add_argument("--headless")
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")
    driver = webdriver.Firefox(options=options)
    driver.set_page_load_timeout("60")
    driver.get(enlace)

    return driver

def descargarDatos(url, r1, r2):
    driver = getDriver(url)
    # driver.refresh()
    driver.set_page_load_timeout("30")
    
    c = 0
    i = 0
    
    while(c == 0):
        try:
            file = driver.find_element_by_xpath("/html/body/main/div/div[1]/div/div/div/div/div/div/div[5]/div/div/div/a")
            print(file.text)
            c = 1
            print("Descargando...")
            i = 0
            
        except:
            print("Cargando...")
            time.sleep(10)
            c = 0
            i = i + 1
            
    url = file.text
    driver.close()
    
    myfile = requests.get(url)
    open('Files/' + str(r1) + ' - ' + str(r2) + '.csv', 'wb').write(myfile.content)
    
def descarga():

    r1 = 0
    r2 = 500
        
    for i in range(10):

        url = enlace + "?rango1=" + str(r1) + "&rango2=" + str(r2)
        print(url)
        
        descargarDatos(url, r1, r2)
        
        r1 = r2 + 1
        r2 += 500

if __name__ == '__main__':
    descarga()
