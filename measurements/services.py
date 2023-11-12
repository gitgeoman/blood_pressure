from abc import ABC, abstractmethod

from dataclasses import dataclass
from datetime import datetime
from faker import Faker

faker = Faker()

@dataclass
class Measurement:
    id: int
    date: datetime
    systolic: int
    diastolic: int


class IMeasurementsService(ABC):

    @abstractmethod
    def list() -> list[Measurement]:
        pass

class FakeMeasurementsService(IMeasurementsService):
    id = 1

    @classmethod
    def list(cls) -> list[Measurement]:
        
        ms = []
        for i in range(1, 26):
            ms.append(
       
                Measurement(
                    id=i,
                    date=faker.date_time(),
                    systolic = faker.random.randint(60, 250),
                    diastolic=faker.random.randint(30, 180)
                )
            )
        
    
        return ms
    

class InMemoeryMeasurementService(IMeasurementsService):
    id = 1
    measurements: list[Measurement] = []

    @classmethod
    def list(cls) -> list[Measurement]:
        return cls.measurements
    

    @classmethod
    def create(cls, systolic: int, diastolic: int, date: datetime) -> Measurement:

        m = Measurement(
            id=cls.id,
            date=date,
            systolic=systolic,
            diastolic=diastolic
        )

        cls.measurements.append(m)

        cls.id += 1
        return m