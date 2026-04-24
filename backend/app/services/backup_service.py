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
