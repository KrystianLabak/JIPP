import re
from collections import Counter

text = "Is we miles ready he might going. Own books built put civil fully blind fanny. Projection appearance at of admiration no. As he totally cousins warrant besides ashamed do. Therefore by applauded acuteness supported affection it. Except had sex limits county enough the figure former add. Do sang my he next mr soon. It merely waited do unable."

list_of_words = text.split()
print(list_of_words)
num_of_words = len(list_of_words)
print(num_of_words)
num_of_sentences = re.split(r'[.?!]+', text)
print(len(num_of_sentences))
num_of_paragraphs = text.split('\n')
print(len(num_of_paragraphs))
counter = Counter(list_of_words)
mostWords = counter.most_common(2)
print(mostWords)

def reverse(list,word):
    for x in list:
        if x[0] == 'a' or x[0] == 'A':
            x = x[slice(None,None, -1)]
        word.append(x)

reversed_words = []
reverse(list_of_words,reversed_words)
print(reversed_words)