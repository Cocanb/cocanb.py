# by nonka

# original just in case i fuck up
# def toc(sentence):
#     initial = sentence.split()
#     additional = ""
#     for i in initial:
#         additional += i[-1] + chr(ord('`') + len(i))
#         initial[initial.index(i)] = i[:-1]
#     final = "".join(initial) + "non" + additional
#     return final

def toc(sentence):
    initial = sentence.split()
    additional = ""
    nums = []
    for i in initial:
        if i.isnumeric():
            nums.append(i)
            i = "<num>"
    for i in initial:
        if (i[0] != "<" and i[-1] != ">"):
            additional += i[-1] + ("å" * (len(i) // 26)) + chr(ord('`') + (len(i) % 26))
            initial[initial.index(i)] = i[:-1]
    final = "".join(initial) + "non" + additional
    final = final.replace("<", " <").replace(">", "> ")
    return final