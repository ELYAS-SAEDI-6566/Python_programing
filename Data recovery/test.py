import os , sys , glob

#The path of the current script
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

#geting names and path of document files
txtfiles = []
for file in glob.glob(f'{script_directory}\\Documents\\*.txt'):
    #txtfiles.append(os.path.basename(file))
    txtfiles.append(file)

#Opening and reading document files
with open(txtfiles[0]) as f:
    content = f.read()
    
#print(content.count('hello'))

for targetFile in txtfiles:
    with open(targetFile) as f:
        content = f.read()
    print(os.path.basename(targetFile) + " " + str(content.count('art')))