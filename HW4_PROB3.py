import os, glob
import re
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

p = re.compile("<p data-testid=\"vuln-description\">(.*\n*)<\/p>")

noun = {}
verb = {}

folder_path = './Problem3_html_files/'
for filename in glob.glob(os.path.join(folder_path, '*.html')):
    with open(filename, 'r', encoding='UTF-8') as f:
        html = f.read()
        desc = p.search(html).group(1).replace("&#39;", "'")
        tagged = nltk.pos_tag(nltk.word_tokenize(desc))
        
        for word, tag in tagged:
            if tag[0] == 'N':
                if word in noun:
                    noun[word] += 1
                else:
                    noun[word] = 1

            if tag[0] == 'V':
                if word in verb:
                    verb[word] += 1
                else:
                    verb[word] = 1

noun = sorted(noun.items(), key = lambda item: item[1], reverse = True)
verb = sorted(verb.items(), key = lambda item: item[1], reverse = True)

i = 1
print('noun:')
for word, count in noun[:10]:
    print(str(i) + ". \"" + word + "\" -  " + str(count))
    i += 1

i = 1
print('verb:')
for word, count in verb[:10]:
    print(str(i) + ". \"" + word + "\" -  " + str(count))
    i += 1