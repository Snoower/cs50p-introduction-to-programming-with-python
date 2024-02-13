from googletrans import Translator, LANGUAGES
from PyMultiDictionary import MultiDictionary, DICT_WORDNET
import sys
import argparse

translator = Translator()
languages = {v: k for k, v in LANGUAGES.items()}
dictionary = MultiDictionary()
native_language = 'en'

def main():
    tool = sys.argv[1]
    if tool == "--translator":
        word = ' '.join(args.translator)
        language = input("What language?: ")
        try:
            language_code = get_language_code(language)
            if language_code:
                print("Translated text: " + translate(word, native_language, language_code))
            else:
                print("Invalid language")
        except KeyError:
            print("Invalid language")
    elif tool == "--lookup":
        word = ' '.join(args.lookup)
        print(lookup(word))
    elif tool == "--identifier":
        word = ' '.join(args.identifier)
        print(identify(word))


def translate(w, src_lang, dest_lang):
    translation = translator.translate(w, src=src_lang, dest=dest_lang)
    return translation.text

def lookup(w):
    try:
        definition = dictionary.meaning(native_language, w, dictionary=DICT_WORDNET)
        if definition:
            definition = ", ".join(definition.get('Noun', []))
            definition = definition[0].upper() + definition[1:]
            return definition
    except Exception:
        return "Meaning not found."

def identify(w):
    identify = translator.detect(w)
    language_name = LANGUAGES.get(identify.lang, "Unknown")
    return "Language: " + language_name

def get_language_code(language_name):
    return languages.get(language_name.lower())


if __name__ == "__main__":
    ascii_art = r"""
 (
 )\ )                                          *   )        (       )    )    )    )
(()/(    )       (  (    (     ) (  (    (   ` )  /(        )\   ( /( ( /( ( /( ( /(
 /(_))( /(  (    )\))(  ))\ ( /( )\))(  ))\   ( )(_)|    ( ((_)  )\()))\()))\()))\())
(_))  )(_)) )\ )((_))\ /((_))(_)|(_))\ /((_) (_(_()))\   )\ _   ((_)\((_)\((_)\((_)\
| |  ((_)_ _(_/( (()(_|_))(((_)_ (()(_|_))   |_   _((_) ((_) |   / (_)  (_)  (_)  (_)
| |__/ _` | ' \)) _` || || / _` / _` |/ -_)    | |/ _ \/ _ \ |   | || () | () | () |
|____\__,_|_||_|\__, | \_,_\__,_\__, |\___|    |_|\___/\___/_|   |_| \__/ \__/ \__/
                |___/           |___/
 """
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=ascii_art + "\nThis program has three tools: language translator, definition lookup, and language identifier.")
    parser.add_argument('--translator', metavar='', nargs='+', help='Translates English to a language of your choice')
    parser.add_argument('--lookup', metavar='', nargs='+', help='Looks up the definition of an English word or words')
    parser.add_argument('--identifier', metavar='', nargs='+', help='Identifies the language of the input (English romanization works too, but native language inputs will be more accurate!)')
    args = parser.parse_args()
    main()

#Banner from http://www.patorjk.com/software/taag/#p=display&h=2&f=Fire%20Font-s&t=Language%20Tool%201000
