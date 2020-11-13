from Specialties import Specialties
from General import General
from ConcreteMediator import ConcreteMediator

if __name__ == "__main__":
    # The client code.
    specialties = Specialties()
    general = General()
    mediator = ConcreteMediator(general, specialties)

    specialties.cardiology()

    print("\n", end="")

    print("Client triggers operation D.")
    general.pediatrics()