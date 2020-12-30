import re
from collections import namedtuple

Range = namedtuple('Range',['start','end'])

class Field():
    def __init__(self,description):
        regex = r'(\w+\s*\w*): (\d+)-(\d+) or (\d+)-(\d+)'
        matches = re.match(regex,description)
        if matches:
            self._name = matches.group(1)
            self._range1 = Range(int(matches.group(2)),int(matches.group(3)))
            self._range2 = Range(int(matches.group(4)),int(matches.group(5)))

    @property
    def name(self):
        return self._name

    @property
    def range1(self):
        return self._range1

    @property
    def range2(self):
        return self._range2

class Tickets():

    def __init__(self,file_name):
        self._field_types = {}    # Part 2, holds the type (name) of each field in a ticket
        self._fields = []
        self._nearby_tickets = []
        with open(file_name,'r') as ticket_notes:
            # first section (until first blank line) is Fields
            next_line = ticket_notes.readline().strip('\n')
            while len(next_line) > 0:
                self._fields.append(Field(next_line))
                next_line = ticket_notes.readline().strip('\n')

            # next section is your ticket
            ticket_notes.readline()
            self._my_ticket = [self.get_ticket(ticket_notes.readline().strip('\n'))]
            ticket_notes.readline()

            # next section is nearby tickets
            ticket_notes.readline()
            next_line = ticket_notes.readline().strip('\n')
            while len(next_line) > 0:
                self._nearby_tickets.append(self.get_ticket(next_line))
                next_line = ticket_notes.readline().strip('\n')
            
    def get_ticket(self,ticket_str):
        '''
        Ticket contains a field value and a field type
        '''
        return [int(t) for t in ticket_str.split(',')]

    def scanning_error_rate(self):
        '''
        Scan through nearby tickets and work out which fields in ticket are not valid
        '''
        invalid_fields = []
        for t in self._nearby_tickets:
            self._get_invalid_fields(t,invalid_fields)
        return sum(invalid_fields)

    def _get_invalid_fields(self,ticket,invalid_fields):
        '''
        Gets any invalid field values in ticket
        '''
        for field_value in ticket:
            for f in self._fields:
                if (field_value >= f.range1.start and field_value <= f.range1.end) or (field_value >= f.range2.start and field_value <= f.range2.end):
                    break
            else:
                # no match found 
                invalid_fields.append(field_value)

    def departure_fields(self):
        ''' 
        Identifies the type of each field in a ticket
        Return the value of all the 6 deperature fields multiplied together
        '''
        valid_tickets = [t for t in self._nearby_tickets if not self._invalid_ticket(t)]
        candidate_fields = self._fields.copy()
        for index in range(0,len(self._my_ticket[0])):
            candidate_fields_tf = candidate_fields.copy()
            for vt in valid_tickets:
                curr_field = vt[index]
                candidate_fields_tf = self.remove_candidate_fields(curr_field,candidate_fields_tf)
            if len(candidate_fields_tf) == 1:
                # field identified exclusively
                self._field_types[index] = [candidate_fields_tf[0].name]
                
                # remove this field as a candidate for all other fields
                candidate_fields.remove(candidate_fields_tf[0])

                # check whether this field is a candidate for any other field and remove
                for key,value in self._field_types.items():
                    if len(value) > 1 and candidate_fields_tf[0].name in value:
                        value.remove(candidate_fields_tf[0].name)
                        if len(value) == 1:
                            try:
                                candidate_fields.remove(candidate_fields_tf[0])
                            except ValueError:
                                pass
            else:
                self._field_types[index] = []
                for cf in candidate_fields_tf:
                    self._field_types[index].append(cf.name)

        # process confirmed candidates
        self.process_confirmed_candidates()  

        # multiply all the values together for departure fields in my_ticket
        result = 1        
        for key,value in self._field_types.items():
             if value[0].startswith('departure'):
                result *= self._my_ticket[0][key]
        return result

    def process_confirmed_candidates(self):
        # go through self._field_types until all indexes have only value
        more_to_process = True
        while more_to_process:
            more_to_process = False
            for key1,value1 in self._field_types.items():
                if len(value1) == 1:
                    for key2,value2 in self._field_types.items():
                        if key2 != key1 and value1[0] in value2:
                            value2.remove(value1[0])
                else:
                    more_to_process = True

    def remove_candidate_fields(self,field_value,candidate_fields):
        for f in candidate_fields[::-1]:
            if not ((field_value >= f.range1.start and field_value <= f.range1.end) or (field_value >= f.range2.start and field_value <= f.range2.end)):
                candidate_fields.remove(f)
        return candidate_fields

    def _invalid_ticket(self,ticket):
        '''
        Returns TRUE if invalid ticket i.e. it contains an invalid field
        '''
        for field_value in ticket:
            for f in self._fields:
                if (field_value >= f.range1.start and field_value <= f.range1.end) or (field_value >= f.range2.start and field_value <= f.range2.end):
                    break
            else:
                return True
        return False
    