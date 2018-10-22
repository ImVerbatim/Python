def freq(sentence):
  d = {}
  for x in sentence:
    if x not in d:
      d[x] = 1
    else:
      d[x] += 1
  return d


print freq('Star Wars')

