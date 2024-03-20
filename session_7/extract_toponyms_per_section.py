from openiti.helper.funcs import get_semantic_tag_elements
import regex

# load the text:
path = "0346Istakhri.MasalikWaMamalik.Shamela0011680-ara1.mARkdown"
with open(path, encoding="utf8") as file:
    text = file.read()

# print the toponyms per section 
# (only print the section title if it contains toponyms):
for section in text.split("### "):
    # find the toponyms in this section:
    toponyms = get_semantic_tag_elements("TOP", section)
    # print the toponyms + section header only if toponyms were found:
    if len(toponyms) > 0:
        # get the section header (= the first line of the section): 
        header = section.split("\n")[0]
        # print the section header and the toponyms found in it:
        print(header)
        print(toponyms)
