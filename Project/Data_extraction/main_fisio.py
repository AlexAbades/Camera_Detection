from logging import exception
import requests
import xmltojson
import pandas as pd
import io


import re
from tqdm import tqdm
from bs4 import BeautifulSoup
import json 

# To speed up we can search for the max number of profesionals and create a dataframe with that 
# dimensions before making thge requet so we are not increasing the dataframe. 

# Also, make a request to check the max number of profsionals, if it hasn't changed we don't make the request 


if __name__ == "__main__":
    
    try:

        # Define max time the request to a page it's going to be allowed 
        maxtime = 10  # Seconds
        # WEB SCARPING: Obtain the max page number. 
        # Define the main page
        main_URL = 'https://www.consejo-fisioterapia.org/vu_colegiados.html'
        # Define the URL that has the information of one specific page. 
        page_URL = 'https://www.consejologopedas.com/censo_de_colegiados/pag_1/descargar.html'
        # Make a request to the page 
        response = requests.get(main_URL, timeout=maxtime)
        # Check if request is satifactory 
        if response:
            print('Request succesfull, proceeding to extract the number of pages\n...')
        else:
            print(f'Response not sucesfull. Error: {response}')
        # Parse to beatifulsoup so we can operate
        soup = BeautifulSoup(response.content, "html.parser")
        # Find in which section the pages are defined 
        results = soup.find(id="contenido")
        # Search for the specific class that stores the number of pages 
        job_elements = results.find_all("ul", class_="pagination")
                
        # Iterate through elements to get the links (even if it's just one element)
        for element in job_elements:
            # -- snip --
            links = element.find_all("a")
        

        # get the last page reference 
        last_page = int(links[-1].text)
        print(f'Last page found: {last_page}')
        # MOD
        last_page = 5
        # Iterate through all the number of pages and download the script
        for i in tqdm(range(1,last_page+1)):
            # Actualize the data 
            url_tmp = re.sub(r'\d', str(i), page_URL)
            # request the csv file
            urlData = requests.get(url_tmp, timeout=maxtime)
            # Check if request it's Ok
            if urlData:
                # check if it's the first time and create the original dataframe
                if i == 1:
                    # Transform the data into a dataframe and create main dataframe
                    df = pd.read_csv(io.StringIO(urlData.content.decode('ISO-8859-1')), delimiter=';')
                else: 
                    # Transform the data dataframe and create a temporary df
                    df_tmp = pd.read_csv(io.StringIO(urlData.content.decode('ISO-8859-1')), delimiter=';')
                    #  concatenate the dataframe
                    df = pd.concat(
                                    [df, df_tmp],
                                    axis=0,
                                    join="outer",
                                    ignore_index=True,
                                    keys=None,
                                    levels=None,
                                    names=None,
                                    verify_integrity=False,
                                    copy=True,
                                )
            else:
                print(f'An Error: {urlData} ocurred while requesting the information on tha mage URL: \n{page_URL}')
        # Drop last column 
        df.drop(columns=df.columns[-1], inplace=True)
        # Save DataFrame 
        try: 
            df.to_csv('Fisios_DataFrame.csv', index=False)
            print("SAVED SUCCESSFUL!\nSummary:")
            print(df.info(memory_usage='deep'))

        except exception as err:
            print('Not saved an Error ocurred: {err}')

    # Except some Errors
    except requests.ConnectionError:
        print('No internet Connection')
    except requests.Timeout:
        print('Request timeout exceeded: Internet connection lost or not fast enough') 