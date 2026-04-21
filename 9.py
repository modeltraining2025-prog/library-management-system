def ASDF(strr):
    freq = {}
    for i in strr.split():
        ch = i[0]
        if ch not in freq:  freq[ch] = []
        freq[ch].append(i)
    return freq

strr = 'hello buddy how are you'
print(diction(strr))
