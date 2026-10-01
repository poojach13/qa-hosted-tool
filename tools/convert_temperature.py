from typing import ClassVar

from pydantic import BaseModel, Field
from trase_os_sdk.tools import BaseTool


class TemperatureInput(BaseModel):
    celsius: float = Field(
        description="Temperature in degrees Celsius",
        ge=-273.15,
        allow_inf_nan=False,
    )


class QaConvertTemperature(BaseTool):
    name: ClassVar[str] = "QaConvertTemperature"
    description: ClassVar[str] = "Convert Celsius to Fahrenheit."
    pydantic_inputs: ClassVar[type[BaseModel]] = TemperatureInput
    output_type: ClassVar[str] = "object"

    def forward(self, celsius: float) -> dict:
        inputs = TemperatureInput(celsius=celsius)
        return {"fahrenheit": round(inputs.celsius * 9 / 5 + 32, 1), "build": "v1"}
