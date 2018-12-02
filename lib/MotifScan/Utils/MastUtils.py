#BuildMastCommand
#RunMastCommand
#ParseMastOutput
import os

def BuildMastCommand(motifpath,fastapath):
    mastDirPath = '/kb/module/work/tmp/mast_out'
    MastStr = 'mast -oc ' + mastDirPath + ' ' + motifpath + ' ' + fastapath
    return MastStr

def RunMastCommand(commandstr):
    os.system(command)
    return None

def ParseMastOutput():
    mastDirPath = '/kb/module/work/tmp/mast_out'
    mastTxtPath = mastDirPath + '/' + 'mast.txt'
    mastFile = open(mastTxtPath,'r')

    readMotifID = False

    for line in mastFile:
        if '----- ----------------------------- ------ ----- -------------------' in line:
            break
    line = mastFile.readline()
    motifDict = {}
    while(len(line.split()) != 0):
        #parse Motif
        elems = line.split()
        motifDict[elems[0]] = elems[1]
        line = mastFile.readline()
    for line in mastFile:
        if 'SECTION II' in line:
            break
    for line in mastFile:
        if '-------------                      --------  -------------' in file:
            break
    #ASSUME SEQUENCE NAME UNGAPPED
    line = mastFile.readline()
    sequenceDict = {}
    #key -> sequence name
    #value ->
    while(len(line.split()) != 0):
        #stuff
        elems = line.split()
        #positions = elems[2].split('-')
        position = 0
        #bool for motif
        #bool for offset
        diagramLen = len(elems[2])
        motifPos = 0
        diagpos = 0
        parseWidth = False
        start = 0
        while(diagpos != diagramLen):
            if elems[2][diagpos] == '[':
                diagpos +=1
                while(elems[2][diagpos] != ']'):
                    fs
                #parse the motif location
            if elems[2][diagpos] == '<':
                diagpos +=1
                while(elems[2][diagpos] != '>'):
                    sf
                #parse location
            if elems[2][diagpos] == '-':
                parseWidth = False
                width = int(elems[2][start:diagpos])
                motifPos += width
                #parse
            if elems[2][diagpos].isnumeric() and parseWidth is False:
                start = diagpos
                parseWidth = True
            diagpos += 1
        for c in elems[2]:
            if '[' in p:
                id = int(p.replace('[','').replace(']',''))

            else:
                position += int(p)
        line = mastFile.readline()
