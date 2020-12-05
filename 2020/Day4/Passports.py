import re

class Passport:
    def __init__(self):
        self.passport = {}
        self.passport['byr'] = None
        self.passport['iyr'] = None
        self.passport['eyr'] = None
        self.passport['hcl'] = None
        self.passport['ecl'] = None
        self.passport['hgt'] = None
        self.passport['pid'] = None
        self.passport['cid'] = None
        

    def valid(self):
        '''
        Passport is valid if: 
           cid value is missing and all other key:value pairs must have a value
           all key:value pairs have a value 
        '''
        return (self.passport['byr'] is not None and 
        self.passport['iyr'] is not None and               
        self.passport['eyr'] is not None and 
        self.passport['hgt'] is not None and 
        self.passport['ecl'] is not None and 
        self.passport['hcl'] is not None and 
        self.passport['pid'] is not None)

    def valid2(self):
        '''
        Passport is valid if: 
            cid value is missing then all other key:value pairs must have a value
            all key:value pairs have a value

            and: 

            byr (Birth Year) - four digits; at least 1920 and at most 2002.
            iyr (Issue Year) - four digits; at least 2010 and at most 2020.
            eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
            hgt (Height) - a number followed by either cm or in:
                If cm, the number must be at least 150 and at most 193.
                If in, the number must be at least 59 and at most 76.
            hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
            ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
            pid (Passport ID) - a nine-digit number, including leading zeroes.
            cid (Country ID) - ignored, missing or not. 

        '''
        valid_byr = self.passport['byr'] is not None and self._valid_year(self.passport['byr'],range(1920,2003))
        valid_iyr = self.passport['iyr'] is not None and self._valid_year(self.passport['iyr'],range(2010,2021))
        valid_eyr = self.passport['eyr'] is not None and self._valid_year(self.passport['eyr'],range(2020,2031))
        valid_ecl = self.passport['ecl'] is not None and self._valid_ecl(self.passport['ecl']) 
        valid_hcl = self.passport['hcl'] is not None and self._valid_hcl(self.passport['hcl']) 
        valid_hgt = self.passport['hgt'] is not None and self._valid_hgt(self.passport['hgt'])
        valid_pid = self.passport['pid'] is not None and self._valid_pid(self.passport['pid'])
        return valid_byr and valid_iyr and valid_eyr and valid_ecl and valid_hcl and valid_hgt and valid_pid

    def _valid_pid(self,pid_str):
        return len(pid_str) == 9 and re.match('\d{9}',pid_str) is not None

    def _valid_ecl(self,ecl_str):
        return ecl_str in ('amb','blu','brn','gry','grn','hzl','oth')
        
    def _valid_hcl(self,hcl_str):
        return len(hcl_str) == 7 and re.match('\#[abcdef0123456789]{6}',hcl_str) is not None

    def _valid_hgt(self,height_str):
        if len(height_str) > 2:
            units = height_str[-2:]
            if units in ('cm','in'):
                measure_str = height_str[0:-2]
                try:
                    measure = int(measure_str)
                    if units == "in":
                        return measure in range(59,77)
                    else:
                        return measure in range(150,194)
                except:
                    return False
            else:
                return False
        else:
            return False 

    def _valid_year(self,year_str,year_range):
        try:
            year = int(year_str)
            return year in year_range
        except:
            return False

class Passports:

    def __init__(self,file_name):
        passport = Passport()
        self.passports = []
        with open(file_name, "r") as passport_data:
            for line in passport_data:
                if len(line.strip('\n')) == 0:
                    # new passport - add current on and create a new one
                    self.passports.append(passport)
                    passport = Passport()
                else:
                    pairs = line.strip('\n').split(' ')
                    for pair in pairs:
                        pair_parts = pair.split(':')
                        passport.passport[pair_parts[0]] = pair_parts[1]
            
            # add last passport
            self.passports.append(passport)
            
    def valid(self):
        '''
        Return number of valid passports - part 1
        '''
        return len([p for p in self.passports if p.valid()])

    def valid2(self):
        '''
        Return number of valid passports - part 2
        '''
        return len([p for p in self.passports if p.valid2()])