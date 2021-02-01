from dtl.main import dtl
# file for main menu
def start():
  command = ""
  while(command != "exit"):
    help()
    command=input(">> ")
    print()
    if(command == "1"):
      dtl().menu()

def help():
  print("Menu:")
  print("1. dtl")
  print("Type a number to explore its functionality")
  print("type 'exit' (without the quotes) to quit")

if(__name__ == "__main__"):
  start()