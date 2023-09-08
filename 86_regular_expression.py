<<<<<<< HEAD
import re

mystr ='''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
gaurav now work is open
work as nowwww'''

# findall, search, split, sub, finditer
# patt = re.compile(r'faas')
# patt = re.compile(r'.adm')
# patt = re.compile(r'^Tata')
# patt = re.compile(r'now$')
# patt = re.compile(r'no+')
# patt = re.compile(r'no{2}{1}')
# patt = re.compile(r'no{2}{1}')
patt = re.compile(r'no{1}|Fax')


# Special Sequences
# patt = re.compile(r'\bFax')
# patt = re.compile(r'27\b')
# patt = re.compile(r'\d{5}-\d{4}')

# Task
# Given a string with a lot of indian phone numbers starting from +91
# patt = re.compile(r'+91\b')

matches = patt.finditer(mystr)
for match in matches:
=======
import re

mystr ='''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
gaurav now work is open
work as nowwww'''

# findall, search, split, sub, finditer
# patt = re.compile(r'faas')
# patt = re.compile(r'.adm')
# patt = re.compile(r'^Tata')
# patt = re.compile(r'now$')
# patt = re.compile(r'no+')
# patt = re.compile(r'no{2}{1}')
# patt = re.compile(r'no{2}{1}')
patt = re.compile(r'no{1}|Fax')


# Special Sequences
# patt = re.compile(r'\bFax')
# patt = re.compile(r'27\b')
# patt = re.compile(r'\d{5}-\d{4}')

# Task
# Given a string with a lot of indian phone numbers starting from +91
# patt = re.compile(r'+91\b')

matches = patt.finditer(mystr)
for match in matches:
>>>>>>> 8ad8ee1 (Add initial files)
    print(match)