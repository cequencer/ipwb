import os
import random
import string


def createUniqueWARC():
    lines = []
    warcInFilename = 'frogTest.warc'
    warcInPath = os.path.join(os.path.dirname(__file__) + '/samples/warcs/' +
                              warcInFilename)

    stringToChange = 'abcdefghijklmnopqrstuvwxz'
    randomString = getRandomString(len(stringToChange))

    with open(warcInPath, 'r') as warcFile:
        newContent = warcFile.read().replace(stringToChange, randomString)

    warcOutFilename = warcInFilename.replace('.warc', '_' +
                                             randomString + '.warc')
    warcOutPath = os.path.join(os.path.dirname(__file__) +
                               '/samples/warcs/' + warcOutFilename)
    with open(warcOutPath, 'w') as warcFile:
        warcFile.write(newContent)

    return warcOutPath


def getRandomString(n):
    return ''.join(random.SystemRandom().choice(
                   string.ascii_lowercase + string.digits) for _ in range(n))
