![image](https://github.com/Snoower/cs50p-introduction-to-programming-with-python/assets/56703794/796f7567-c600-43f9-a1ea-bce72a6cc3cf)
  
# Language Tool 1000
  ### Video Demo: https://www.youtube.com/watch?v=FI6Gicgn72w
  
  ### Description:
  This program offers three tools: language translator, definition lookup, and language identifier. The language translator allows you to translate English word or words to a languagee of your choice. The definition lookup allows you to look up the definition of an English 
  word or words. The language identifier allows you to input a word or words, whether it be in the native language or romanized in English, and identify what the native language is. However, the native language will produce a more accurate result compared to the English 
  romanization.

  ### Files:
  - **project.py** - the python file that contains the source code for my final project, Language Tool 1000. The project file imports from 4 different libraries: googletrans, PyMultiDictionary, sys and argparse.
  Within the project file, there exists a total of 5 functions: ain, translate, lookup, identify, and get language.
    - External Libraries:
      - *Googletrans*: this library provides the language translator and language identifier functionality in my program.
      - *PyMultiDictionary*: this library provides the definition lookup functionality in my program.
      - *Sys*: this library provides the command-line input functionality.
      - *Argparse*: this library provides the functionality to write user-friendly cli's.
    - Functions:
      - *Main*: The main function will read the user's input from the cli and decide what tool the user wants to use (language translator, definition lookup, or language identifier).
      If the user wants to use the language translator, then my program prompt the user to input their target language. It also uses the get_language_code function not only determine if the language is valid, but to also convert the inputted language name to the language code (more on this below).
      If the user wants to use the definition lookup tool or the language identifier tool, then it will call the lookup function or the identify function, respectively. It will then print the output.
      - *Translate*: the translate function will use the Googletrans library with the appropriate arguments (word/phrase, source language, and destination language) and return the result.
      - *Lookup*: the lookup function will use the PyMultiDictionary library to return the dictionary results. I added some additional code to ensure that only the definition is returned because it would instead return a pythonic dictionary.
      - *Identify*: the identify function will use the Googletrans library to return whichever language the tool has the highest confidence level for, which is why inputing the native language typically is more accurate than the English romanization.
      - *Get_Language_Code*: the get_language_code function is used because the Googletrans library requires the language code rather than the language name, so I imported a dictionary of language names and language codes. The format of this is 'language code:language name',
      so I reversed this dictionary. I did this because the program needs to retrieve the language code based on the language name that the user inputs. I defined the variable for this as 'languages'.

  - **test_project.py** - the python file that contains the source code that uses pytest to test the functions that are in my final project, Language Tool 1000. The test file imports the functions from my project file that I would like to test: translate,
  identify, and get_language_code. Within the test file, there exists a a total of 4 functions: test_translate, test_identify, test_get_language_code, and test_value_error.
    - Functions:
      - *Translate Test*: the test_translate function tests that the translate function in my project file is accurate. I tested this three times, where English was translated into three different languages and the expected output is "Potato" in the three different languages. 
      - *Identify Test*: the test_identify function tests that the identify function in my project file is accurate. I tested this three times, where the inputs were in three different languages and the expected output should be the name of the language of the inputs.
      - *Get_Language_Code Test*: the test_get_language_code tests that the get_language_code function in my project is correct. As previously mentioned, I created that function to retrieve the language code for the language that the user inputs, so I tested that when
      inputting a language, then the correct language code is output.
      - *ValueError Tes*t: the test_value_error function tests that the ValueError is raised if a user inputs an invalid language when prompted for the language in the translator tool.

  - **requirements.txt** - the text file that lists the modules and packages required by my final project, Language Tool 1000.

  ### Thought Process:
  Originally, my initial thought for my final project was to make an exclusive English/Korean language tool. The idea for that program was to allow translation from English to Korean and vise-versa. It would also allow the user to look up the definition of either English
  or Korean words. This posed a harder challenge than I expected because the python libraries that provided Korean dictionary utility were either outdated and wouldn't return any results or were having API connection issues. The former library was ncdic, which would have been 
  perfect for my use-case, but it was refusing to output anything, even when I isolated testing to only that library. The latter library was krdict, where I was experiencing connection issues to the API. I ended up pivoting to a more general purpose language tool. I also found 
  this to be a better option because now users aren't restriced to only Korean translations. It also allowed my code to be more dynamic because I am not having to hardcode "Korean" or "English" into it. If I wanted to make modifications, such as allowing the tool to natively 
  be any language other than English, then I would need to change the "native_language" variable to the desired language code and then supply the lookup function with a dictionary in that language.
