#IMPORTANT: MUST BE RUN IN VIRTUAL ENVIRONMENT
#DON´T FORGET TO CLOSE VIRTUAL ENVIRONMENT AFTER DONE!!!

# Extract text from PDF
# package pdfminer.six
# run from directory in terminal

import re
from pdfminer.high_level import extract_pages, extract_text

filename="Lektion-4-Funktioner och modulär programmering.pdf"

text = extract_text(filename)

#REGEX - regular expressions


pattern_1 = re.compile(r'1. Modulär textomvandlare')
pattern_2 = re.compile(r'2. Filtrera lista med funktioner')
matches_1 = pattern_1.finditer(text)
matches_2 = pattern_2.finditer(text)


for match in matches_1:
    print(match)


