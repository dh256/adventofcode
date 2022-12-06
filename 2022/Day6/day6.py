from Device import Device 

def main():
    device = Device('input.txt')
    print(device.first_marker(4))
    print(device.first_marker(14))

if __name__ == '__main__':
    main()