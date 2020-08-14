import re

class IP:

    def __init__(self,address):
        self.full_address = address 
        regex = re.compile(r'\[(.*?)\]')  # regex to find [...]
        self.hypernet_sequences = regex.findall(self.full_address)
        self.supernet_sequences = regex.sub(' ',self.full_address).split(' ')
        self.supports_tls = self.supports_tls() 
        self.supports_ssl = self.supports_ssl() 
        
    def supports_tls(self):
        no_hypernets_contain_abbas = len([seq for seq in self.hypernet_sequences if self.contains_abba(seq)]) == 0
        non_hypernet_contains_abba = len([seq for seq in self.supernet_sequences if self.contains_abba(seq)]) > 0 #self.contains_abba(self.non_hypernet_sequence)
        return no_hypernets_contain_abbas and non_hypernet_contains_abba

    def contains_abba(self,text):
        # find abbas
        if len(text) < 4:
            return False
        else:
            for pos in range(0,len(text)-3):
                first_part = text[pos:pos+2]
                if first_part[0] != first_part[1] and first_part[1] == text[pos+2] and first_part[0] == text[pos+3]:
                    return True   

    def supports_ssl(self):
        for seq in self.supernet_sequences:
            abas = self.get_abas(seq)
            for aba in abas:
                bab = self.convert_aba_to_bab(aba)
                for seq in self.hypernet_sequences:
                    if bab in seq:
                        return True
        return False

    def get_abas(self,text):
        abas = []
        if len(text) >= 3:
            for pos in range(0,len(text)-2):
                if text[pos] == text[pos+2] and text[pos] != text[pos+1]:
                    abas.append(text[pos:pos+3])
        return abas

    def convert_aba_to_bab(self,aba):
        if len(aba) != 3:
            raise ValueError
        else:
            return f'{aba[1]}{aba[0]}{aba[1]}' 

class IPAddresses:
    def __init__(self,file_name):
        with open(file_name,"r") as file_input:
            self.ips = [IP(line.strip('\n')) for line in file_input]

    def supports_tls(self):
        return len([ip for ip in self.ips if ip.supports_tls])

    def supports_ssl(self):
        return len([ip for ip in self.ips if ip.supports_ssl])