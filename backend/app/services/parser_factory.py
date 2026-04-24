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
