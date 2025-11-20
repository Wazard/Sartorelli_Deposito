from WashingMachine import WashingMachine
from Refrigerator import Refrigerator
from Oven import Oven
from RefurbishTicket import RefurbishTicket, TicketStatus
from Workshop import Workshop


def main():
    # --- Create Appliances ---
    wm1 = WashingMachine("Bosch", "WMX100", 2020, load_capacity=7.0, spin_speed=1200)
    wm2 = WashingMachine("LG", "TurboWash", 2021, load_capacity=8.0, spin_speed=1400)

    fridge1 = Refrigerator("Samsung", "CoolMax", 2019, load_capacity=65.0, has_freezer=True)
    fridge2 = Refrigerator("Whirlpool", "FreshLine", 2022, load_capacity=55.0, has_freezer=False)

    oven1 = Oven("Electrolux", "BakePro", 2018, oven_type="gas", is_ventilated=True)
    oven2 = Oven("Siemens", "HeatMaster", 2021, oven_type="electric", is_ventilated=False)

    # --- Create Tickets ---
    ticket1 = RefurbishTicket(wm1, status=TicketStatus.OPEN.value)
    ticket2 = RefurbishTicket(wm2, status=TicketStatus.OPEN.value)
    ticket3 = RefurbishTicket(fridge1, status=TicketStatus.OPEN.value)
    ticket4 = RefurbishTicket(fridge2, status=TicketStatus.OPEN.value)
    ticket5 = RefurbishTicket(oven1, status=TicketStatus.OPEN.value)
    ticket6 = RefurbishTicket(oven2, status=TicketStatus.OPEN.value)

    # --- Create Workshop ---
    workshop = Workshop("Central Repair Hub")

    # Add tickets
    for t in [ticket1, ticket2, ticket3, ticket4, ticket5, ticket6]:
        workshop.add_ticket(t)

    # --- Test functionality ---
    print(workshop.description())
    print("\nInitial Report:")
    print(workshop.report())

    # Close a couple of tickets
    workshop.close_ticket(ticket1.get_ticket_id())
    workshop.close_ticket(ticket3.get_ticket_id())

    print("\nAfter Closing Some Tickets:")
    print(workshop.description())

    # Show open and closed tickets
    print("\nOpen Tickets:")
    for t in workshop.get_open_tickets():
        print(t.description())

    print("\nClosed Tickets:")
    for t in workshop.get_closed_tickets():
        print(t.description())

    # Total costs
    print("\nTotal Costs of All Tickets:", workshop.get_total_costs())

    # Demonstrate extras in cost estimate
    print("\nTicket with extras:")
    print(f"{ticket2.get_ticket_id()} cost with extras:", ticket2.total_cost_estimate(25.0, 40.0))

    # --- Additional Usage Examples ---
    # Add notes to a ticket
    ticket2.add_notes("Customer requested urgent repair.")
    print("\nTicket with notes added:")
    print(ticket2.description())

    # Re-open a closed ticket
    ticket1.set_status(TicketStatus.OPEN.value)
    print("\nRe-opened Ticket:")
    print(ticket1.description())

    # Create a second workshop and transfer a ticket
    secondary_workshop = Workshop("Branch Repair Hub")
    secondary_workshop.add_ticket(ticket4)
    print("\nSecondary Workshop Report:")
    print(secondary_workshop.report())

    # Iterate over all tickets and print appliance-specific details
    print("\nDetailed Appliance Info:")
    for t in workshop.get_tickets():
        appliance = t.get_appliance()
        print(f"{appliance.get_name()} -> {appliance.description()} | Cost: {t.total_cost_estimate()}")


if __name__ == "__main__":
    main()