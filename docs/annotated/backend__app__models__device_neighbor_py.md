# backend/app/models/device_neighbor.py

## Propósito

Archivo del proyecto ubicado en `backend/app/models/device_neighbor.py`.

## Código fuente

```py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class DeviceNeighbor(Base):
    __tablename__ = "device_neighbors"

    id = Column(Integer, primary_key=True, index=True)
    switch_id = Column(Integer, ForeignKey("switches.id", ondelete="CASCADE"), nullable=False)
    local_port = Column(String(100), nullable=False)
    neighbor_name = Column(String(150), nullable=True)
    neighbor_ip = Column(String(45), nullable=True)
    neighbor_platform = Column(String(150), nullable=True)
    neighbor_port = Column(String(100), nullable=True)
    protocol = Column(String(20), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from sqlalchemy import Column, Integer, String, DateTime, ForeignKey` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from sqlalchemy.sql import func` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `from app.core.database import Base` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 5 | `class DeviceNeighbor(Base):` | Declara la clase `DeviceNeighbor` como unidad principal de este bloque. |
| 6 | `    __tablename__ = "device_neighbors"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 8 | `    id = Column(Integer, primary_key=True, index=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `    switch_id = Column(Integer, ForeignKey("switches.id", ondelete="CASCADE"), nullable=False)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `    local_port = Column(String(100), nullable=False)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `    neighbor_name = Column(String(150), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `    neighbor_ip = Column(String(45), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 13 | `    neighbor_platform = Column(String(150), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 14 | `    neighbor_port = Column(String(100), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 15 | `    protocol = Column(String(20), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 16 | `    created_at = Column(DateTime, server_default=func.now())` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 17 | `    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())` | Asigna un valor a una variable o atributo para usarlo más adelante. |