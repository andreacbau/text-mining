# PART 01 
# Data Source Chosen: Wikipedia

from mediawiki import MediaWiki

wikipedia = MediaWiki()
AI_progress = wikipedia.page("Progress in artificial intelligence")

print(AI_progress.title)

print(AI_progress.content)

print(AI_progress.url)

print(AI_progress.images[1])

text = AI_progress.content
print(text)


# PART 02 --

# Characterizing by Word Frequencies

wordlist = text.split()
wordfreq = []

for w in wordlist:
    wordfreq.append(wordlist.count(w))

# Print text string from article text
print("String\n" + text +"\n")

# Print text string as list of words in article
print("List\n" + str(wordlist) + "\n")

# Print frequencies of words in list in respective order (following order of the word list not in descending 
# ascending order)
print("Frequencies\n" + str(wordfreq) + "\n")

# Print pairs of words and frequencies together
print("Pairs\n" + str(list(zip(wordlist, wordfreq))))


# Characterizing by word frequencies descending order 

from collections import Counter

# Create list of all the words in text string 

split_text = text.split()
print(split_text)

# pass the split_text string to Counter class 

Counter = Counter(split_text)

# most_common(n) will return a list of the n most common elements and their 
# respective counts in descending order 

word_frequencies_descending = Counter.most_common(5)

print(word_frequencies_descending)


# Stemmming Text

# tokenizers can be used to find the words and punctuation in a string

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize


ps = PorterStemmer()

for word in split_text:
    print(ps.stem(word))

#Stopwords 

import nltk 

nltk.download('stopwords')

from nltk.corpus import stopwords

# See list of stopwords
from nltk.tokenize import word_tokenize

stops = set(stopwords.words('english'))
print(stops)

word_tokens = word_tokenize(text)

filtered_text = [w for w in word_tokens if not w in stops]

filtered_text = []

for w in word_tokens:
    if w not in stops:
        filtered_text.append(w)

print(word_tokens)

print(filtered_text)



