from Computer import Computer,StopReason
from SequenceCodes import SequenceCodes   

class Amplifiers:
    def __init__(self,filename,number,sequence_codes):
        self.number = number
        self.sequence_codes = sequence_codes
        with open(filename,"r") as program_file:
            self.program = program_file.readline().strip('\n')

    ''' PART 1, 1ST ATTEMPT - NO LONGER NEEDED
    def get_max_thruster_signal(self):
        thruster_signals = []
        for sequence_code in self.sequence_codes: 
            output_from_last_amp = 0
            for amp_no in range(0,self.number):
                amp = Amplifier(self.program,[sequence_code[amp_no],output_from_last_amp])
                output_from_last_amp = amp.get_output()[0]
            thruster_signals.append(output_from_last_amp)
        return max(thruster_signals)
    '''

    def get_max_thruster_signal(self):
        thruster_signals = []
        for sequence_code in self.sequence_codes: 
            # create amps
            amps=[]
            for amp_no in range(0,self.number):
                if amp_no == 0:
                    amps.append(Amplifier(self.program,[sequence_code[amp_no],0]))
                else:
                    amps.append(Amplifier(self.program,[sequence_code[amp_no]]))
            
            # run each amp in turn appending
            stop = False
            while not stop: 
                for amp_no in range(0,self.number):
                    output_val = amps[amp_no].get_output(False)
                    if amp_no == self.number-1 and output_val[1] == StopReason.STOP:
                        thruster_signals.append(output_val[0])
                        stop = True
                        break
                    else:
                        next_amp_no = amp_no + 1
                        if next_amp_no == self.number:
                            next_amp_no = 0
                        amps[next_amp_no].computer.input_vals.append(output_val[0])
            
            
        #thruster_signals.append(output_from_last_amp)
        return max(thruster_signals)

class Amplifier:
    def __init__(self,program,input_vals):
        self.computer = Computer(program,input_vals)
    
    def get_output(self,start_at_zero=True):
        output = self.computer.run_program(start_at_zero)
        return output

