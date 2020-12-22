from collections import namedtuple

class Seat(): 
    def __init__(self,state,state_changed):
        self._state = state
        self._state_changed = state_changed
    
    @property
    def state(self):
        return self._state
    
    @property
    def state_changed(self):
        return self._state_changed

    @state_changed.setter 
    def state_changed(self,state_changed):
        self._state_changed = state_changed

    @state.setter 
    def state(self,state):
        self._state = state

Position = namedtuple('Position',['x','y']) 

class FerrySeats():

    OCCUPIED = "#"
    EMPTY = "L"
    FLOOR = "."

    VISIBLE_MODE = 'V'    # Part 2
    ADJACENT_MODE = 'A'   # Part 1

    def __init__(self,file_name):
        with open(file_name,'r') as seat_data:
            seat_rows = [line.strip('\n') for line in seat_data]
            self._rows = len(seat_rows)
            self._rowlen = len(seat_rows[0])
            self._seats = {}
            y=0
            for row in seat_rows:
                x=0
                for seat in row:        
                    if seat == FerrySeats.OCCUPIED or seat == FerrySeats.EMPTY:
                        self._seats[Position(x,y)] = Seat(seat,False)
                    else:
                        self._seats[Position(x,y)] = Seat(seat,None)
                    x+=1
                y+=1

    def __str__(self):
        output = ''        
        for y in range(0,self._rows):
            for x in range(0,self._rowlen):
                output += self._seats[Position(x,y)].state
            output += '\n'
        return output

    def reset_state_changed(self):
        for pos in self._seats.keys():
            if self._seats[pos].state in (FerrySeats.EMPTY,FerrySeats.OCCUPIED):
                self._seats[pos].state_changed = False     

    def change_seat_state_adjacent(self,pos,seat):
        '''
        Checks adjacent seats for the current seat
        If EMPTY, returns True if one adjacent seat occupied
        If OCCUPIED, returns True if 4 or more adjacent seats
        '''
        occupied = 0
        for x in range(pos.x-1,pos.x+2):
            for y in range(pos.y-1,pos.y+2):
                if x == pos.x and y == pos.y:
                    pass    # ignore
                elif x < 0 or y < 0:
                    pass    # ignore
                elif x >= self._rowlen or y >= self._rows:
                    pass    # ignore
                elif self._seats[Position(x,y)].state == FerrySeats.OCCUPIED:
                        occupied += 1
                        
        if seat.state == FerrySeats.EMPTY and occupied == 0:
            return True
        elif seat.state == FerrySeats.OCCUPIED and occupied > 3:
            return True
        else:
            return False
                    
    def change_seat_state_visible(self,pos,seat):
        occupied = 0
        
        # UP (N)
        for y in range(pos.y-1,-1,-1):
            if self._seats[Position(pos.x,y)].state == FerrySeats.OCCUPIED:
                occupied += 1
                break
            elif self._seats[Position(pos.x,y)].state == FerrySeats.EMPTY: 
                break

        # DOWN  (S)
        for y in range(pos.y+1,self._rows):
            if self._seats[Position(pos.x,y)].state == FerrySeats.OCCUPIED:
                occupied += 1
                break
            elif self._seats[Position(pos.x,y)].state == FerrySeats.EMPTY: 
                break

        # LEFT  (W)
        for x in range(pos.x-1,-1,-1):
            if self._seats[Position(x,pos.y)].state == FerrySeats.OCCUPIED:
                occupied += 1
                break
            elif self._seats[Position(x,pos.y)].state == FerrySeats.EMPTY: 
                break

        # RIGHT (E)
        for x in range(pos.x+1,self._rowlen):
            if self._seats[Position(x,pos.y)].state == FerrySeats.OCCUPIED:
                occupied += 1
                break
            elif self._seats[Position(x,pos.y)].state == FerrySeats.EMPTY: 
                break

        # UP RIGHT  (NE)
        x = pos.x + 1
        y = pos.y - 1
        while x < self._rowlen and y >= 0:
            if self._seats[Position(x,y)].state == FerrySeats.OCCUPIED:
                occupied += 1
                break
            elif self._seats[Position(x,y)].state == FerrySeats.EMPTY: 
                break
            x += 1
            y -= 1

        # DOWN RIGHT  (SE)
        x = pos.x + 1
        y = pos.y + 1
        while x < self._rowlen and y < self._rows:
            if self._seats[Position(x,y)].state == FerrySeats.OCCUPIED:
                occupied += 1
                break
            elif self._seats[Position(x,y)].state == FerrySeats.EMPTY: 
                break
            x += 1
            y += 1

        # DOWN LEFT  (SW)
        x = pos.x - 1
        y = pos.y + 1
        while x >= 0 and y < self._rows:
            if self._seats[Position(x,y)].state == FerrySeats.OCCUPIED:
                occupied += 1
                break
            elif self._seats[Position(x,y)].state == FerrySeats.EMPTY: 
                break
            x -= 1
            y += 1
            
        # UP LEFT  (NW)
        x = pos.x - 1
        y = pos.y - 1
        while x >= 0 and y >= 0:
            if self._seats[Position(x,y)].state == FerrySeats.OCCUPIED:
                occupied += 1
                break
            elif self._seats[Position(x,y)].state == FerrySeats.EMPTY: 
                break
            x -= 1
            y -= 1
                        
        if seat.state == FerrySeats.EMPTY and occupied == 0:
            return True
        elif seat.state == FerrySeats.OCCUPIED and occupied > 4:
            return True
        else:
            return False

    def calculate_occupied_seats(self,mode):
        '''
        If Mode = "A" (Adjancent)  - Part 1
            Loop through all seat 
            Examine number of occupied adjacenet seats and determine if state should change.
            If so, change state once all seats examined
            If no seats change state return number of occupied seats
        If Mode = "V" (Visible)  - Part 2
            Calculate number of occupied seats once no seats change state
            If a seat is empty (L) and there are no visible occupied seats in any direction, the seat becomes occupied.
            If a seat is occupied (#) and five or more visible occupied seats in any direction to it are also occupied, the seat becomes empty.
            Otherwise seat state does not change

            Loop through all seats applying above rules recording which seats change state
            Once no seats change, return number of occupied seats
        ''' 
        while True:
            self.reset_state_changed()
            for pos,seat in self._seats.items():
                if seat.state == FerrySeats.EMPTY or seat.state == FerrySeats.OCCUPIED:
                    if mode == FerrySeats.ADJACENT_MODE:  # Part 1
                        self._seats[pos].state_changed = self.change_seat_state_adjacent(pos,seat)
                    elif mode == FerrySeats.VISIBLE_MODE:  # Part 2
                        self._seats[pos].state_changed = self.change_seat_state_visible(pos,seat)

            # any seats changed state
            changed_seats = dict(filter(lambda elem: elem[1].state_changed == True, self._seats.items()))
            if len(changed_seats) == 0:
                # calculate occupied seats
                occupied_seats = dict(filter(lambda elem: elem[1].state == FerrySeats.OCCUPIED, self._seats.items()))
                return len(occupied_seats)
            else:
                # transform_seats
                for pos in changed_seats.keys():
                    if self._seats[pos].state == FerrySeats.OCCUPIED: 
                        self._seats[pos].state = FerrySeats.EMPTY
                    elif self._seats[pos].state == FerrySeats.EMPTY:
                        self._seats[pos].state = FerrySeats.OCCUPIED
                