import re

class Bus():

    def __init__(self,file_name):
        with open(file_name,'r') as schedule_data:
            self._timestamp = int(schedule_data.readline().strip('\n'))
            schedule_parts = schedule_data.readline().strip('\n').split(',')
            self._bus_ids = []
            for part in schedule_parts:
                if part != 'x':
                    self._bus_ids.append(int(part))


    def next_bus(self):
        ''' 
        Return id of next bus * minutes you'll have to wait
        '''
        next_bus_due = [(id, id - (self._timestamp % id)) for id in self._bus_ids]
        sorted_next_bus_due = sorted(next_bus_due,key=lambda d : d[1])
        return sorted_next_bus_due[0][0] * sorted_next_bus_due[0][1] 
