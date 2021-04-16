# -*- coding: utf-8 -*-

import re

f = open("data.txt", "r")
data = f.read()
f.close()

all_words = re.findall(r'\w+', data)

print(len(all_words))

