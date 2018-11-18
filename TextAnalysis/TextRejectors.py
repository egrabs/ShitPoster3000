
# a bunch of functions that return booleans indicating whether
# the given text is crappy in one way or another

# really too much nonascii text but I like putting "emoji" in my function name
def tooManyEmojis(text):
    # effin millenials
    rejectionThreshold = 0.25
    numAscii = len([c for c in text if ord(c) < 128])
    numUnicode = len([c for c in text if ord(c) >= 128])
    return numUnicode > rejectionThreshold*numAscii

def tooManySpaces(text):
    # g u a r d  a g a i n s t  t h i s  s o r t  o f  p e r s o n
    rejectionThreshold = 3
    tokens = text.split(' ')
    tokens = [token for token in text.split(' ') if token != '']
    avgTokenLen = sum([len(token) for token in tokens]) / len(tokens)
    return avgTokenLen <= rejectionThreshold

def tooManyNonWords(text):
    rejectionThreshold = 0.30
    tokens = [token for token in text.split(' ') if token != '']
    nonWords = 0
    for token in tokens:
        startChar = token[0]
        asciiNum = ord(startChar)
        if asciiNum < ord('A') or (asciiNum > ord('Z') and asciiNum < ord('a')) or asciiNum > ord('z'):
            nonWords += 1
    return (nonWords / len(tokens)) >= rejectionThreshold


def empty(text):
    # empty or mostly empty
    rejectionThreshold = 5
    return len(text) < rejectionThreshold

def buildRejectionPipeline(rejectUnicode=True, rejectSpaces=True, rejectNonWords=True):
    pipeline = [empty]
    if rejectUnicode:
        pipeline.append(tooManyEmojis)
    if rejectSpaces:
        pipeline.append(tooManySpaces)
    if rejectNonWords:
        pipeline.append(tooManyNonWords)
    return pipeline
