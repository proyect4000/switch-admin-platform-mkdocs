# backend/app/models/device_link.py

## Propósito

Archivo del proyecto ubicado en `backend/app/models/device_link.py`.

## Código fuente

```py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class DeviceLink(Base):
    __tablename__ = "device_links"

    id = Column(Integer, primary_key=True, index=True)
    source_switch_id = Column(Integer, ForeignKey("switches.id", ondelete="CASCADE"), nullable=False)
    source_port_id = Column(Integer, ForeignKey("switch_ports.id", ondelete="SET NULL"), nullable=True)
    target_switch_id = Column(Integer, ForeignKey("switches.id", ondelete="CASCADE"), nullable=False)
    target_port_id = Column(Integer, ForeignKey("switch_ports.id", ondelete="SET NULL"), nullable=True)
    link_type = Column(String(30), default="uplink")
    status = Column(String(20), default="active")
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
| 5 | `class DeviceLink(Base):` | Declara la clase `DeviceLink` como unidad principal de este bloque. |
| 6 | `    __tablename__ = "device_links"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 8 | `    id = Column(Integer, primary_key=True, index=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `    source_switch_id = Column(Integer, ForeignKey("switches.id", ondelete="CASCADE"), nullable=False)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `    source_port_id = Column(Integer, ForeignKey("switch_ports.id", ondelete="SET NULL"), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `    target_switch_id = Column(Integer, ForeignKey("switches.id", ondelete="CASCADE"), nullable=False)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `    target_port_id = Column(Integer, ForeignKey("switch_ports.id", ondelete="SET NULL"), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 13 | `    link_type = Column(String(30), default="uplink")` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 14 | `    status = Column(String(20), default="active")` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 15 | `    created_at = Column(DateTime, server_default=func.now())` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 16 | `    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())` | Asigna un valor a una variable o atributo para usarlo más adelante. |