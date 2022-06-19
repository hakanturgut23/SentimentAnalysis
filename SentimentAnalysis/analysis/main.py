import string
from collections import Counter

import matplotlib.pyplot as plt

text = open("analysis/metin.txt", encoding="utf-8").read()

lower_case = text.lower()

cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

tokenized_words = cleaned_text.split()


final_words = []
for word in tokenized_words:
        final_words.append(word)

duygu_list = []
with open('analysis/duygu.txt', 'r') as file:
    for line in file:
        print(line)
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        if word in final_words:
            duygu_list.append(emotion)

print(duygu_list)
w = Counter(duygu_list)
print(w)


fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()