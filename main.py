def main():
    with open('./books/frankenstein.txt') as f:
        txt =f.read()
    print(txt)
    
if __name__ == '__main__':
    main()