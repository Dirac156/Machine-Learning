import pycountry
from babel.languages import get_official_languages, get_territory_language_info
from babel import Locale

def get_local_language(territory: str):
    """  """
    # get territory code
    territory_code = (pycountry.countries.search_fuzzy(territory)[0]).alpha_2
    
    # get official languages

    official_languages = get_official_languages(territory_code)

    # get non official languages

    languages = get_territory_language_info(territory_code)

    official_languages_dic = {}

    non_official_languages = {}

    # get the most recognized languages

    try:
        for official_language in official_languages:
            l = Locale.parse(official_language)
            official_languages_dic[official_language] =  l.get_display_name(official_language)
    except:
        pass


    try:
        for language, value in languages.items():
            l = Locale.parse(language)
            value['language_name'] = l.get_display_name(language)
            non_official_languages[language] = value 
    except:
        pass
    
    return official_languages_dic, non_official_languages
