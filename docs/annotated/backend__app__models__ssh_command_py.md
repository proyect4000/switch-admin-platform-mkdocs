# backend/app/models/ssh_command.py

## Propósito

Archivo del proyecto ubicado en `backend/app/models/ssh_command.py`.

## Código fuente

```py
from sqlalchemy import Column, Integer, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class SSHCommand(Base):
    __tablename__ = "ssh_commands"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("ssh_sessions.id", ondelete="CASCADE"), nullable=False)
    command_text = Column(Text, nullable=False)
    output_text = Column(Text, nullable=True)
    executed_at = Column(DateTime, server_default=func.now())
    success = Column(Boolean, default=True)
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from sqlalchemy import Column, Integer, Text, DateTime, Boolean, ForeignKey` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from sqlalchemy.sql import func` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `from app.core.database import Base` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 5 | `class SSHCommand(Base):` | Declara la clase `SSHCommand` como unidad principal de este bloque. |
| 6 | `    __tablename__ = "ssh_commands"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 8 | `    id = Column(Integer, primary_key=True, index=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `    session_id = Column(Integer, ForeignKey("ssh_sessions.id", ondelete="CASCADE"), nullable=False)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `    command_text = Column(Text, nullable=False)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `    output_text = Column(Text, nullable=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `    executed_at = Column(DateTime, server_default=func.now())` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 13 | `    success = Column(Boolean, default=True)` | Asigna un valor a una variable o atributo para usarlo más adelante. |