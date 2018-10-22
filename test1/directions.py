def make_direction(secret):
    def direction(path):
      if path < secret:
        return +1
      elif path > secret:
        return -1
      return 0
    return direction

