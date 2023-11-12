import json
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
    def serialize(self):
        v = vars(self).copy()
        v["date"] = v["date"].isoformat() 
        return v
    @classmethod
    def deserialize(cls, data: dict) -> 'Measurement':
        data["date"] = datetime.fromisoformat(data["date"])
        return cls(**data)

class IMeasurementsService(ABC):

    @abstractmethod
    def list() -> list[Measurement]:
        pass

    @abstractmethod
    def create() -> Measurement:
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
    
    
    @classmethod
    def create(cls, systolic: int, diastolic: int, date: datetime) -> Measurement:

        m = Measurement(
            id=1,
            date=date,
            systolic=systolic,
            diastolic=diastolic
        )

        return m


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
        # xxx = [{"id": m.id, "data": m.date, ...}, ]
        # for x in xxx:
        #     m = Measurement(**x)  # Measurement(id=1, date="2023-11-11T12:00")
        cls.measurements.append(m)

        cls.id += 1
        return m


class JsonMeasurementService(IMeasurementsService):
    id = 1
    filename = "baza.json"

    @classmethod
    def _load_data(cls) -> list[Measurement]:
        print("Load data")
        try:
            with open(cls.filename) as f:
                raw_data = json.load(f)
                data = [Measurement.deserialize(d) for d in raw_data] 
        except FileNotFoundError:
            data = []

        cls.id = len(data) + 1
        return data

    @classmethod
    def _save_data(cls, measurements: list[Measurement] ):
        print("Save data")
        serialized_data = [m.serialize() for m in measurements]
        with open(cls.filename, "w") as f:
            json.dump(serialized_data, f)

    @classmethod
    def list(cls) -> list[Measurement]:
        measurements: list[Measurement] = cls._load_data()
        return measurements
    

    @classmethod
    def create(cls, systolic: int, diastolic: int, date: datetime) -> Measurement:
        measurements = cls._load_data()

        m = Measurement(
            id=cls.id,
            date=date,
            systolic=systolic,
            diastolic=diastolic
        )

        measurements.append(m)
        cls.id += 1
        cls._save_data(measurements)
        return m