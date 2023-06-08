# Kurmanji Conjugator
The project addresses the limitations of existing alternatives by providing a user-friendly and feature-rich tool for generating accurate verb forms across various tenses and transitivity patterns in the Kurdish language.

The primary objective of the project is to create a reliable resource that assists Kurdish language learners, researchers, and native speakers in conjugating verbs with precision. The development of an enhanced Kurdish verb conjugator with autocorrection is a significant contribution to overcoming the scarcity of practical data and resources available for accurate verb conjugation in Kurmanji.

## Usage
Kurmanji Conjugator is written in Python

Here are the some test cases:

- print_result("acizbûn") #intransive and a compound verb

- print_result("ditin") # if the user misspell a verb, autocorrect function start to work and gives response.

- print_result("dîtin", tense="past") #if the user tense parameter into function, it only gives the tense that the user put  

**Here is the output:**
```
> Min dît. (I saw)

> Te dît. (You saw)

> Ew dît. (She saw)
```
