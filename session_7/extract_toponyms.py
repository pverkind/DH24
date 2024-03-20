from openiti.helper.funcs import get_semantic_tag_elements

# load the text:
path = "0346Istakhri.MasalikWaMamalik.Shamela0011680-ara1.mARkdown"
with open(path, encoding="utf8") as file:
    text = file.read()

print(text[:500])

# extract toponyms from the text:
toponyms = get_semantic_tag_elements("@TOP", text)

# print the toponyms:
print(toponyms[:10])

for top in toponyms[:100]:
    print(top)
