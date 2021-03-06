from datetime import date

class Lesson:

    def __init__(self, name, date, time, instrument, tutor, max_capacity, group_status=False, id=None):
        self.name = name
        self.date = date
        self.time = time
        self.instrument = instrument
        self.tutor = tutor
        self.max_capacity = max_capacity
        self.attendees = []
        self.fee = 10.00
        self.group_status = group_status
        self.id = id


    def add_attendees_to_lesson(self, input_attendees):
        for attendee in input_attendees:
            self.attendees.append(attendee)
    
    def count_free_spaces(self):
        no_attendees = len(self.attendees)
        spaces = self.max_capacity - no_attendees
        return spaces
        
    def print_free_spaces(self):
        spaces = self.count_free_spaces()
        print(spaces)

    def count_attendees(self):
        no_attendees = len(self.attendees)
        return no_attendees

    def todays_date(self):
        today = date.today()
        print(today)
        return today
        

