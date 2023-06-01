# -*- coding: utf-8 -*-
"""Copy of Ling360 kurmanji conjugator final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Lja2iC2X6lIYn-Y3AvyQBtrfS4VB17MI
"""

!pip install hfst-dev
import hfst_dev
from hfst_dev import fst, regex, disjunct, intersect, concatenate, compose, compile_lexc_script, compile_lexc_file, HfstTransducer, XfstCompiler, compile_xfst_script, subtract
import re
import json

dictionary = []
with open('leker-kurmanji.json', 'r') as f:
  first_dictionary = json.load(f)
  for i in first_dictionary:
    new_i = {"word":i.get("word"), "meaning":i.get("meanings")[0].get("translation")}
    dictionary.append(new_i)
print(dictionary)

verb_list = []
with open("verb_transitivity.txt", "r", encoding="utf-8-sig") as file:
  lines = file.readlines()
  for line in lines:
    if len(line) > 1:
      verb_list.append(line.replace("\n", ""))

  transitive_verb_list = []
  intransitive_verb_list = []
  for item in verb_list:
    if "intransitive" in item:
        intransitive_verb_list.append(item.split(':')[0].strip())
    else:
        transitive_verb_list.append(item.split(':')[0].strip())

kurmanji_verb_list = []
for i in dictionary:
  if i.get("word") in transitive_verb_list:
    i['Transitive'] = True
  elif i.get("word") in intransitive_verb_list:
    i['Transitive'] = False
  else:
    i['Transitive'] = True

  if i.get("word")[-2:] == "în":
    i["past_root"] = i.get("word")[:-2] + "î"
    i["present_root"] = i.get("word")[:-2]
    i['Transitive'] = False
  elif i.get("word")[-3:] == "bûn":
    i["past_root"] = "bû"
    i["present_root"] = "b"
    i["stem"] = i.get("word")[:-3]
    i['Transitive'] = False
  elif i.get("word")[-3:] == "dan":
    i["past_root"] = "da"
    i["present_root"] = "d"
    i["stem"] = i.get("word")[:-3]
    i['Transitive'] = True
  elif i.get("word")[-3:] == "man":
    i["past_root"] = "ma"
    i["present_root"] = "mîn"
    i["stem"] = i.get("word")[:-3]
    i['Transitive'] = False
  elif i.get("word")[-8:] == "kişandin":
    i["past_root"] = "kişand"
    i["present_root"] = "kişîn"
    i["stem"] = i.get("word")[:-8]
    i['Transitive'] = True
  elif i.get("word")[-6:] == "şandin":
    i["past_root"] = "şand"
    i["present_root"] = "şîn"
    i["stem"] = i.get("word")[:-6]
    i['Transitive'] = True
  elif i.get("word")[-6:] == "ajotin":
    i["past_root"] = "ajot"
    i["present_root"] = "ajo"
    i['Transitive'] = True
  elif i.get("word")[-5:] == "kirin":
    i["past_root"] = "kir"
    i["present_root"] = "k"
    i["stem"] = i.get("word")[:-5]
    i['Transitive'] = True
  elif i.get("word")[-5:] == "dîtin":
    i["past_root"] = "dît"
    i["present_root"] = "bîn"
    i["stem"] = i.get("word")[:-5]
    i['Transitive'] = True  
  elif i.get("word")[-6:] == "girtin":
    i["past_root"] = "girt"
    i["present_root"] = "gir"
    i["stem"] = i.get("word")[:-6]
    i['Transitive'] = True
  elif i.get("word")[-6:] == "kuştin":
    i["past_root"] = "kuşt"
    i["present_root"] = "kuj"
    i["stem"] = i.get("word")[:-6]
    i['Transitive'] = True  
  elif i.get("word")[-5:] == "ketin":
    i["past_root"] = "ket"
    i["present_root"] = "kev"
    i["stem"] = i.get("word")[:-5]
    i['Transitive'] = False
  elif i.get("word")[-7:] == "xwendin":
    i["past_root"] = "xwend"
    i["present_root"] = "xwîn"
    i["stem"] = i.get("word")[:-7]
    i['Transitive'] = True  
  elif i.get("word")[-7:] == "standin":
    i["past_root"] = "stand"
    i["present_root"] = "stîn"
    i["stem"] = i.get("word")[:-7]
    i['Transitive'] = True
  elif i.get("word")[-5:] == "andin":
    i["past_root"] = i.get("word")[:-5] + "and"
    i["present_root"] = i.get("word")[:-5] + "în"
    i['Transitive'] = True
  elif i.get("word")[-2:] == "in":
    i["past_root"] = i.get("word")[:-2]
    i["present_root"] = i.get("word")[:-2]
    i['Transitive'] = False
  else:
    i["past_root"] = "0"
    i["present_root"] = "0"
  
  kurmanji_verb_list.append(i)

