dictionary = {
    "keywords": {
        "tupu": "None",
        "Kweli": "True",
        "SiKweli": "False",  # semantical correction
        "vunja": "break",
        "endelea": "continue",
        "rudisha": "return",
        "weka": "input", # we have to use weka so as ingiza ro be used on import
        "ikiwa": "if", # we have to put ikiwa so as to give keyword "as" as kama example: from->kutoka starlette_api.applications import->ingiza Starlette as->kama my_app
        "pia": "elif",  # as long as it makes sense semantical translation does not matter
        "iwapo": "for", # we have to give iwapo so as  keyword if to be use as ikiwa example: ikiwa jumla == 7: and iwapo props katika list:
        "katiya": "range",
        "katika": "in", #example for prop in list: -> iwapo prop katika list:
        "wakati": "while",
        "andika": "print",
        "zaidi": "else",
        "njia": "def",  # njia is a more relevant keyword to functions/method
        "pamoja": "with",
        "darasa": "class",
        "futa": "del",  # futa is a lot simple to catch with and is commonly used than ondoa
        "kutoka": "from",
        "ingiza": "import"
        "sio": "not",
        "ni": "is",
        "au": "or",
        "na": "and",
        "neno": "str",
        "orodha": "list",
        "kamusi": "dict",
        "jaribu": "try",
        "ila": "except",  # ila is a lot simple to catch with and most relevant translation of except
        "mwisho": "fianlly" #can be even mwishowe 
        "kama": "as" #we have to put ikiwa so as to give keyword "as" as kama 
    },
    "block_keywords": {
        "ikiwa": "if", # we have to put "ikiwa" so as to give keyword "as" as kama 
        "pia": "elif",  # reference line 10
        "zaidi": "else",
        "wakati": "while",
        "iwapo": "for", # we have to give iwapo so as  keyword if to be use as ikiwa example:if jumla == 7: => ikiwa jumla == 7: , and for props in list: => iwapo prop katika list:
        "njia": "def",  # reference line 17
        "pamoja": "with",
        "ila": "except",  # reference line 30
    },
}
