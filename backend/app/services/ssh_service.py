import time
import paramiko
from app.core.crypto import decrypt_value

class SSHService:
    @staticmethod
    def _connect(host: str, port: int, username: str, encrypted_password: str):
        password = decrypt_value(encrypted_password)

        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.RejectPolicy())
        client.connect(
            hostname=host,
            port=port,
            username=username,
            password=password,
            timeout=10,
            banner_timeout=10,
            auth_timeout=10,
            look_for_keys=False,
            allow_agent=False
        )
        return client

    @staticmethod
    def test_connection(host: str, port: int, username: str, encrypted_password: str) -> bool:
        try:
            client = SSHService._connect(host, port, username, encrypted_password)
            client.close()
            return True
        except Exception:
            return False

    @staticmethod
    def run_commands_in_shell(host: str, port: int, username: str, encrypted_password: str, commands: list[str]) -> str:
        client = SSHService._connect(host, port, username, encrypted_password)
        channel = client.invoke_shell()
        output = ""
        try:
            time.sleep(1)
            while channel.recv_ready():
                output += channel.recv(65535).decode("utf-8", errors="ignore")
            for cmd in commands:
                channel.send(cmd + "\n")
                time.sleep(2)
                while channel.recv_ready():
                    output += channel.recv(65535).decode("utf-8", errors="ignore")
            return output
        finally:
            try:
                channel.close()
            except Exception:
                pass
            client.close()
