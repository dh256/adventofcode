from FileSystem import FileSystem

def main():
    fs = FileSystem('input.txt')
    print(f'Part 1: {fs.total_size_of_folders_up_to_size(100000)}')
    print(f'Part 2: {fs.smallest_to_delete(30000000)}')

if __name__ == '__main__':
    main()