from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    tipo_usuario: str
    nombre_usuario: str
    correo_electronico: str
    contrasena: str
    numero_telefono: str
    estatus: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int
    fecha_registro: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None

    class Config:
        from_attributes = True  # Cambio de orm_mode a from_attributes (Pydantic v2)
