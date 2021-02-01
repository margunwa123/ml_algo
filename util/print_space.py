class print_space:
  def __init__(self, space):
    self.space = space

  def print(self, word):
    print(" " * self.space, end="")
    print(word)
  
  def input(self):
    return input(" " * self.space + ">> ")
