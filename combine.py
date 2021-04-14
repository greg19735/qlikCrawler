import os
import glob
import config

print('hello')

path =  config.path
crawledLinksDir = path + "\\crawledLinks"

dirList = []

#get all directories with crawled stuff
for root, dirs, files, in os.walk(crawledLinksDir, topdown=False):
    for name in dirs:
        dirList.append(os.path.join(root, name))

dirCount = 0

for dir in dirList:

    #output file
    outputFileName = dir + '/combined' + str(dirCount)
    dirCount= dirCount + 1


    #get files in array
    filenames = []
    os.chdir(dir)
    for file in glob.glob("*.txt"):
        filenames.append(file)

    #combined
    with open(outputFileName, 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                lineCount = 0
                for line in infile:
                    if(lineCount!= 0):
                        outfile.write(line)
                    lineCount = lineCount + 1





print(dirList)