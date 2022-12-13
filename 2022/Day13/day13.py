from DistressSignal import Signal

def main():
    signal = Signal('input.txt')
    print(signal.right_order_pairs())
    print(signal.pairs_in_right_order())

if __name__ == '__main__':
    main()