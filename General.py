from ClinicInterface import ClinicInterface

class General(ClinicInterface):
    
    def generalMedicine(self) -> None:
        print("saco una cita para medicina general")
        self.mediator.bookAnAppointment(self, "Medicina General")

    def pediatrics(self)-> None:
        print("saco una cita en medicina general para pediatria")
        self.mediator.bookAnAppointment(self, "Pediatria")
          