# Scraper CCI Salta 🤖

Repositorio que forma parte del proyecto con la CCI de Salta para completar la información correspondiente a los registros mediante el "raspado" de la web "Cuit Online".

**Nota: Se pone a disposición el código, no así los datos de los registros que son de índole privada. Se emplea Python 3.10**

## Getting Started 

**Clone repository**
```
git clone git@github.com/federicofloresh/scraper_cci_salta.git
```
**Create virtual environment**
```
python -m venv venv
```
**Activate new virtual environment**
```
.\venv\Scripts\activate
```
**Install Dependencies**
```
pip install -r requirements.txt
```
**Run Script to Obtain URL's to scrape**
```
python cuit_online_urls.py
```
**Run Script to Obtain Cuits Details**
```
python cuit_online_scrape.py
```
