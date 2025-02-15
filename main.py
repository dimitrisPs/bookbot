def wc(txt):
    return len(txt.split())
    
def main():
    with open('./books/frankenstein.txt') as f:
        txt =f.read()
    print(txt)
    
    print(wc(txt))
    
if __name__ == '__main__':
    main()