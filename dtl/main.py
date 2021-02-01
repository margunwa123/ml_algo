from util.print_space import print_space

class dtl(print_space):
  def __init__(self):
    print_space.__init__(self, 2)
  
  def menu(self):
    command = ""
    while(command != "3"):
      self.print("DTL ------")
      self.print("1. entropy")
      self.print("2. gain")
      self.print("3. back")
      command = self.input()
      if(command == "1"):
        self.entropy()
      elif(command =="2"):
        self.gain()
      print()

  def entropy(self):
    # get user input dengan self.input() untuk spacing yang lebih
    pass
  def gain(self):
    # get user input dengan self.input() untuk spacing yang lebih
    pass
