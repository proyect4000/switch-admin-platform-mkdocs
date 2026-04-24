# backend/app/services/backup_service.py

## Propósito

Archivo del proyecto ubicado en `backend/app/services/backup_service.py`.

## Código fuente

```py
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.config_backup import ConfigBackup
from app.services.ssh_service import SSHService

class BackupService:
    @staticmethod
    def get_command(brand: str | None, backup_type: str):
        brand = (brand or "").lower()
        if "cisco" in brand:
            return "show running-config" if backup_type == "running-config" else "show startup-config"
        if "aruba" in brand or "hp" in brand:
            return "show running-config"
        return "show running-config"

    @staticmethod
    def run_backup(db: Session, switch, backup_type: str = "running-config", user_id: int | None = None):
        command = BackupService.get_command(switch.brand, backup_type)
        output = SSHService.run_commands_in_shell(
            switch.ip_address, switch.ssh_port, switch.ssh_username, switch.ssh_password_encrypted,
            ["terminal length 0", command]
        )
        filename = f"{switch.name}_{backup_type}_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.txt"
        backup = ConfigBackup(
            switch_id=switch.id,
            backup_type=backup_type,
            filename=filename,
            content=output,
            created_by=user_id
        )
        db.add(backup)
        db.commit()
        db.refresh(backup)
        return backup
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from datetime import datetime` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from sqlalchemy.orm import Session` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `from app.models.config_backup import ConfigBackup` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `from app.services.ssh_service import SSHService` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 5 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 6 | `class BackupService:` | Declara la clase `BackupService` como unidad principal de este bloque. |
| 7 | `    @staticmethod` | Decorador que modifica o registra el comportamiento del elemento definido a continuación. |
| 8 | `    def get_command(brand: str \| None, backup_type: str):` | Declara la función `get_command` con la lógica que se ejecutará cuando sea invocada. |
| 9 | `        brand = (brand or "").lower()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `        if "cisco" in brand:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 11 | `            return "show running-config" if backup_type == "running-config" else "show startup-config"` | Devuelve el resultado de la función al código que la llamó. |
| 12 | `        if "aruba" in brand or "hp" in brand:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 13 | `            return "show running-config"` | Devuelve el resultado de la función al código que la llamó. |
| 14 | `        return "show running-config"` | Devuelve el resultado de la función al código que la llamó. |
| 15 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 16 | `    @staticmethod` | Decorador que modifica o registra el comportamiento del elemento definido a continuación. |
| 17 | `    def run_backup(db: Session, switch, backup_type: str = "running-config", user_id: int \| None = None):` | Declara la función `run_backup` con la lógica que se ejecutará cuando sea invocada. |
| 18 | `        command = BackupService.get_command(switch.brand, backup_type)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 19 | `        output = SSHService.run_commands_in_shell(` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 20 | `            switch.ip_address, switch.ssh_port, switch.ssh_username, switch.ssh_password_encrypted,` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 21 | `            ["terminal length 0", command]` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 22 | `        )` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 23 | `        filename = f"{switch.name}_{backup_type}_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.txt"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 24 | `        backup = ConfigBackup(` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 25 | `            switch_id=switch.id,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 26 | `            backup_type=backup_type,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 27 | `            filename=filename,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 28 | `            content=output,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 29 | `            created_by=user_id` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 30 | `        )` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 31 | `        db.add(backup)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 32 | `        db.commit()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 33 | `        db.refresh(backup)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 34 | `        return backup` | Devuelve el resultado de la función al código que la llamó. |