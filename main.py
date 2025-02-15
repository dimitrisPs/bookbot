def wc(txt):
    return len(txt.split())
    
    
def cc(txt):
    occurances={}
    for c in txt:
        c = c.lower()
        if c not in occurances:
            occurances[c] = 0
        occurances[c]+=1
    return occurances
        
def main():
    with open('./books/frankenstein.txt') as f:
        txt =f.read()
    print(txt)
    
    print(wc(txt))
    print(cc(txt))
    
if __name__ == '__main__':
    main()