
"""
    Input -  A subject + infinitive form of a verb.

    To conjugate a verb in the imparfait:
        - Drop the last two letters of the verb.
        - Replace it with the correct ending.
    See the table in the description for conjugations.
Subject 	Verb Ending
Je (I) 	            -ais
Tu (You) 	        -ais
Il/Elle/On
(He/She/It or We) 	-ait
Nous (We) 	        -ions
Vous (You or Y'all)  -iez
Ils/Elles (They) 	-aient
"""


def to_imparfait(verb_phrase):
    ending = ""
    separate_words = verb_phrase.split()
    if separate_words[0]=="Je" or separate_words[0]=="Tu":
        ending = "ais"
    elif separate_words[0]=="Il" or separate_words[0]=="Elle" or separate_words[0]=="On":
        ending = "ait"
    elif separate_words[0]=="Nous":
        ending = "ions"
    elif separate_words[0]=="Vous":
        ending = "iez"
    else:
        ending = "aient"
    return verb_phrase[0:-2]+ending


to_imparfait("On helper")