from Stream import Stream

def main():
    stream = Stream('input.txt')
    print(f'Groups: {stream.get_totals()[0]}; Score: {stream.get_totals()[1]} Non-Garbage Chars: {stream.get_totals()[2]}')

if __name__ == '__main__':
    main()