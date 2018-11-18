
# these functions take the text and 
# filter out things to make it better for the markov chain

def removeUnicode(text):
    return ''.join([c for c in text if ord(c) < 128])

def removeErrantWhitespace(text):
    retval = ' '.join([token for token in text.split(' ') if token != ''])
    return retval

def buildFilterPipeline(filterUnicode=True, filterWhitespace=True):
    pipeline = []
    if filterUnicode:
        pipeline.append(removeUnicode)
    if filterWhitespace:
        pipeline.append(removeErrantWhitespace)
    return pipeline