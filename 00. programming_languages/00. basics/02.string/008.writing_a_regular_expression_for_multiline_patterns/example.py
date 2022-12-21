
# Regular expression that matches multiline patterns

import re

text = '''/* this is a
              multiline comment */
'''
comment_1 = re.compile(r'/\*(.*?)\*/')
comment_2 = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment_1.findall(text))
print(comment_2.findall(text))
