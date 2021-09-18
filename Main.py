"""
Abbreviations
Message Analysis
"""
# Declare Dictionary
abbreviationsDictionary = {
 "afaik": "as far as i know",
 "aka": "also known as",
 "ama": "ask me anything",
 "amaa": "ask me almost anything",
 "asap": "as soon as possible",
 "atm": "at the moment",
 "bae": "before anyone else",
 "b4n": "bye for now",
 "bbl": "be back later",
 "bc": "because",
 "b/c": "because",
 "bday": "birthday",
 "bff": "best friend forever",
 "brb": "be right back",
 "btw": "by the way",
 "cob": "close of business",
 "cya": "see ya",
 "cyt": "see you tomorrow",
 "dae": "does anybody else",
 "diky": "do i know you?",
 "diky": "do i know you",
 "diy": "do it yourself",
 "dm": "direct message",
 "eod": "end of day",
 "f2f": "face to face",
 "fomo": "fear of missing out",
 "ftfy": "fixed that for you",
 "ftw": "for the win",
 "fwiw": "for what it's worth",
 "fyi": "for your information",
 "gtg": "got to go",
 "g2g": "got to go",
 "gr8": "great",
 "hbu": "how about you?",
 "hbu": "how about you",
 "hifw": "how I feel when",
 "hmu": "hit me up",
 "hth": "hope this helps",
 "icymi": "in case you missed it",
 "idc": "i don't care",
 "idk": "i don't know",
 "ifyp": "i feel your pain",
 "ig": "instagram",
 "iirc": "if i recall correctly",
 "ikr": "i know right",
 "ilysm": "i love you so much",
 "ily": "i love you",
 "imo": "in my opinion",
 "imho": "in my humble opinion",
 "imho": "in my honest opinion",
 "irl": "in real life",
 "istg": "i swear to god",
 "iykyk": "if you know you know",
 "jic": "just in case",
 "jk": "just kidding",
 "jsyk": "just so you know",
 "kmn": "kill me now",
 "lmk": "let me know",
 "mfw": "my face when",
 "mrw": "my reaction when",
 "msg": "message",
 "nbd": "no big deal",
 "ngl": "not gonna lie",
 "np": "no problem",
 "nth": "nice to have",
 "nvm": "never mind",
 "ofc": "of course",
 "omg": "oh my god",
 "oml": "oh my lord",
 "omw": "on my way",
 "ooo": "out of office",
 "ootd": "outfit of the day",
 "otoh": "on the other hand",
 "pnl": "peace and love",
 "pov": "point of view",
 "ppl": "people",
 "qap": "quick as possible",
 "qotd": "quote of the day",
 "rn": "right now",
 "rofl": "rolling on the floor laughing",
 "rofl": "rolling on floor laughing",
 "sflr": "sorry for late reply",
 "smh": "shaking my head",
 "snmp": "so not my problem",
 "srsly": "seriously",
 "sus": "suspicious",
 "tba": "to be announced",
 "tbc": "to be continued",
 "tbd": "to be decided",
 "tbd": "to be determined",
 "tbf": "to be frank",
 "tbh": "to be honest",
 "tfw": "that feeling when",
 "tgif": "thank goodness it's friday",
 "tgif": "thank god it's friday",
 "thx": "thanks",
 "tia": "thanks in advance",
 "til": "today i learned",
 "tl;dr": "too long; didn't read",
 "tl;dr": "too long; don't read",
 "tmi": "too much information",
 "ttp": "to the point",
 "ttyl": "talk to you later",
 "ty": "thank you",
 "tyt": "take your time",
 "wdym": "what do you mean?",
 "wdym": "what do you mean",
 "wfh": "work from home",
 "w/o": "without",
 "wywh": "wish you were here",
 "ygti": "you get the idea",
 "ymmv": "your mileage may vary",
 "yolo": "you only live once",
 "yp": "yes please",
 "afk": "away from keyboard",
 "aamof": "as a matter of fact",
 "aap": "always a pleasure",
 "atb": "all the best",
 "afaic": "as far as i'm concerned",
 "bf": "boyfriend",
 "gf": "girlfriend",
 "bg": "background",
 "b/f": "boyfriend",
 "g/f": "girlfriend",
 "b/g": "background",
 "bif": "before i forget",
 "bsts": "better safe than sorry",
 "btdt": "been there, done that",
 "btdt": "been there done that",
 "ezy": "easy",
 "sm": "so much",
 "lmao": "laughing my a** off",
 "lmfao": "laughing my f**k*** a** off",
}
# Chatbot Intro

print("Hello! My name is 404 Bot. You can use me to convert phrases in your message into texting abbreviations and vice versa.")
print("I hope I can be of use in bridging the gap in communication between generations.")

# Conditional Statements
boolean = "Yes"
while boolean == "Yes":
  print("Analysis Method: ATM - Acronym To Message, MTA - Message To Acronym")
  analysisMethod = str(input("Analysis Method: "))
  while analysisMethod != "ATM" and analysisMethod != "MTA":
    analysisMethod = str(input("Analysis Method: "))

  userMessage = str(input("Enter Message: "))
  if analysisMethod == "ATM":
    for key in abbreviationsDictionary:
      try:
        userMessage = userMessage.casefold()
        userMessage.index(key)
      except ValueError:
        pass
      else:
        replace = abbreviationsDictionary.get(key)
        userMessage = userMessage.replace(key, replace)

  elif analysisMethod == "MTA":
    list1 = list(abbreviationsDictionary.values())
    for value in list1:
      try:
        value = value.casefold()
        userMessage.index(str(value))
      except ValueError:
        pass
      else:
        replace2 = (list(abbreviationsDictionary.keys())[list(abbreviationsDictionary.values()).index(str(value))])
        userMessage = userMessage.replace(str(value), replace2)

  if boolean == "Yes":
    print(userMessage)
  else:
    pass

  boolean = input("Do you want to enter another message? ")
  if boolean == "No":
    print("Thank you! You just got a taste of the future of communication.")


