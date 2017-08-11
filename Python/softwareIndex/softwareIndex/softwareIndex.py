
import sys

try:
    file_name = r"C:\Users\lixin\OneDrive\Documents\softwareIndex.txt"
    with open(file_name, "r") as file:
        mydict = {}
        for line in file:
            mylist = []
            mylist = line.split('/')
            length = len(mylist)
            if length > 1:
                if mylist[length - 2].lower() in mydict:
                    mydict[mylist[length - 2].lower()].append(mylist[length - 1].lower())
                else:
                    mydict[mylist[length - 2].lower()] = []
                    mydict[mylist[length - 2].lower()].append(mylist[length - 1].lower())
            else:
                mylist2 = []
                mylist2 = mylist[length - 1].split('-', maxsplit=1)
                if len(mylist2) > 1:
                    if mylist2[0].lower() in mydict:
                        mydict[mylist2[0].lower()].append(mylist2[1].lower())
                    else:
                        mydict[mylist2[0].lower()] = []
                        mydict[mylist2[0].lower()].append(mylist2[1].lower())
                else:
                    if mylist2[length - 1].lower() in mydict:
                        mydict[mylist2[length - 1].lower()].append(mylist2[length - 1].lower())
                    else:
                        mydict[mylist2[length - 1].lower().strip()] = [mylist2[length - 1].lower()]
    f = open("resultList", "w")
    for key, value in sorted(mydict.items()):
        if len(value) > 0:
            f.write(key + "\n")
            print(key + "\n")
            for version in value:
                f.write("\t" + version)
                print("\t" + version)
    f.close()
    sys.exit()
except IOError:
    print ("There was an error for reading", file_name)
    sys.exit()