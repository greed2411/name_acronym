import json
import re
from typing import List, Dict

import bs4
import requests

from pprint import pprint

def computing_and_it_abbreviations() -> Dict[str, List]:

    url = "https://en.wikipedia.org/wiki/List_of_computing_and_IT_abbreviations"
    resp = requests.get(url=url)
    soup = bs4.BeautifulSoup(resp.content, "html5lib")
    div_sections = soup.findAll("div", attrs={"class": "div-col"})

    acronyms_expansions_dict = {}

    for section in div_sections:
        
        for list_element in section.findAll("li"):

            try:
                acronym = list_element.find("a").text
                acronym_expansion = list_element.text
                expansion = acronym_expansion[len(acronym)+1:]
                # print(acronym, expansion)
                if acronym in acronyms_expansions_dict:
                    acronyms_expansions_dict[acronym].append(expansion)
                else:
                    acronyms_expansions_dict[acronym] = [expansion]

            except Exception as e:
                # print(e)
                # print(list_element)
                continue

    # pprint(acronyms_expansions_dict)
    return acronyms_expansions_dict



def filename_extensions_abbreviations():

    urls = [
        "https://en.wikipedia.org/wiki/List_of_filename_extensions_(A%E2%80%93E)",
        "https://en.wikipedia.org/wiki/List_of_filename_extensions_(F%E2%80%93L)",
        "https://en.wikipedia.org/wiki/List_of_filename_extensions_(M%E2%80%93R)",
        "https://en.wikipedia.org/wiki/List_of_filename_extensions_(S%E2%80%93Z)",
    ]

    acronyms_expansions_dict = {}


    for url in urls:

        resp = requests.get(url=url)
        soup = bs4.BeautifulSoup(resp.content, "html5lib")

        tables = soup.findAll("table", attrs={"class": "wikitable"})

        for table in tables:
            tbody = table.find("tbody")
            for tr in tbody.findAll("tr"):
                for j, td in enumerate(tr.findAll("td")):
                    if j<2:
                        word = td.text.strip()
                        word =  re.sub(r"\[[^()]*\]", "", word)
                        if ".mw-parser-output" in word:
                            break
                        if j == 0:
                            acronym = word
                            if word not in acronyms_expansions_dict:
                                acronyms_expansions_dict[acronym] = []
                        elif j == 1:
                            expansion = word
                            acronyms_expansions_dict[acronym].append(expansion)


    # pprint(acronyms_expansions_dict)
    return acronyms_expansions_dict


                        




if __name__ == "__main__":
    
    comp_it_acronyms = computing_and_it_abbreviations()
    print(len(comp_it_acronyms.keys()))
    filename_acronyms = filename_extensions_abbreviations()
    print(len(filename_acronyms.keys()))

    with open("wiki_computer_and_it_abbreviations.json", "w") as fp:
        json.dump(comp_it_acronyms, fp)

    with open("wiki_filename_extensions.json", "w") as fp:
        json.dump(filename_acronyms, fp)

    print("successfully dumped the jsons!")
