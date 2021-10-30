## **Part 3: Project Write Up and Reflection**

*In this Assignment I was asked to access text from the web and social media source in order to run some 
sort of computational analysis on it. The Data Source that I chose to work with was Wikipedia. I first went 
on the Wikipedia website and chose an article of my preference titled “Progress in artificial intelligence.” 
The technique that I used to process this data source was  by using the python mediawiki package in order to 
search Wikipedia, obtain article summaries in Part 2, get different data like the URL link of the article and 
images from the article and more. To get this package, I ran a command in the Command Prompt. Once I processed 
the article/text in python, I proceeded to analyze the text in Part 2. Some of the techniques I used in order to 
analyze the text was Natural Language Processing, computing summary statistics, and so on. Throughout this 
Assignment I hoped to learn how to use python in order to find information in a much faster and efficient way, 
how to manipulate text through a system that I created myself, and I hoped to create a system that can assist both 
myself and others when exploring certain texts more in depth.*#


First, I set forth in choosing an article and downloading the mediawiki extension in order to process the article. 
I then opened and ran the article and printed out its sections. I then set forth in printing out its title, content, 
an image, and the URL to get familiar with what I will be working with/manipulating. Next, I moved on to Part 2 where
I began to brainstorm which techniques I was going to use to analyze, process, and compute language analysis. The first 
thing I decided to do was characterize the text by frequencies. I converted the text into a word list in order to count 
the frequency of each word. It was easy to process the list using a for loop. I then created a list that was empty at first 
to run through each word in the list, and keep count of the number of times that each respective word appears in the whole 
list. I then added all of the word counts to a frequency list. I then implemented the Zip operation which I learned more 
about in youtube which allowed me to match the first word that appeared on the word list with the first respective number 
on the frequency list I made and the same for the other words and frequencies. The result was a list of pairs consisting 
of the words and their respective frequency counts. This was a fun start! 


Following, I wanted to take my text analysis a step further and decided to characterize by word frequencies in descending 
order. In order to do so I had to import Counter. I used counter as it will hold the count of each of the elements present 
in the container. Counter is a sub-class available inside the dictionary class. Using this, I was able to count the key-value 
pairs in an object, aka a hashtable object. I wrote it in such way that one can choose to see the top 2, 3, 4, 5, . . . etc. 
most common words in the text and their respective frequencies for anyone who wishes to see only the top 4 or the top 30. In 
order to do this I used most_common(n) which returns a list of the n most common words in the text, I learned this in google 
when exploring the counter. 


Another thing I decided to do was some Natural Language Processing using NLTK which is the Natural Language Toolkit which is 
useful in python when working with human language data. I proceeded to experiment with stop words. First, I had to Install nltk 
by running a command in Command Prompt. Then I imported nltk into my python file and downloaded stopwords and printed them in 
order to see the list of English stop words and familiarize myself with the content. I also imported word_tokenize from 
nltk.tokenize. Tokenizers can be used to find the words and punctuations in a text. I learned that it is useful for splitting 
sentences/text into words and I did that with the article text. Then I filtered the text by showing all words that are not stop 
words in a new list and printed it. 

Overall throughout this project and from my text analysis I found a selection of interesting things. For example the most 
frequent words in the article were ('of', 44), ('the', 36), ('and', 32), ('to', 29), ('a', 24)]. This was an interesting find 
for me because since I personally carefully chose an article about artificial intelligence I assumed that the top most frequent 
words would be key words someone would use when searching the web for articles/information about Artificial intelligence however, 
the most frequent words resulted to be common words we use to make sentences flow. Another interesting thing I found is that you 
could retrieve the URL of an image from a Wikipedia article using python code as I did. For example I found the url for image: 
https://upload.wikimedia.org/wikipedia/commons/7/7a/Anatomy-1751201_1280.png. On the terminal, one can click on the link and it 
takes you directly the the link of the image. 

Another interesting thing I was able to obtain and learn from this project was from exploring the stopwords with NLTK. From 
research in pythonprogramming.net I learned that the main essence of Natural Language Processing is to conduct some form of 
analysis, or processing where one/a machine can better understand what the text implies or says. In the human language we know 
some words carry more meaning than others, aka some words are just fluff words. Using NLTK and stopwords in python allowed me 
to write a system that can help filter out some of those words that can take up unencessary space in databases or increase 
processing time which is valuable to my understanding! I learned how to remove stopowrds from the article by first importing 
the list of stopwords from NLTK. I then processed the system and the output showed a filtered article without the stopwords 
which helps when trying to skim for key words faster. I also stemmed the words with NLTK however it id not yield very exciting 
results. Stemming is mostly like a normalizing method for many variations of words or phrases that carry the same meaning other 
than the tense being used however, for this article it was not of immense use.  

4. Reflection [~1 paragraph] From a process point of view, what went well? What could you improve? Other possible reflection topics: Was your project appropriately scoped? Did you have a good plan for testing? How will you use what you learned going forward? What do you wish you knew before you started that would have helped you succeed?

This project was very challenging but also fun! From a process point of view, it was very tedious in the sense that every step must 
be perfect because it may impact the rest of the script. At first, it took me some time to do some research on my own to figure out 
what I wanted to do and how I was going to execute that. Once I set my gameplan I began experimenting with differnet way to analyze 
the text and I did run into hundreds of errors but it was a fun challenge figuring out how to overcome them. I did use the professor's
help for a few of the errors but I was able to fix them and proceed. It was fun installing and getting to know how to use different 
python extensions such as mediawiki and nltk since I was not nearly very familiar with them. I would have loved to play around and 
explore more ways to analyze and process the text but because I am new to programming I spent more time trying to make sure I understood
what I was doing a long the way. I will now use what I have learned to simplify more of my other code and apply it to any future projects, including the group project or any personal coding/python projects I wish to pursue. Before I started I wish I would have spent more time 
exploring different python resources in order to be more prepared to analyze and process the text. Overall It was a fun assignment! Thanks 
professor. 

