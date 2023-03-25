from collections import Counter
text = "creo que a veces es la gente de la que nadie espera nada, la que hace cosas que nadie puede imaginar"
list_text = list(text.lower().split())
count_text = Counter(list_text)
print(dict(count_text))

text = "creo que a veces es la gente de la que nadie espera nada, la que hace cosas que nadie puede imaginar"
list_text = list(text.lower().split())
dict_t = dict()
for i in list_text:
    if i in dict_t:
        dict_t[i] += 1
    else:
        dict_t[i] = 1
print(dict_t)