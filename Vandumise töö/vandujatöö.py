import re
pahad = "mets"
lause = "See on lause kust tuleb eemaldada sõna metsa"

leid = re.findall("mets\w*", lause)

print(re.sub("("+pahad+")\w*", "*" * len(pahad), lause))