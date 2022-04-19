import re

txt = "Hello my name is Ali Ali.\nhello, hello!\ngood- good not? not"
# regex_str = r"\b([^\s]+)[,]?\s\1\b"
punctuation_sep = ',\\.-?:_!'
regex_str = f"\\b([^\\s]+)[{punctuation_sep}]?(\\s+\\1\\b)"
regex = re.compile(regex_str)
matcher = regex.match(txt)

print(regex.findall(txt))