import os

def getRoot():
    utilitiesFolderPath = os.path.dirname(__file__)
    # Make sure it's the real path
    utilitiesFolderPath = os.path.realpath(utilitiesFolderPath)
    # Now need to find the 'repl_python' folder in there
    pieces = utilitiesFolderPath.split('/')
    # find index of our root folder
    rootPos = [i for i in range(len(pieces)) if pieces[i].lower() == "repl_python"]
    # take the pieces from 0 to rootPos
    rootPieces = pieces[0-rootPos]
    rootPath = os.path.join("/", rootPieces)
    return rootPath

def getOutputFolderPath()->str:
    rootPath = getRoot()
    outputPath = os.path.join(rootPath, "output")
    return outputPath

def getOutFilePath(filename: str)->str:
    outPath = getOutputFolderPath()
    filePath = os.path.join(outPath, filename)
    return filePath


