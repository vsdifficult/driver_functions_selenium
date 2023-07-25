from selenium import webdriver 
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup 

import requests as r

def searach_in_google( text): 
        driver__ = webdriver.Chrome('./chromedriver.exe') 
        driver__.get('https://google.com')
        

        if text is None: 
                print('Вы не ввели запрос')
        else: 
                serach_text = driver__.find_element(By.CLASS_NAME, 'gLFyf') 
                serach_text.send_keys(text) 
                print(serach_text)

def driver_optios(page, s,  arg1): 
                
                driver = webdriver.Chrome('./chromedriver.exe') 
                driver.get(page) 
                search = driver.find_element(By.CLASS_NAME, arg1) 
                search.send_keys(s)
    
                for result in search: 
                   print(result) 
             
                driver.close() 
                response = r.get(page) 
                bs4obj = BeautifulSoup(response.text, 'html.parser' )  

                for element in arg1: 
                    if bs4obj.find(arg1): 
                        print(element)

def custum_driver(url, element1, element2, element3, element4 ): 
         driver = webdriver.Chrome('./chromedriver.exe') 
         
         response = r.get(url)
         
         if url is None: 
                 print("Вы не ввели сслыку") 
         else: 
                if response.status_code == 200: 
                   
                   driver.get(url)   
                
                else: 
                        print("Error link")

         if element1 is None: 
                print('Заполните первый эелемнет') 
         else: 
                search_elemet1 = driver.find_element(By.CLASS_NAME, element1) 

                for res in search_elemet1: 
                        print(res) 

         if element2 is None: 
                print('Заполните второй эелемнет') 
         else: 
                                search_elemet2 = driver.find_element(By.CLASS_NAME, element2)  

                                for res2 in search_elemet2: 
                                        print(res2) 
         if element3 is None: 
                 print('Вы не ввели третий элемент')
         else: 
                 search_element3 = driver.find_element(By.CLASS_NAME, element3 )  

                 for res3 in search_element3: 
                         print(res3) 

         if element4 is None: 
                 print('Вы не ввели ссылку') 
         else: 
                 search_element4 = driver.find_element(By.CLASS_NAME, element4) 

                 for res4 in search_element4: 
                     print(res4)      

        
