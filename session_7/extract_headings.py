


import regex

# load the text:
path = "0346Istakhri.MasalikWaMamalik.Shamela0011680-ara1.mARkdown"
with open(path, encoding="utf8") as file:
    text = file.read()

print(text[:500])

# extract headings from the text:

pattern = "### \|+ .+"
headings = regex.findall(pattern, text)

for heading in headings[0:10]:
    print(heading)


with open("headings.csv", mode="w", encoding="utf8") as file:
    for heading in headings:
        file.write(heading+"\n")
