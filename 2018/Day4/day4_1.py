from datetime import datetime
from datetime import timedelta
from enum import Enum

class GuardState(Enum):
    NEW=0
    SHIFT_START=1
    SLEEPING=2
    AWAKE=3

class LogEntryType(Enum):
    SLEEP = 0
    WAKE = 1
    SHIFT = 2

class TimesheetEntry:
    def __init__(self, date, guardid=None):
        self.date = date
        self.guardId = guardid
        self.midnightHour = [0] * 60

    def __eq__(self,other):
        return self.date == other.date and self.guardId == other.guardId

class Timesheet:
    def __init__(self, minDate, maxDate):
        currDate = minDate
        self.entries = []
        while currDate <= maxDate:
            self.entries.append(TimesheetEntry(currDate))
            currDate = currDate + timedelta(days=1)

    def setGuard(self,date,guardId):
        #find date entry and update guardId to guardId
        for entry in self.entries:
            if entry.date == date:
                entry.guardId = guardId


    def setSleep(self,date,guardId,startMinute,endMinute=60):
        #set midnightHour list value to 1 for indexes in range startMinute to endMinute
        #Note: if end minute is None set to 59
        index = 0
        while index < len(self.entries):
            if self.entries[index].date == date and self.entries[index].guardId == guardId:
                for minute in range(startMinute,endMinute):
                    self.entries[index].midnightHour[minute] = 1
                break
            index += 1

    def sleepiestGuard(self):
        distr = {}
        for entry in self.entries:
            if not entry.guardId in distr:
                distr[entry.guardId] = 0

            minutesSleeping = 0
            for minute in entry.midnightHour:
                if minute == 1:
                    minutesSleeping += 1
            
            distr[entry.guardId] += minutesSleeping
        return sorted(distr.items(), key=lambda x: x[1], reverse=True)[0][0]

    def sleepiestGuardMinute(self, guardId):
        distr = {}
        for minute in range (0,59):
            distr[minute] = 0

        for entry in self.entries:
            if entry.guardId == guardId:
                minIndex = 0
                while minIndex <= 59:
                    if entry.midnightHour[minIndex] == 1:
                        distr[minIndex] += 1
                    minIndex += 1
                    
        return sorted(distr.items(), key=lambda x: x[1], reverse=True)[0][0]

    def getGuardAsleepSameMinute(self):
        distr = {}
        for entry in self.entries:
            if not entry.guardId == None:
                minIndex = 0
                while minIndex <= 59:
                    if not (entry.guardId,minIndex) in distr:
                        distr[entry.guardId,minIndex] = 0
                    if entry.midnightHour[minIndex] == 1:
                        distr[entry.guardId,minIndex] += 1  
                    minIndex += 1  
                

        return sorted(distr.items(), key=lambda x: x[1], reverse=True)[0]
        
class TimeLogEntry:
    def __init__(self, time, description):
        self.time = time
        self.description = description

    def entryType(self):
        #if description contains "starts shift" then this is a "SHIFT" record
        #wakes up is a WAKE record
        #falls asleep is a SLEEP record
        if "falls asleep" in self.description:
            return LogEntryType.SLEEP
        elif "wakes up" in self.description:
            return LogEntryType.WAKE
        elif "begins shift" in self.description:
            return LogEntryType.SHIFT
        else:
            return None

    def guardId(self):
        #Check is a shift start record
        if self.entryType() == LogEntryType.SHIFT:
            descParts = self.description.split(" ")
            guardId = descParts[1][1:]
            return guardId
        else:
            return None 

    def hour(self):
        return self.time.hour

    def minute(self):
        return self.time.minute

    def date(self):
        return datetime(self.time.year, self.time.month, self.time.day)

def processTimeLogEntry(entry):
    entry = entry.rstrip('\n')
    timeString = entry[1:17]
    time = datetime.fromisoformat(timeString)
    description = entry[19:]
    entry = TimeLogEntry(time, description)
    return entry

def processFile(fileName):
    #create list containing all timesheet entries
    with open(fileName, "r") as input:
        timeLog = [processTimeLogEntry(line) for line in input]

        #sort list by time
        timeLog.sort(key=lambda x:x.time, reverse=False)
        return timeLog

def startShift(entry):
    guardId = entry.guardId() 
    timesheetDate = entry.date()
    if entry.hour() == 23:
        # add 1 day to date 
        timesheetDate += timedelta(days=1)

    return {'Date': timesheetDate, 'GuardId': guardId}
    

def processTimeLogs(timeLogEntries, timesheet):
    """
    first entry contains guard number and start time
    subsequent entries contain a sequence of falls aslepp and awake events
    if fall asleep start recording 1s in list using minute as index
        e.g. if falls asleep at 00:05 start recording 1s at index 5
        if wakens up at 00:20 stop recording 1s at index 20 
    when get to next guard entry repeat above

    Complications:
    if initial time.hour for a Guard entry is not 0 (23) then move date on one day
    """
    state = GuardState.NEW
    startSleep = 0
    endSleep = 0
    entryIndex = 0
    shiftRec = {}
    while entryIndex < len(timeLogEntries):
        if timeLogEntries[entryIndex].entryType() == LogEntryType.SHIFT:
            if state == GuardState.SLEEPING:
                # previous guard was sleeping at 00:59
                timesheet.setSleep(shiftRec['Date'], shiftRec['GuardId'], startSleep) 

            # get new shift record
            shiftRec = startShift(timeLogEntries[entryIndex])
            timesheet.setGuard(shiftRec['Date'], shiftRec['GuardId'])
            state = GuardState.SHIFT_START
        elif timeLogEntries[entryIndex].entryType() == LogEntryType.SLEEP:
            startSleep = timeLogEntries[entryIndex].minute()
            state = GuardState.SLEEPING

        elif timeLogEntries[entryIndex].entryType() == LogEntryType.WAKE:
            endSleep = timeLogEntries[entryIndex].minute()
            timesheet.setSleep(shiftRec['Date'], shiftRec['GuardId'], startSleep, endSleep)
            state = GuardState.AWAKE
        
        entryIndex += 1

def shiftStartHoursDistr(entries):
    # calcuklate a distribution of shift start hours
    distr = {}
    for entry in entries:
        if entry.hour() in distr.keys():
            distr[entry.hour()] += 1
        else:
            distr[entry.hour()] = 1
    print(distr)

def printTimeLogEntries(entries):
    for entry in entries:
        print(entry.time, entry.description)

#solve puzzle
timeLogEntries=processFile('day4.txt')
timesheet=Timesheet(timeLogEntries[0].date(), timeLogEntries[-1].date())
processTimeLogs(timeLogEntries, timesheet)

# PART 1 - Sleepiest guard and minute in which they sleep most
sleepiestGuard = timesheet.sleepiestGuard()
sleepiestGuardMinute = timesheet.sleepiestGuardMinute(sleepiestGuard)
print("Puzzle answer (PART 1):", int(sleepiestGuard) * int(sleepiestGuardMinute))

# PART 2 - Of all guards, which guard is most frequently asleep on the same minute?
getGuardAsleepSameMinute = timesheet.getGuardAsleepSameMinute()
guardId = int(getGuardAsleepSameMinute[0][0])
minute = int(getGuardAsleepSameMinute[0][1])
print("Puzzle answer (PART 2):", guardId * minute)
