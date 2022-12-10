from CathodeRayTube import CPU

def main():
    cpu = CPU('input.txt')
    cpu.run_instructions()
    print(cpu.sum_signal_strengths([20,60,100,140,180,220]))

    cpu.display()

if __name__ == '__main__':
    main()