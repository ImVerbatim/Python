def replace_all(d,x,y):
  for key in d:
    if d[key] == x:
      d[key] = y
  return d
