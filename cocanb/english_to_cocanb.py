def english_to_cocanb(sentence):
    initial = sentence.split()
    additional = ""
    for i in initial:
        additional += i[-1] + chr(ord('`') + len(i))
        initial[initial.index(i)] = i[:-1]
    final = "".join(initial) + "non" + additional
    return final