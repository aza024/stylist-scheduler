# 1. Prompt for input

# 2. Schedule either: 
    # Haircut: 30 minutes
    # Shampoo and Haircut: 1 hour (60 minutes)
    # OR:
    # List all appointments
    # Exit

#

class Event(object):
    def __init__(self, start, end):
        # type: (int, int) -> None
        self.start = start
        self.end = end

    def get_start_time(self):
        # type: () -> int
        return self.start

    def get_end_time(self):
        # type: () -> int
        return self.end


    def overlaps_with(self, other):
        # type: (Event) -> bool
        # If we start while the other event is happening
        if self.get_start_time() > other.get_start_time():
            if self.get_start_time() < other.get_end_time():
                return True

        # If we end while the other event is happening
        if self.get_end_time() > other.get_start_time():
            if self.get_end_time() < other.get_end_time():
                return True

        # Otherwise
        return False


class Scheduler(object):
    def __init__(self):
        self.appointments = []  # type: List[Event]

    def add_appointment(self, new_appointment):
        # type: (Event) -> Optional[Event]
        for existing in self.appointments:
            if existing.overlaps_with(new_appointment):
                return existing

        self.appointments.append(new_appointment)

    def list_appointment(self):
        # type: () -> None
        for appointment in self.appointments:
            print(appointment)

def get_appointment_time():
    # type: () -> int
    
    print('Please enter the time you would like, in the format HH:MM (military time)')
    while True:
        input_time = raw_input()
        split_time = input_time.split(":")

        if len(split_time) != 2:
            print("Sorry, {} is not a valid appointment time. Please use the format HH:MM (military time)".format(input_time))
            continue
        
        hour = split_time[0]
        minute = split_time[1]

        if not (hour.isdigit() and minute.isdigit()):
            print("Sorry, {} is not a valid appointment time. Please use the format HH:MM (military time)".format(input_time))
            continue    

        hour = int(hour)
        minute = int(minute)

        if minute % 15 != 0 or minute > 60:
            print("Sorry, minutes".format(input_time))
            continue                

        combined = hour + minute
        if not combined.isdigit():
            print("Sorry, {} is not a valid appointment time. Please use the format HH:MM (military time)".format(input_time))
            continue

        return int(combined)

def get_event():
    # type: () -> Optional[Event]
    print('Hello! To schedule a haircut, press 1. To schedule a haircut with shampoo, press 2.')
    while True:
        user_in = raw_input()
        if not user_in.isdigit():
            print('{} is not a valid number, please try again'.format(user_in))
            print('To schedule a haircut, press 1. To schedule a haircut with shampoo, press 2.')
            continue

        choice = int(user_in)
        appt_time = get_appointment_time()
        if choice == 1:
            end_time = appt_time + 30
        elif choice == 2:
            end_time = appt_time + 45
        else:
            print('{} is not a valid, please try again'.format(user_in))
            print('To schedule a haircut, press 1. To schedule a haircut with shampoo, press 2.')
            continue
            
        return Event(appt_time, end_time)


def main():
    scheduler = Scheduler()

    while True:
        event = get_event()
        conflict = scheduler.add_appointment(event)
        if conflict:
            print('Sorry, there is already an appointment at that time.')

if __name__ == "__main__":
    main()