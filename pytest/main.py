# import requests BeautifulSoup4 lxml
from dataclass import Website
import requests
from bs4 import BeautifulSoup
from typing import List

url = 'https://en.wikipedia.org/wiki/Programming_languages_used_in_most _popular_websites'
page = requests.get(url).text


def get_data_from_site(link: str) -> List[List[str]]:
    """
    Download data from the site table to the list by rows
    """
    soup = BeautifulSoup(page, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    table_body = table.find('tbody')
    table_rows = table_body.find_all('tr')[1:]
    row_list = [row.text.split('\n') for row in table_rows]
    #remove empty values
    clean_list = [[element for element in list_element if element] for list_element in row_list]
    return clean_list


def convert_data_to_dataclass(data: List[List[str]]) -> List[Website]:
    """
    Convert str data in the list to dataclass Website
    """
    websites = []
    for row in data:
        name = row[0]
        popularity = row[1]
        frontend = row[2]
        backend = row[3]
        database = row[4]
        notes = row[5] if len(row) > 5 else None
        website = Website(name, popularity, frontend, backend, database, notes)
        websites.append(website)
    return websites


def convert_popularity_to_int(websites: List[Website]) -> List[Website]:
    """
    Change popularity by str to int type
    """
    websites_int = []
    for website in websites:
        remove_extra = website.popularity.split('[')[0]
        int_popularity = ''.join(filter(str.isdigit, remove_extra))
        website.popularity = int(int_popularity)
        websites_int.append(website)
    return websites_int


def get_data_from_table() -> List[Website]:
    """
    Return list of class Website with data from table Programming languages used in most popular  websites
    """
    base_data = get_data_from_site(url)
    converted_data = convert_data_to_dataclass(base_data)
    result_data = convert_popularity_to_int(converted_data)
    return result_data


if __name__ == '__main__':
    get_data_from_table()








