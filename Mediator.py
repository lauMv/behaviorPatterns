from __future__ import annotations
from abc import ABC


class Mediator(ABC):
    
    def bookAnAppointment(self, patient: object, area: str) ->None:
        pass

    