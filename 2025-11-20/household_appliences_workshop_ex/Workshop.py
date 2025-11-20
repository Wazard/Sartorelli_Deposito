from RefurbishTicket import RefurbishTicket, TicketStatus

class Workshop:
    def __init__(self, name: str):
        self.__name = name
        self.__tickets: list[RefurbishTicket] = []

    # --- Getters ---
    def get_name(self) -> str:
        return self.__name

    def get_tickets(self) -> list[RefurbishTicket]:
        return self.__tickets

    # --- Ticket Management ---
    def add_ticket(self, ticket: RefurbishTicket) -> None:
        self.__tickets.append(ticket)

    def close_ticket(self, ticket_id: str) -> None:
        for ticket in self.__tickets:
            if ticket.get_ticket_id() == ticket_id:
                ticket.set_status(TicketStatus.CLOSED)
                return
        raise ValueError(f"No ticket found with ID {ticket_id}")

    def get_open_tickets(self) -> list[RefurbishTicket]:
        return [t for t in self.__tickets if t.get_status() == TicketStatus.OPEN]

    def get_closed_tickets(self) -> list[RefurbishTicket]:
        return [t for t in self.__tickets if t.get_status() == TicketStatus.CLOSED]

    def get_total_costs(self) -> float:
        return round(sum(t.total_cost_estimate() for t in self.__tickets), 2)

    # --- Utility ---
    def description(self) -> str:
        return (f"Workshop: {self.__name} | "
                f"Tickets: {len(self.__tickets)} | "
                f"Open: {len(self.get_open_tickets())} | "
                f"Closed: {len(self.get_closed_tickets())}")

    def report(self) -> str:
    
        #Returns a formatted report:
        # Appliance | amount in warehouse | total revenue

        summary: dict[str, dict[str, float]] = {} # using a nested dictionary seemed like the only solution available

        for ticket in self.__tickets:
            appliance = ticket.get_appliance()
            appliance_type = appliance.get_name()  # e.g. WashingMachine, Oven, Refrigeration
            cost = ticket.total_cost_estimate()

            if appliance_type not in summary:
                summary[appliance_type] = {"count": 0, "revenue": 0.0} # initializing the dictionaries

            summary[appliance_type]["count"] += 1
            summary[appliance_type]["revenue"] += cost

        # Build table string
        lines = ["Appliance | amount in warehouse | total revenue"] # hard coding the first line
        for appliance_type, data in summary.items():
            lines.append(f"{appliance_type} | {data['count']} | {int(data['revenue'])}")

        return "\n".join(lines)