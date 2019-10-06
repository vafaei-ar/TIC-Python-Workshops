def freq(fname):
    file=open(fname,"r")
    wlist = file.read().split()
    file.close()  

    wordcount={}
    for word in wlist:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    return wordcount

def add(x,y):
    return x+y

if __name__=='__main__':
    print('new load')
    print(3+2)

