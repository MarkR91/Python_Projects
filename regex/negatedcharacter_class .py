"""
Use negated character class regex:

^[^i]*$
```

"""


import re

lines = ["Hello", "if", "Another line", "Start"]

pattern = re.compile(r"^[^i]*$")

for line in lines:
    if pattern.match(line):
        print(line)
