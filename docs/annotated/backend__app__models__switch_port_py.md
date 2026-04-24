# backend/app/models/switch_port.py

## Propósito

Archivo del proyecto ubicado en `backend/app/models/switch_port.py`.

## Código fuente

```py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class SwitchPort(Base):
    __tablename__ = "switch_ports"

    id = Column(Integer, primary_key=True, index=True)
    switch_id = Column(Integer, ForeignKey("switches.id", ondelete="CASCADE"), nullable=False)
    port_name = Column(String(50), nullable=False)
    port_number = Column(Integer, nullable=True)
    description = Column(String(200), nullable=True)
    admin_status = Column(String(20), default="down")
    oper_status = Column(String(20), default="down")
    speed = Column(String(30), nullable=True)
    duplex = Column(String(20), nullable=True)
    vlan = Column(String(30), nullable=True)
    mac_address = Column(String(50), nullable=True)
    connected_device_name = Column(String(150), nullable=True)
    connected_device_ip = Column(String(45), nullable=True)
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
| 5 | `class SwitchPort(Base):` | Declara la clase `SwitchPort` como unidad principal de este bloque. |
| 6 | `    __tablename__ = "switch_ports"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 8 | `    id = Column(Integer, primary_key=True, index=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `    switch_id = Column(Integer, ForeignKey("switches.id", ondelete="CASCADE"), nullable=False)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `    port_name = Column(String(50), nullable=False)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `    port_number = Column(Integer, nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `    description = Column(String(200), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 13 | `    admin_status = Column(String(20), default="down")` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 14 | `    oper_status = Column(String(20), default="down")` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 15 | `    speed = Column(String(30), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 16 | `    duplex = Column(String(20), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 17 | `    vlan = Column(String(30), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 18 | `    mac_address = Column(String(50), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 19 | `    connected_device_name = Column(String(150), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 20 | `    connected_device_ip = Column(String(45), nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 21 | `    created_at = Column(DateTime, server_default=func.now())` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 22 | `    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())` | Asigna un valor a una variable o atributo para usarlo más adelante. |