import sys
import json 

if len(sys.argv) == 2:
    command = sys.argv[1]
    if command == "save":
        print("save")
    elif command == "load":
        print("load")
    elif command == "del":
        print("delete")
    else:
        print("That command is unknown.")