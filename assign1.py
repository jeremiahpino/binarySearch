import sys

# get text file argument 
infile = sys.argv[1]

# open text file for reading
txtFile = open(infile, "r")

# read text file content
fileContent = txtFile.read()

# put content of file into list 
clist = fileContent.split(",")

# close text file
txtFile.close()

min = 0
max = len(clist) - 1

# call binary search
def bsearch(list1, min, max):
    
    mid = (max + min) // 2

    if min <= max:
        # if mid equals length of list 
        if(mid == len(list1) - 1):
            return list1[mid]
        
        # odd and mid index does NOT equal next index (EXPECTED)
        # singleton is right subsection
        elif(mid % 2 != 0) and (list1[mid] != list1[mid + 1]):
            return bsearch(list1, mid + 1, max)

        # odd and mid index equals next index (NOT EXPECTED)
        # singleton is in left subsection
        elif(mid % 2 != 0) and (list1[mid] == list1[mid + 1]):
            return bsearch(list1, min, mid - 1)

        # even and mid index does NOT equal next index (NOT EXPECTED)
        # singleton is in left subsection
        elif(mid % 2 == 0) and (list1[mid] != list1[mid + 1]):
            return bsearch(list1, min, mid - 1)

        # even and mid index does equal next index (EXPECTED)
        # singleton is in right subsection
        elif(mid % 2 == 0) and (list1[mid] == list1[mid + 1]):
            return bsearch(list1, mid + 1, max)
    return list1[min]

lone = bsearch(clist, min, max)

if(lone):
    print(lone)
    