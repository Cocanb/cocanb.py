import re

class Sentence:
  def __init__(self, string, punc):
    self.string = string
    self.punc = punc
  def join(self):
    return self.string + self.punc

def split_sentences(_input):
  str_list = re.split("[.!\?\n]", _input.strip())
  if not str_list[-1]: # idek
    str_list = str_list[:-1]
  for i in str_list:
    i = i.strip()
  punc_list = []
  for i in _input:
    if i in [".", "!", "?", "\n"]:
      punc_list.append(i)
  output = [None] * len(str_list)
  for i in range(len(str_list)):
    output[i] = Sentence(str_list[i], punc_list[i])
  return output

def join_sentences(_input):
  output = ""
  for i in _input:
    output += i.join() + " "
  return output

