## I'm trying to design a Slot Booking system of Meeting-Rooms in a Co-working space company.

# Standard Rules:
1) There are total of 3 Room(Types) Available ( C(Cave), T(Tower), M(Mansion) )
2) Allocation of Room is determined on the number of Attendees (0-3--> C, 4-7--> T, 8-20--> M)
3) Number of Attendees must lie in the range of 2-20.
4) Each Room can be booked anytime b/w (Early Morning)00:00 - 00:00(Midnight)
5) Meeting must start/end at a 15-minute period interval (Valid(Start/End)--> 12:00, 14:15, 16:30  Invalid--> 16:03, 17:12)
6) Meeting can take place for any amount of time (provided it ends before Midnight).
7) There is a scheduled Maintenance-time (9-9:15, 13:15-13:30, 18:45-19:00), where-in no slots will be available in this intervals.
8) If the slot-request has an Overlap, with the Maintenance-time, request must be rejected. (NO_VACANT_ROOM)

# Availability WorkArounds:
1) If a Room is Full, Next Available Room would be allocated ( Preference: Cave -> Tower -> Mansion )
  Eg: If Cave is NA, Allocate Tower. If Tower is NA, Allocate Mansion..

Sample Case:  # BOOK <start_at> <end_at> <attendees>
  Input: BOOK 11:00 11:45 2  
    # Since, <attendees> <= 3, CAVE is the best option
    # Check, if CAVE room is available on given timings.
    # Confirm the availability and block the slot
    # If not, check for the next room.
    # If None is Avail, return "NO_VACANT_ROOM"

OOPS Design

Parent Class:
  Room
    Data: AvailTimings
          MIN_ATTENDEES
          MAX_ATTENDEES
          MAINT_TIMINGS
    Methods:
          get_all_time_slots <-- This will initialize all the slots as "FREE" at beginning of the day.
          validate_meeting_timings <-- This would validate the request input.          
          get_req_time_slots <-- This would get all the time-slots(15 min. intervals) that fit between the requested time.
          is_available <-- All the above time-slots, would be check for availability
