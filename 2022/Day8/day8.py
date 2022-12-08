from Trees import Trees

def main():
    trees = Trees('input.txt')
    print(trees.number_visible())
    print(trees.scenic_score())

if __name__ == '__main__':
    main()