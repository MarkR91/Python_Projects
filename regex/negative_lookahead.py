""" Use negative lookahead assertion:

^(?!.*ifdf).*$
"""

import re

lines = ["Hello", "Line with ifdf", "No ifdf on this line", "Last line"]

pattern = re.compile(r"^(?!.*ifdf).*$")

for line in lines:
    if pattern.match(line):
        print(line)
