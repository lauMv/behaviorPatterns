from Mediator import Mediator
from General import General
from Specialties import Specialties

class ConcreteMediator(Mediator):
    def __init__(self, general: General, specialties: Specialties) -> None:
        self.general = general
        self.general.mediator = self
        self.specialties = specialties
        self.specialties.mediator = self

    def bookAnAppointment(self, patient: object, area: str) -> None:
        if area == "Medicina General": 
            print("Mediador clinica a medicina general")
            self.general.generalMedicine()
        elif area == "Pediatria": 
            print("Mediador general a pediatria")
            self.general.pediatrics()
        elif area == "Cardiologia": 
            print("Mediador especialidades a Cardiologia")
            self.specialties.cardiology()
        elif area == "Oftalmologia": 
            print("Mediador especialidades a oftalmologia")
            self.specialties.ophthalmology()