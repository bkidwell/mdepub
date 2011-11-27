import unicodedata
import string
import mdepub

validFilenameChars = "'-_.() %s%s" % (string.ascii_letters, string.digits)

def clean(filename):
    cleanedFilename = unicodedata.normalize('NFKD', unicode(filename)).encode('ASCII', 'ignore')
    return ''.join(c for c in cleanedFilename if c in validFilenameChars)

def getFN(ext):
    """Get the project filename with the given extension (.md, .htm, etc.)"""
    return "%s.%s" % (mdepub.options['filename'], ext)
