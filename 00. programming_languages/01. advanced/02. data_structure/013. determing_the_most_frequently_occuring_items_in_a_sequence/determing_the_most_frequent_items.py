from collections import Counter
words = [
    'look', ('into','dssd'), 'my', 'eyes', 'look', 'into', 'my'
]
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)