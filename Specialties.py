from ClinicInterface import ClinicInterface

class Specialties(ClinicInterface):
    
    def cardiology(self) -> None:
        print ("Se reservo una cita en especialidades para Cardiologia")
        self.mediator.bookAnAppointment(self,"Medicina General")
        self.mediator.bookAnAppointment(self, "Cardiologia")

    def ophthalmology(self) -> None:
        print ("Se reservo una cita en especialidades para Oftalmologia")
        self.mediator.bookAnAppointment(self, "Oftalmologia")