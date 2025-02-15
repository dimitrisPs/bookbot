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

def filter_alphabetical(occurances):
    a='c'
    return {k:v for k,v in occurances.items() if k.isalpha()}

def print_report(word_count, char_occ):
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{word_count} words found in the document\n')
    
    for c, times in char_occ.items():
        print(f"The '{c}' character was found {times} times")
    
    print("--- End report ---")
        
def main():
    with open('./books/frankenstein.txt') as f:
        txt =f.read()
    
    word_count = wc(txt)
    occ = cc(txt)
    filt_occ = filter_alphabetical(occ)
    print_report(word_count, filt_occ)
    
if __name__ == '__main__':
    main()