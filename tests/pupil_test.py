import unittest
from datetime import date

from models.pupil import *
from models.attendance import *

class TestPupil(unittest.TestCase):

    def setUp(self):
        self.pupil1 = Pupil("Harry Potter", date(2010, 7, 31), "Piano", "4", "Rubeus Hagrid", "Sat grade 4 exam in April", True)
        self.pupil2 = Pupil("Hermione Granger", "19-09-2015", "Recorder", "0", "Parents", "Recommended to us by school teacher", True)
        self.attendance1 = Attendance("Beginner Recorder", "Harry Potter")
        self.attendance2 = Attendance("Beginner Recorder", "")
    
    def test_pupil_has_name(self):
        self.assertEqual("Harry Potter", self.pupil1.name)

    def test_pupil_has_dob(self):
        self.assertEqual(date(2010, 7, 31), self.pupil1.dob)

    def test_pupil_has_instrument(self):
        self.assertEqual("Piano", self.pupil1.instrument)
    
    def test_pupil_has_grade(self):
        self.assertEqual("4", self.pupil1.grade)
    
    def test_pupil_has_nok(self):
        self.assertEqual("Rubeus Hagrid", self.pupil1.nok)
    
    def test_pupil_has_notes(self):
        self.assertEqual("Sat grade 4 exam in April", self.pupil1.notes)
    
    def test_pupil_has_id(self):
        self.assertEqual(None, self.pupil1.id)
    
    def test_pupil_has_active_status(self):
        self.assertEqual(True, self.pupil1.active)
    
    def test_count_no_attended_lessons(self):
        self.attendance1.mark_attended()
        attendances = [self.attendance1, self.attendance2]
        self.assertEqual(1, self.pupil1.no_attended(attendances))