with open("ferhengo.json", 'w', encoding="utf-8") as json_file:
    json.dump(kurmanji_verb_list, json_file, indent=4, separators=(',', ': '), ensure_ascii=False)

data = kurmanji_verb_list

verb_past_root_transitive = []
verb_present_root_transitive = []

verb_past_root_intransitive = []
verb_present_root_intransitive = []


for i in data: 
  if i.get("stem") == None:
    if i.get("Transitive") == True:   
      verb_past_root_transitive.append([i.get("word"), i.get("past_root")])
      verb_present_root_transitive.append([i.get("word"), i.get("present_root")])
    elif i.get("Transitive") == False:   
      verb_past_root_intransitive.append([i.get("word"), i.get("past_root")])
      verb_present_root_intransitive.append([i.get("word"), i.get("present_root")])
  else:
    if i.get("Transitive") == True:   
      verb_past_root_transitive.append([i.get("word"), i.get("past_root"), i.get("stem")])
      verb_present_root_transitive.append([i.get("word"), i.get("present_root"), i.get("stem")])
    elif i.get("Transitive") == False:   
      verb_past_root_intransitive.append([i.get("word"), i.get("past_root"), i.get("stem")])
      verb_present_root_intransitive.append([i.get("word"), i.get("present_root"), i.get("stem")])

words_stems = []
words_with_no_stems = []
for i in data: 
  if i.get("stem") != None:
    words_stems.append([i.get("word"),i.get("stem")])
  else:
    words_with_no_stems.append([i.get("word"),i.get("present_root")])

# HFST Leker Kurmanji

with open("kurdish_verb_parser.lexc","w",encoding="utf-8") as lexc_file:
  lexc_file.write("""
   
  LEXICON Root
          Verbs_intransitive ; ! No input, no output
          Verbs_transitive ; ! No input, no output
         

Futureprefix+:ê%     Stem ;
Futureprefix+:ê%     Future_with_no_prebase ;
Present+:di        Verbs_future_present;

  LEXICON Stem
  """)
  [lexc_file.write(f"{i[0]}:{i[1]}\t Future ;\n") for i in words_stems]
  lexc_file.write("""

  LEXICON Future

  +Future+:bi      Verbs_future_present;

  LEXICON Future_with_no_prebase

  Future+:bi      Verbs_future_present;


  LEXICON Verbs_future_present
  """)
  [lexc_file.write(f"{i[0]}:{i[1]}\t Verb ;\n") for i in verb_present_root_transitive]
  [lexc_file.write(f"{i[0]}:{i[1]}\t Verb ;\n") for i in verb_present_root_intransitive]
  lexc_file.write("""

  LEXICON Verb
  +Verb:0    Subject_verb_agreement ;

  LEXICON Subject_verb_agreement
  +A1sg:im   # ;
  +A2sg:î    # ;
  +A3sg:e    # ;
  +A1pl:in   # ;
  +A2pl:in   # ;
  +A3pl:in   # ;   

  LEXICON Verbs_intransitive
  """)
  [lexc_file.write(f"{i[0]}:{i[1]}\t Verb_intransitive_0 ;\n") for i in verb_past_root_intransitive]
  lexc_file.write("""


  LEXICON Verb_intransitive_0
  +Verb+Past:0    Subject_verb_agreement_intransitive ;

  LEXICON Subject_verb_agreement_intransitive
  +A1sg:im   # ;  
  +A2sg:î    # ;
  +A3sg:0    # ;
  +A1pl:in   # ;
  +A2pl:in   # ;
  +A3pl:in   # ; 

  LEXICON Verbs_transitive
  """)
  [lexc_file.write(f"{i[0]}:{i[1]}\t Verb_transitive_0 ;\n") for i in verb_past_root_transitive]
  lexc_file.write("""

  LEXICON Verb_transitive_0
  +Verb+Past:0    Subject_verb_agreement_transitive ;

  LEXICON Subject_verb_agreement_transitive
  +O_Sg:0   # ;
  +O_Pl:in    # ;
  

  END
  """)

kurdish_verb = compile_lexc_file("kurdish_verb_parser.lexc",verbosity=1)
kurdish_verb.minimize()

def find(lst, key, value):
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return i
    return -1

def erase_duplicate(word):
  if word[-1] in 'aeiouûî' and word[-2] in 'aeiouûî':
    new_word = word[:-1]
    return new_word
  elif word[-2] in 'aeiouûî' and word[-3] in 'aeiouûî':
    consanant_ending = word[:len(word)-2] + word[len(word)-1:]
    return consanant_ending
  else:
    return word

