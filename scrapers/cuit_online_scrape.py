import pandas as pd
from playwright.sync_api import Page, expect
from playwright.async_api import async_playwright
from playwright.async_api import async_playwright
from playwright.async_api._generated import ElementHandle
import pickle
import asyncio

pickle_file = './urls.pkl'

with open(pickle_file, 'rb') as archivo_pickle:
    urls = pickle.load(archivo_pickle)

async def main(url):
    
    data_scraped = []

    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        for j in url:

            cuit = j.split("/")[-2]
            try:
                await page.goto(j)

                #Fields

                try:
                    actividades_element = page.locator('xpath=//h2[@class="impuestos_activos"]/../div/span')

                    count_actividades = await actividades_element.count()

                    actividades = []

                    for indice in range(0,count_actividades):

                        detalle_act = await actividades_element.nth(indice).text_content()

                        actividades.append(detalle_act)

                except:

                    actividades = None
                
                try:
                    street = await page.locator('xpath=//li[@itemprop="address"]/span[@itemprop="streetAddress"]').text_content(timeout=5000)
                    province = await page.locator('xpath=//li[@itemprop="address"]/span[@itemprop="addressRegion"]').text_content(timeout=5000)
                    locality = await page.locator('xpath=//li[@itemprop="address"]/span[@itemprop="addressLocality"]').text_content(timeout=5000)

                except:
                    street = None
                    province = None
                    locality = None

                data_scraped.append({
                    'cuit':cuit,
                    'street': street,
                    'province':province,
                    'locality':locality,
                    'activities':actividades

                }
                )

                await asyncio.sleep(10)
            
            except:
                continue


        return data_scraped

async def go_to_url():

    tasks = [main(url) for url in urls]
    return await asyncio.wait(tasks)

results =  asyncio.get_event_loop().run_until_complete(go_to_url())

results = results[0]

lista_final = []

for i in results:
    lista_final.append(i.result())

print(lista_final)

with open('./data_cuit.pickle', 'wb') as archivo_pickle:
    pickle.dump(lista_final, archivo_pickle)
