# open()
################# Read Mode ##################
# file1=open('textfile.txt','r')
#
# for i in file1:
#     print(i)
# #textsting=file1.readlines()
# textsting=file1.read()
# #textsting=file1.readline(7)
# print((textsting))
# file1.close()


# with open('textfile.txt','r') as fileobject:
#     print(fileobject.readlines())


##################### write mode ####################

# with open("writetextfile.txt",'a') as fileobject:
#     fileobject.write("this is python\n")
#     fileobject.write("this is python class\n")
#     fileobject.write("this is python learing\n")
#     # fileobject.write("this is python learing new version\n")



##################### Binaryh file mode ####################
with open("Lato-Regular.bin", 'r+b') as fileobject:
    print(fileobject.readline())

