# backend/app/services/parser_factory.py

## Propósito

Archivo del proyecto ubicado en `backend/app/services/parser_factory.py`.

## Código fuente

```py
from app.parsers.cisco_parser import CiscoParser
from app.parsers.aruba_parser import ArubaParser
from app.parsers.generic_parser import GenericParser

class ParserFactory:
    @staticmethod
    def get_parser(brand: str | None):
        brand = (brand or "").lower()
        if "cisco" in brand:
            return CiscoParser
        if "aruba" in brand or "hp" in brand:
            return ArubaParser
        return GenericParser
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from app.parsers.cisco_parser import CiscoParser` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from app.parsers.aruba_parser import ArubaParser` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `from app.parsers.generic_parser import GenericParser` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 5 | `class ParserFactory:` | Declara la clase `ParserFactory` como unidad principal de este bloque. |
| 6 | `    @staticmethod` | Decorador que modifica o registra el comportamiento del elemento definido a continuación. |
| 7 | `    def get_parser(brand: str \| None):` | Declara la función `get_parser` con la lógica que se ejecutará cuando sea invocada. |
| 8 | `        brand = (brand or "").lower()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `        if "cisco" in brand:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 10 | `            return CiscoParser` | Devuelve el resultado de la función al código que la llamó. |
| 11 | `        if "aruba" in brand or "hp" in brand:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 12 | `            return ArubaParser` | Devuelve el resultado de la función al código que la llamó. |
| 13 | `        return GenericParser` | Devuelve el resultado de la función al código que la llamó. |