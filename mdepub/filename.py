import unicodedata
import string

validFilenameChars = "'-_.() %s%s" % (string.ascii_letters, string.digits)

def clean(filename):
    cleanedFilename = unicodedata.normalize('NFKD', unicode(filename)).encode('ASCII', 'ignore')
    return ''.join(c for c in cleanedFilename if c in validFilenameChars)
