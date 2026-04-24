# backend/app/services/ssh_service.py

## Propósito

Archivo del proyecto ubicado en `backend/app/services/ssh_service.py`.

## Código fuente

```py
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
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `import time` | Importa un módulo o paquete necesario para este archivo. |
| 2 | `import paramiko` | Importa un módulo o paquete necesario para este archivo. |
| 3 | `from app.core.crypto import decrypt_value` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 5 | `class SSHService:` | Declara la clase `SSHService` como unidad principal de este bloque. |
| 6 | `    @staticmethod` | Decorador que modifica o registra el comportamiento del elemento definido a continuación. |
| 7 | `    def _connect(host: str, port: int, username: str, encrypted_password: str):` | Declara la función `_connect` con la lógica que se ejecutará cuando sea invocada. |
| 8 | `        password = decrypt_value(encrypted_password)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 10 | `        client = paramiko.SSHClient()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `        client.load_system_host_keys()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 12 | `        client.set_missing_host_key_policy(paramiko.RejectPolicy())` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 13 | `        client.connect(` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 14 | `            hostname=host,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 15 | `            port=port,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 16 | `            username=username,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 17 | `            password=password,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 18 | `            timeout=10,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 19 | `            banner_timeout=10,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 20 | `            auth_timeout=10,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 21 | `            look_for_keys=False,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 22 | `            allow_agent=False` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 23 | `        )` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 24 | `        return client` | Devuelve el resultado de la función al código que la llamó. |
| 25 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 26 | `    @staticmethod` | Decorador que modifica o registra el comportamiento del elemento definido a continuación. |
| 27 | `    def test_connection(host: str, port: int, username: str, encrypted_password: str) -> bool:` | Declara la función `test_connection` con la lógica que se ejecutará cuando sea invocada. |
| 28 | `        try:` | Inicio del manejo controlado de errores para operaciones riesgosas. |
| 29 | `            client = SSHService._connect(host, port, username, encrypted_password)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 30 | `            client.close()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 31 | `            return True` | Devuelve el resultado de la función al código que la llamó. |
| 32 | `        except Exception:` | Captura una excepción específica para responder sin interrumpir toda la aplicación. |
| 33 | `            return False` | Devuelve el resultado de la función al código que la llamó. |
| 34 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 35 | `    @staticmethod` | Decorador que modifica o registra el comportamiento del elemento definido a continuación. |
| 36 | `    def run_commands_in_shell(host: str, port: int, username: str, encrypted_password: str, commands: list[str]) -> str:` | Declara la función `run_commands_in_shell` con la lógica que se ejecutará cuando sea invocada. |
| 37 | `        client = SSHService._connect(host, port, username, encrypted_password)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 38 | `        channel = client.invoke_shell()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 39 | `        output = ""` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 40 | `        try:` | Inicio del manejo controlado de errores para operaciones riesgosas. |
| 41 | `            time.sleep(1)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 42 | `            while channel.recv_ready():` | Inicia un ciclo que se repetirá mientras la condición sea verdadera. |
| 43 | `                output += channel.recv(65535).decode("utf-8", errors="ignore")` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 44 | `            for cmd in commands:` | Itera sobre una colección para procesar sus elementos uno por uno. |
| 45 | `                channel.send(cmd + "\n")` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 46 | `                time.sleep(2)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 47 | `                while channel.recv_ready():` | Inicia un ciclo que se repetirá mientras la condición sea verdadera. |
| 48 | `                    output += channel.recv(65535).decode("utf-8", errors="ignore")` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 49 | `            return output` | Devuelve el resultado de la función al código que la llamó. |
| 50 | `        finally:` | Bloque de cierre que se ejecuta siempre, útil para liberar recursos. |
| 51 | `            try:` | Inicio del manejo controlado de errores para operaciones riesgosas. |
| 52 | `                channel.close()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 53 | `            except Exception:` | Captura una excepción específica para responder sin interrumpir toda la aplicación. |
| 54 | `                pass` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 55 | `            client.close()` | Línea de implementación que forma parte del comportamiento interno del archivo. |