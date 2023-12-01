# regular expression in python
import re
pattern = "was"
text = '''
lorem33
dkjfadkfaosdnonv was


'''

match = re.search(pattern, text)
print(match)