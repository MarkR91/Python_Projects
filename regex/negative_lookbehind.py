"""Use negative lookbehind assertion:

^.*(?<!ifdf)$
"""

import re

lines = [
    "Hello world",
    "This line has abc",
    "Another line without ifdf",
    "Last line has ifdf",
]

pattern = re.compile(r"^((?!.*ifdf).*)$")

for line in lines:
    if pattern.match(line):
        print(line)
