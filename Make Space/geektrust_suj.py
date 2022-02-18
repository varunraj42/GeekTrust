from datetime import datetime
import datetime as dt

class Room:
    MIN_ATTENDEES = 2
    MAX_ATTENDEES = 20
    MAINT_TIMINGS = ["09:00", "13:15", "18:45"]
    DATE_FORMAT = "%H:%M"
    START_END_INTERVAL = 15


    def __init__(self, roomType, maxCapacity):
        self.availTimings =  self.get_all_timeslots()
        self.maxCapacity = maxCapacity
        self.roomType = roomType


    def get_all_timeslots(self):
        availTimings = []

        for hour in range(0, 24):
            for min in range(0, 60, 15):
                datetimeObj = datetime.strptime(f"{hour}:{min}", Room.DATE_FORMAT)
                if datetimeObj.strftime(Room.DATE_FORMAT) not in Room.MAINT_TIMINGS:
                    availTimings.append(datetimeObj)

        return availTimings


    def validate_meeting_timings(self, startAt, endAt):
        try:
            if all([(startAt < endAt), (startAt.minute%15 ==0 and endAt.minute%15 ==0) ]):
                return True
        except ValueError as ve:
            pass

        return False


    def get_req_timeslots(self, startAt, endAt):
        timeSlots = []

        startTimeSlot = startAt
        while startTimeSlot < endAt:
            timeSlots.append(startTimeSlot)
            startTimeSlot += dt.timedelta(minutes=15)

        return timeSlots


    def is_available(self, capacityNeed, startAt, endAt, blockSlot=True):
        startAt = datetime.strptime(startAt, "%H:%M")
        endAt = datetime.strptime(endAt, "%H:%M")

        if self.validate_meeting_timings(startAt, endAt):
            timeSlots = self.get_req_timeslots(startAt, endAt)

            for slot in timeSlots:
                if slot not in self.availTimings or capacityNeed > self.maxCapacity:
                    return False
                elif blockSlot:
                    self.availTimings.remove(slot)
        else:
            return "INCORRECT INPUT"

        return True


def read_input(file):
    with open(file, 'r') as input:
        data = input.read()

    return data

def show_vacant_rooms(startAt, endAt, roomTypes):
    vacantRooms = []
    for room in roomTypes:
        isAvailable = room.is_available(0, startAt, endAt, blockSlot=False)

        if isAvailable == "INCORRECT INPUT":
            return "INCORRECT_INPUT"

        if isAvailable:
            vacantRooms.append(room.roomType)

    if len(vacantRooms) == 0:
        return f"NO_VACANT_ROOM"

    return f"{' '.join(vacantRooms)}"


def book_room(startAt, endAt, capacityNeed, roomTypes):
    booked = False
    for room in roomTypes:
        isAvailable = room.is_available(capacityNeed, startAt, endAt)

        if capacityNeed < 2 or isAvailable == "INCORRECT INPUT":
            return "INCORRECT_INPUT"

        if isAvailable:
            booked = True
            return f"{room.roomType}"

    if not booked:
        return "NO_VACANT_ROOM"



def run(file):
    instructions = read_input(file)
    instructions = instructions.split('\n')

    output = []

    cave = Room("C-Cave", 3)
    tower = Room("D-Tower", 7)
    mansion = Room("G-Mansion", 20)
    for ins in instructions:
        if 'VACANCY' in ins and ins !='':
            command, startAt, endAt = ins.split(' ')
            output.append(show_vacant_rooms(startAt, endAt, [cave, tower, mansion]))

        elif 'BOOK' in ins and ins !='':
            command, startAt, endAt, capacityNeed = ins.split(' ')
            capacityNeed = int(capacityNeed)
            output.append(book_room(startAt, endAt, capacityNeed, [cave, tower, mansion]))

    return '\n'.join(output)


if __name__ == '__main__':
    import sys
    file = sys.argv[1]
    print(run(file))
