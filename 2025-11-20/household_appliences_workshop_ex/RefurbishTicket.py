import hashlib
from enum import Enum
from Appliance import Appliance

class TicketStatus(Enum):
    OPEN = "Open"
    CLOSED = "Closed"

class RefurbishTicket:
    __counter = 0  # static counter for unique IDs

    def __init__(self, appliance: Appliance, status: TicketStatus = TicketStatus.OPEN):
        # Generate unique 16-char ticket_id
        RefurbishTicket.__counter += 1
        raw_id = f"{appliance.get_make()}-{appliance.get_model()}-{RefurbishTicket.__counter}"
        self.__ticket_id = hashlib.sha256(raw_id.encode()).hexdigest()[:9]

        # Appliance association
        self.__appliance = appliance

        # Status validation
        self.__status = TicketStatus
        self.__notes = ""

    # --- Getters ---
    def get_ticket_id(self) -> str:
        return self.__ticket_id

    def get_appliance(self) -> Appliance:
        return self.__appliance

    def get_status(self) -> TicketStatus:
        return self.__status

    def get_notes(self) -> str:
        return self.__notes

    # --- Setters ---
    def set_appliance(self, appliance: Appliance) -> None:
        self.__appliance = appliance

    def set_status(self, status: TicketStatus) -> None:
        self.__status = status

    def set_notes(self, notes: str) -> None:
        self.__notes = notes

    # --- Utility Methods ---
    def add_notes(self, notes: str) -> None:
        self.set_notes(notes)

    def total_cost_estimate(self, *extras: float) -> float:

        # Compute total cost estimate:
        # - Base cost from Appliance
        # - Add any extras passed in

        base_cost = self.__appliance.base_cost_estimate()
        total = base_cost + sum(extras)
        return round(total, 2)

    def description(self) -> str:
        # Readable summary of the ticket.
        return (f"Ticket {self.__ticket_id} | Status: {self.__status} | "
                f"Appliance: {self.__appliance.description()} | Notes: {self.__notes}")