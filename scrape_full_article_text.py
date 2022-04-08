import os
import sys
import requests
import pandas as pd

from bs4 import BeautifulSoup
from datetime import date

def detect_path():
    pwd = os.path.abspath('')
    return pwd + '/' + 'data'

def time_stamp():
    today = date.today()
    return today.strftime("%m-%d-%Y")

def extract_article_text(citations):
    ts = time_stamp()
    pwd = detect_path()

    citations = pd.read_csv(citations)

    for index, row in citations.iterrows():
        url = row['url']
        article_id = row['article_id']
        source = row['source']

        try:
            # "if not ondemand" is for the NPR citations specifically 
            if not 'ondemand' in url:
                response = requests.get(url)
                page_content = BeautifulSoup(response.text, 'html.parser')
        
                for paragraph in page_content.findAll('p'):
                    paragraph = list(paragraph.stripped_strings)

                    for sentence in paragraph:
                        export_name = pwd + '/' + ts + '/' + source + '_full_article_text_' + ts + '.txt'

                        with open(export_name, 'a+') as f:
                            f.write(sentence)
                            
                with open(export_name, 'a+') as f:
                    f.write('\n')
                    f.write('   \n')

        except Exception as response_exception:
            with open(pwd + '/' + ts + '/' + source + '_full_article_text_exception_log_' + ts + '.txt', 'a+') as f:
                        f.write(response_exception + '    ' + url + '    ' + article_id)

if __name__ == '__main__':
    try:
        input_file = sys.argv[1]
    except IndexError:
        exit('Missing input file argument')

    extract_article_text(input_file)
    #extract_article_text('/home/stephbuon/projects/entascope/data/scraped_pages/12-27-2021/citations_NPR_12-27-2021.csv')