import editdistance as editdistance

def autocorrect(word, n=6):
    if word in data:
        return word
    else:
        candidates = {}
        for correct_word in data:
            distance = editdistance.distance(word, correct_word["word"])
            candidates[correct_word["word"]] = distance

        minimum_dist = min(candidates.values())
        possible_verbs = []
        for k, v in candidates.items():
            if v == minimum_dist:
                possible_verbs.append(k)

        if len(possible_verbs) == 1:
            print(f"Did you mean {possible_verbs[0]}?\n")
            return possible_verbs[0]

        elif len(possible_verbs) > 0:
            print("Did you mean one of the following verbs?")
            for i, verb in enumerate(possible_verbs, start=1):
                print(f"{i}. {verb}")

            while True:
                choice = input("Please enter the number of the verb you choose: ")
                try:
                    choice = int(choice)
                    if 1 <= choice <= len(possible_verbs):
                        return possible_verbs[choice - 1]
                    else:
                        print("Invalid choice. Please enter a valid number.")
                except ValueError:
                    print("Invalid choice. Please enter a valid number.")
        
        else:
            return None  # No possible corrections found

        word = input("Enter a word: ")
        corrected_verb = autocorrect(word)
        if corrected_verb:
            return corrected_verb
        else:
            print("No correction found.")

