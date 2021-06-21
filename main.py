import json
import re
import sys
from typing import Dict, Iterable, List, Pattern, Tuple


def build_re_patterns(keys: Iterable) -> Pattern[str]:

    sorted_keys = sorted(keys, key=len, reverse=True)
    patterns_str = "|".join(re.escape(term) for term in sorted_keys)
    patterns_str = "(?=({}))".format(patterns_str)
    patterns = re.compile(patterns_str, re.IGNORECASE)
    return patterns


def return_acronym_dicts() -> Tuple[Dict[str, List], Dict[str, List]]:

    with open("wiki_computer_and_it_abbreviations.json", "r") as fp:
        comp_it_acronyms = json.load(fp)
        

    with open("wiki_filename_extensions.json", "r") as fp:
        filename_acronyms = json.load(fp)

    return comp_it_acronyms, filename_acronyms


def lower_case_keys_in_dict(acronym_dict):

    lower_cased_acronyms = {k.lower(): v for k, v in acronym_dict.items()}
    return lower_cased_acronyms


def pattern_match_on_str(text: str) -> None:

    text = text.lower()
    comp_it_acronyms, filename_acronyms = return_acronym_dicts()
    comp_it_lu = {k.lower(): k for k in comp_it_acronyms.keys()}
    comp_it_acronyms = lower_case_keys_in_dict(comp_it_acronyms)
    filename_acronyms = lower_case_keys_in_dict(filename_acronyms)

    comp_it_patterns = build_re_patterns(comp_it_acronyms.keys())
    filename_patterns = build_re_patterns(filename_acronyms.keys())

    comp_acronyms = comp_it_patterns.findall(text)
    comp_acronyms = list(dict.fromkeys(comp_acronyms))
    if comp_acronyms:
        print("\nWikipedia List of computing and IT abbreviations: ")
        print("-"*40)
        for acronym in comp_acronyms:
            print(comp_it_lu[acronym], ":" ,*comp_it_acronyms[acronym])
        print("-"*40)

    fn_acronyms = filename_patterns.findall(text)
    fn_acronyms = list(dict.fromkeys(fn_acronyms))
    if fn_acronyms:
        print("\nWikipedia List of filename extensions: ")
        print("-"*40)
        for acronym in fn_acronyms:
            print(f".{acronym}", ":" , *filename_acronyms[acronym])
        print("-"*40)

    
if __name__ == "__main__":

    text = sys.argv[1]
    print("input str:", text)
    pattern_match_on_str(text)
