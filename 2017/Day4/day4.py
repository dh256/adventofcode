from Passphrase import Passphrase

def main():
    pass_phrases = Passphrase('input.txt')
    print(f'{pass_phrases.valid_phrases()}')
    print(f'{pass_phrases.valid_phrases2()}')

if __name__ == '__main__':
    main()