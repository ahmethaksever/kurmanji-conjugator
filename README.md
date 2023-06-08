# Kurmanji Conjugator
The project addresses the limitations of existing alternatives by providing a user-friendly and feature-rich tool for generating accurate verb forms across various tenses and transitivity patterns in the Kurdish language.

The primary objective of the project is to create a reliable resource that assists Kurdish language learners, researchers, and native speakers in conjugating verbs with precision. The development of an enhanced Kurdish verb conjugator with autocorrection is a significant contribution to overcoming the scarcity of practical data and resources available for accurate verb conjugation in Kurmanji.

## Usage
Kurmanji Conjugator is written in Python

Here are the some test cases:

- print_result("acizbûn") #intransive and a compound verb

**Output:**
```
Ez aciz dibim
Tu aciz dibî
Ew aciz dibe
Em aciz dibin
Hun aciz dibin
Ew aciz dibin
Ez ê acizbibim
Tu ê acizbibî
Ew ê acizbibe
Em ê acizbibin
Hun ê acizbibin
Ew ê acizbibin
Ez aciz bûm
Tu aciz bû
Ew aciz bû
Em aciz bûn
Hun aciz bûn
Ew aciz bûn
```

- print_result("ditin") # if the user misspell a verb, autocorrect function start to work and gives response.

**Output:**
```
Did you mean one of the following verbs?
1. dîtin
2. dotin
Please enter the number of the verb you choose: 1
Ez  dibînim
Tu  dibînî
Ew  dibîne
Em  dibînin
Hun  dibînin
Ew  dibînin
```

- print_result("dîtin", tense="past") #if the user tense parameter into function, it only gives the tense that the user put  

**Output:**
```
Min ew  dît
Te ew  dît
Wi/wê ew  dît
Me ew  dît
We ew  dît
Wê ew  dît
```
