from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class SensorReading(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sensor_type: str        # "bin_level", "flow", "toilet_usage"
    location: str           # "Block A Bin 1", "Toilet 2", etc.
    value: float            # e.g. 85.5 (percent full)
    unit: str               # "%", "L/min", "count"
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    