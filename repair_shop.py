"""
Simple Tech Repair Shop System
A beginner-friendly terminal program using OOP concepts.
"""

from abc import ABC, abstractmethod


# Base class for all repair services
class RepairService(ABC):

    def __init__(self, service_id, name, labor_cost):

        # Basic information about the service
        self._service_id = service_id
        self._name = name

        # Private attributes
        self.__labor_cost = labor_cost
        self.__status = "Pending"

    # Get service id
    @property
    def service_id(self):
        return self._service_id

    # Get service name
    @property
    def name(self):
        return self._name

    # Get labor cost
    @property
    def labor_cost(self):
        return self.__labor_cost

    # Change labor cost
    @labor_cost.setter
    def labor_cost(self, value):

        if value < 0:
            raise ValueError("Labor cost cannot be negative.")

        self.__labor_cost = value

    # Get status
    @property
    def status(self):
        return self.__status

    # Change status
    @status.setter
    def status(self, value):

        allowed = ["Pending", "In Progress", "Completed", "Cancelled"]

        if value not in allowed:
            raise ValueError("Invalid status.")

        self.__status = value

    # Every child class must make this method
    @abstractmethod
    def calculate_service_cost(self):
        pass

    # Every child class must make this method
    @abstractmethod
    def display_service_info(self):
        pass


# Class for hardware repairs
class HardwareRepair(RepairService):

    PARTS_TAX = 0.10

    def __init__(self, service_id, name, labor_cost,
                 parts_cost, warranty_months=3):

        super().__init__(service_id, name, labor_cost)

        self.__parts_cost = parts_cost
        self.__warranty_months = warranty_months

    @property
    def parts_cost(self):
        return self.__parts_cost

    @parts_cost.setter
    def parts_cost(self, value):

        if value < 0:
            raise ValueError("Parts cost cannot be negative.")

        self.__parts_cost = value

    @property
    def warranty_months(self):
        return self.__warranty_months

    # Calculate total hardware repair cost
    def calculate_service_cost(self):

        tax = self.__parts_cost * self.PARTS_TAX

        total = self.labor_cost + self.__parts_cost + tax

        return total

    # Show service information
    def display_service_info(self):

        return (
            f"[{self.service_id}] {self.name}\n"
            f"Type      : Hardware Repair\n"
            f"Labor     : ${self.labor_cost}\n"
            f"Parts     : ${self.__parts_cost}\n"
            f"Warranty  : {self.__warranty_months} month(s)\n"
            f"Status    : {self.status}"
        )


# Class for software repairs
class SoftwareRepair(RepairService):

    DIGITAL_FEE = 5

    def __init__(self, service_id, name, labor_cost,
                 license_key, os_version="N/A"):

        super().__init__(service_id, name, labor_cost)

        self.__license_key = license_key
        self.__os_version = os_version

    @property
    def license_key(self):
        return self.__license_key

    @property
    def os_version(self):
        return self.__os_version

    # Calculate software repair cost
    def calculate_service_cost(self):

        return self.labor_cost + self.DIGITAL_FEE

    # Show service information
    def display_service_info(self):

        masked_key = self.__license_key[:4] + "-****"

        return (
            f"[{self.service_id}] {self.name}\n"
            f"Type      : Software Repair\n"
            f"Labor     : ${self.labor_cost}\n"
            f"Fee       : ${self.DIGITAL_FEE}\n"
            f"OS        : {self.__os_version}\n"
            f"License   : {masked_key}\n"
            f"Status    : {self.status}"
        )


# Class for customer invoice
class CustomerInvoice:

    def __init__(self, customer_name):

        self.__customer_name = customer_name
        self.__repairs = []

    # Add repair to invoice
    def add_repair(self, repair):

        self.__repairs.append(repair)

    # Check if invoice is empty
    def is_empty(self):

        return len(self.__repairs) == 0

    # Show current invoice
    def view_invoice(self):

        if self.is_empty():

            print("\nInvoice is empty.\n")
            return

        print("\n===== CURRENT INVOICE =====")

        for repair in self.__repairs:

            print()
            print(repair.display_service_info())

    # Print final bill
    def print_final_bill(self):

        if self.is_empty():

            print("\nNothing to print.\n")
            return

        total = 0

        print("\n===== FINAL BILL =====")
        print(f"Customer: {self.__customer_name}\n")

        for repair in self.__repairs:

            cost = repair.calculate_service_cost()

            total += cost

            print(f"{repair.name} --> ${cost}")

        print("\n-----------------------")
        print(f"TOTAL = ${total}")
        print("-----------------------\n")


# Create available services
def build_catalogue():

    services = [

        HardwareRepair(
            "HW01",
            "Screen Replacement",
            40,
            80,
            6
        ),

        HardwareRepair(
            "HW02",
            "Battery Replacement",
            25,
            30,
            3
        ),

        HardwareRepair(
            "HW03",
            "Motherboard Repair",
            70,
            120,
            12
        ),

        SoftwareRepair(
            "SW01",
            "OS Reinstallation",
            35,
            "WIN1-1234-5678",
            "Windows 11"
        ),

        SoftwareRepair(
            "SW02",
            "Virus Removal",
            30,
            "AV01-ABCD-EFGH",
            "Any"
        )
    ]

    catalogue = {}

    for service in services:

        catalogue[service.service_id] = service

    return catalogue


# Show all services
def view_services(catalogue):

    print("\n===== AVAILABLE SERVICES =====")

    for service in catalogue.values():

        print()
        print(service.display_service_info())


# Add service to invoice
def add_service_to_invoice(catalogue, invoice):

    while True:

        print("\n===== AVAILABLE SERVICES =====\n")

        # Show all services
        for service in catalogue.values():

            print(f"{service.service_id} --> {service.name}")

        # Option to leave
        print("0 --> Back to Main Menu")

        # User input
        service_id = input("\nChoose service id: ").strip().upper()

        # Exit from service menu
        if service_id == "0":

            print("\nReturning to main menu...\n")
            return

        # Add service
        elif service_id in catalogue:

            invoice.add_repair(catalogue[service_id])

            print(f"\n{catalogue[service_id].name} added successfully.\n")

        # Wrong id
        else:

            print("\nInvalid service id.\n")
# Main program
def main():

    print("===== TECH REPAIR SHOP =====\n")

    # Ask customer name
    while True:

        name = input("Enter your name: ").strip()

        if name:
            break

        print("Name cannot be empty.\n")

    catalogue = build_catalogue()

    invoice = CustomerInvoice(name)

    print(f"\nWelcome {name}!\n")

    # Main loop
    while True:

        print("________________________________\n")
        print("1. View Services")
        print("2. Add Service")
        print("3. View Invoice")
        print("4. Print Final Bill")
        print("5. Exit")
        print("________________________________\n")
        choice = input("\nChoose: ").strip()

        if choice == "1":

            view_services(catalogue)

        elif choice == "2":

            add_service_to_invoice(catalogue, invoice)

        elif choice == "3":

            invoice.view_invoice()

        elif choice == "4":

            invoice.print_final_bill()

        elif choice == "5":

            print("\nGoodbye!\n")
            break

        else:

            print("\nInvalid choice.\n")


# Start program
if __name__ == "__main__":

    main()