import json

ar = []

with open('mat.txt', 'r' ) as f:
    for i in f:
        n = i.lower().split(', ')
        if n != ' ':
            ar.append(n)


with open('mat.json', 'w', encoding='utf-8') as e:
    json.dump(ar,e, ensure_ascii=False)