def get_info(d, tense='all'):
  
  if tense == 'present' or tense=='all':
    if 'stem' in d.keys():
      print("Ez",d['stem'],erase_duplicate(kurdish_verb.lookup(f"Present+{d['word']}+Verb+A1sg")[0][0]))
      print("Tu",d['stem'],erase_duplicate(kurdish_verb.lookup(f"Present+{d['word']}+Verb+A2sg")[0][0]))
      print("Ew",d['stem'],erase_duplicate(kurdish_verb.lookup(f"Present+{d['word']}+Verb+A3sg")[0][0]))
      print("Em",d['stem'],erase_duplicate(kurdish_verb.lookup(f"Present+{d['word']}+Verb+A1pl")[0][0]))
      print("Hun",d['stem'],erase_duplicate(kurdish_verb.lookup(f"Present+{d['word']}+Verb+A2pl")[0][0]))
      print("Ew",d['stem'],erase_duplicate(kurdish_verb.lookup(f"Present+{d['word']}+Verb+A3pl")[0][0]))
    else:
      print("Ez",erase_duplicate(kurdish_verb.lookup(f"Present+{d['word']}+Verb+A1sg")[0][0]))
      print("Tu",erase_duplicate(kurdish_verb.lookup(f"Present+{d['word']}+Verb+A2sg")[0][0]))
      print("Ew",erase_duplicate(kurdish_verb.lookup(f"Present+{d['word']}+Verb+A3sg")[0][0]))
      print("Em",erase_duplicate(kurdish_verb.lookup(f"Present+{d['word']}+Verb+A1pl")[0][0]))
      print("Hun",erase_duplicate(kurdish_verb.lookup(f"Present+{d['word']}+Verb+A2pl")[0][0]))
      print("Ew",erase_duplicate(kurdish_verb.lookup(f"Present+{d['word']}+Verb+A3pl")[0][0]))

  if tense == 'future' or tense=='all':
    if 'stem' in d.keys():
      print("Ez",erase_duplicate(kurdish_verb.lookup(f"Futureprefix+{d['word']}+Future+{d['word']}+Verb+A1sg")[0][0]))
      print("Tu",erase_duplicate(kurdish_verb.lookup(f"Futureprefix+{d['word']}+Future+{d['word']}+Verb+A2sg")[0][0]))
      print("Ew",erase_duplicate(kurdish_verb.lookup(f"Futureprefix+{d['word']}+Future+{d['word']}+Verb+A3sg")[0][0]))
      print("Em",erase_duplicate(kurdish_verb.lookup(f"Futureprefix+{d['word']}+Future+{d['word']}+Verb+A1pl")[0][0]))
      print("Hun",erase_duplicate(kurdish_verb.lookup(f"Futureprefix+{d['word']}+Future+{d['word']}+Verb+A2pl")[0][0]))
      print("Ew",erase_duplicate(kurdish_verb.lookup(f"Futureprefix+{d['word']}+Future+{d['word']}+Verb+A3pl")[0][0]))
    else:
      print("Ez",erase_duplicate(kurdish_verb.lookup(f"Futureprefix+Future+{d['word']}+Verb+A1sg")[0][0]))
      print("Tu",erase_duplicate(kurdish_verb.lookup(f"Futureprefix+Future+{d['word']}+Verb+A2sg")[0][0]))
      print("Ew",erase_duplicate(kurdish_verb.lookup(f"Futureprefix+Future+{d['word']}+Verb+A3sg")[0][0]))
      print("Em",erase_duplicate(kurdish_verb.lookup(f"Futureprefix+Future+{d['word']}+Verb+A1pl")[0][0]))
      print("Hun",erase_duplicate(kurdish_verb.lookup(f"Futureprefix+Future+{d['word']}+Verb+A2pl")[0][0]))
      print("Ew",erase_duplicate(kurdish_verb.lookup(f"Futureprefix+Future+{d['word']}+Verb+A3pl")[0][0]))

  if tense == 'past' or tense=='all':
    if d["Transitive"]:
      if 'stem' in d.keys():
        print("Min","ew",d['stem'],erase_duplicate(kurdish_verb.lookup(f"{d['word']}+Verb+Past+O_Sg")[0][0]))
        print("Te","ew",d['stem'],erase_duplicate(kurdish_verb.lookup(f"{d['word']}+Verb+Past+O_Sg")[0][0]))
        print("Wi/wê","ew",d['stem'],erase_duplicate(kurdish_verb.lookup(f"{d['word']}+Verb+Past+O_Sg")[0][0]))
        print("Me","ew",d['stem'],erase_duplicate(kurdish_verb.lookup(f"{d['word']}+Verb+Past+O_Sg")[0][0]))
        print("We","ew",d['stem'],erase_duplicate(kurdish_verb.lookup(f"{d['word']}+Verb+Past+O_Sg")[0][0]))
        print("Wê","ew",d['stem'],erase_duplicate(kurdish_verb.lookup(f"{d['word']}+Verb+Past+O_Sg")[0][0]))
      else:
        print("Min","ew",erase_duplicate(kurdish_verb.lookup(f"{d['word']}+Verb+Past+O_Sg")[0][0]))
        print("Te","ew",erase_duplicate(kurdish_verb.lookup(f"{d['word']}+Verb+Past+O_Sg")[0][0]))
        print("Wi/wê","ew",erase_duplicate(kurdish_verb.lookup(f"{d['word']}+Verb+Past+O_Sg")[0][0]))
        print("Me","ew",erase_duplicate(kurdish_verb.lookup(f"{d['word']}+Verb+Past+O_Sg")[0][0]))
        print("We","ew",erase_duplicate(kurdish_verb.lookup(f"{d['word']}+Verb+Past+O_Sg")[0][0]))
        print("Wê","ew",erase_duplicate(kurdish_verb.lookup(f"{d['word']}+Verb+Past+O_Sg")[0][0]))
    else:
      if 'stem' in d.keys():
        print("Ez",d['stem'],erase_duplicate(kurdish_verb.lookup(f"{d['word']}+Verb+Past+A1sg")[0][0]))
        print("Tu",d['stem'],erase_duplicate(kurdish_verb.lookup(f"{d['word']}+Verb+Past+A2sg")[0][0]))
        print("Ew",d['stem'],erase_duplicate(kurdish_verb.lookup(f"{d['word']}+Verb+Past+A3sg")[0][0]))
        print("Em",d['stem'],erase_duplicate(kurdish_verb.lookup(f"{d['word']}+Verb+Past+A1pl")[0][0]))
        print("Hun",d['stem'],erase_duplicate(kurdish_verb.lookup(f"{d['word']}+Verb+Past+A2pl")[0][0]))
        print("Ew",d['stem'],erase_duplicate(kurdish_verb.lookup(f"{d['word']}+Verb+Past+A3pl")[0][0]))
      else:
        print("Ez",erase_duplicate(kurdish_verb.lookup(f"{d['word']}+Verb+Past+A1sg")[0][0]))
        print("Tu",erase_duplicate(kurdish_verb.lookup(f"{d['word']}+Verb+Past+A2sg")[0][0]))
        print("Ew",erase_duplicate(kurdish_verb.lookup(f"{d['word']}+Verb+Past+A3sg")[0][0]))
        print("Em",erase_duplicate(kurdish_verb.lookup(f"{d['word']}+Verb+Past+A1pl")[0][0]))
        print("Hun",erase_duplicate(kurdish_verb.lookup(f"{d['word']}+Verb+Past+A2pl")[0][0]))
        print("Ew",erase_duplicate(kurdish_verb.lookup(f"{d['word']}+Verb+Past+A3pl")[0][0]))

def print_result(verb, tense="all"):
  correct_verb = autocorrect(verb)
  i=find(data, "word", correct_verb)
  get_info(data[i], tense)

# TEST CASES

print_result("acizbûn") #intransive and a compound verb

print_result("ditin") # if the user misspell a verb, autocorrect function start to work and gives response.

print_result("dîtin", tense="past") #if the user tense parameter into function, it only gives the tense that the user put