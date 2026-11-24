# SOLID Principle: Interface Segregation Principle (ISP)

class Printer:
    def print_document(self):
        print("Printing document")

class Scanner:
    def scan_document(self):
        print("Scanning document")

class MultiFunctionPrinter(Printer, Scanner):
    pass

machine = MultiFunctionPrinter()
machine.print_document()
machine.scan_document()
