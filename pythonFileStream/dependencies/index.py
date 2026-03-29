

globalID: int = 1

def getID():
    mGlo = globalID
    globals()['globalID'] = globalID + 1
    return mGlo




