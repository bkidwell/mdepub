import unicodedata
import string
import mdepub
import os.path

validFilenameChars = "'-_.() {}{}".format(string.ascii_letters, string.digits)

def clean(filename):
    cleanedFilename = unicodedata.normalize('NFKD', unicode(filename)).encode('ASCII', 'ignore')
    return ''.join(c for c in cleanedFilename if c in validFilenameChars)

def getFN(ext):
    """Get the project filename with the given extension (.md, .htm, etc.)"""
    return "{}.{}".format(mdepub.options['filename'], ext)
