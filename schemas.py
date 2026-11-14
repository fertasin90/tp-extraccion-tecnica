from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class ExtraccionTecnica(BaseModel):
    model_config = ConfigDict(extra="forbid")

    tecnologias: list[str] = Field(
        description="Tecnologías mencionadas explícitamente en el texto."
    )
    nivel_de_criticidad: Literal["baja", "media", "alta", "indeterminada"] = Field(
        description="Nivel de impacto operativo según la evidencia del texto."
    )
    resumen_tecnico: str = Field(
        min_length=1, description="Resumen breve en español basado en el texto."
    )
