from WashingMachine import WashingMachine
from Refrigerator import Refrigerator
from Oven import Oven
from RefurbishTicket import RefurbishTicket, TicketStatus
from Workshop import Workshop


def main():
    # --- Create Appliances ---
    # --- Create Appliances ---
    appliances = [
        WashingMachine("Bosch", "EcoWash300", 2019, load_capacity=6.0, spin_speed=1000),
        WashingMachine("Samsung", "QuickSpin", 2020, load_capacity=9.0, spin_speed=1400),
        WashingMachine("Whirlpool", "FreshClean", 2021, load_capacity=7.5, spin_speed=1200),
        WashingMachine("Miele", "ProLine", 2018, load_capacity=10.0, spin_speed=1600),
        WashingMachine("AEG", "SilentWash", 2022, load_capacity=8.0, spin_speed=1300),
        Refrigerator("LG", "CoolSaver", 2020, load_capacity=70.0, has_freezer=True),
        Refrigerator("Bosch", "IceBox", 2019, load_capacity=50.0, has_freezer=False),
        Refrigerator("Electrolux", "ChillMax", 2021, load_capacity=80.0, has_freezer=True),
        Refrigerator("Whirlpool", "FreezePro", 2018, load_capacity=90.0, has_freezer=True),
        Refrigerator("Samsung", "SmartCool", 2022, load_capacity=60.0, has_freezer=False),
        Oven("Bosch", "BakeMaster", 2019, oven_type="electric", is_ventilated=True),
        Oven("Whirlpool", "HeatWave", 2020, oven_type="gas", is_ventilated=False),
        Oven("Electrolux", "ChefLine", 2021, oven_type="electric", is_ventilated=False),
        Oven("Miele", "ProBake", 2018, oven_type="gas", is_ventilated=True),
        Oven("Siemens", "SmartHeat", 2022, oven_type="electric", is_ventilated=True),
        WashingMachine("Candy", "RapidWash", 2020, load_capacity=6.5, spin_speed=1100),
        WashingMachine("Indesit", "DailyWash", 2021, load_capacity=7.0, spin_speed=1200),
        WashingMachine("Haier", "UltraSpin", 2022, load_capacity=9.0, spin_speed=1500),
        Refrigerator("Haier", "MegaCool", 2021, load_capacity=100.0, has_freezer=True),
        Refrigerator("Indesit", "CompactChill", 2020, load_capacity=45.0, has_freezer=False),
    ]

    # --- Create Tickets ---
    tickets = [RefurbishTicket(appliance, status=TicketStatus.OPEN) for appliance in appliances]

    # --- Create Workshop ---
    workshop = Workshop("Central Repair Hub")

    # Add tickets
    for ticket in tickets:
        workshop.add_ticket(ticket)

    # --- Test functionality ---
    print(workshop.description())
    print("\nInitial Report:")
    print(workshop.report())

    # Close a couple of tickets
    workshop.close_ticket(tickets[0].get_ticket_id())
    workshop.close_ticket(tickets[2].get_ticket_id())
    workshop.close_ticket(tickets[5].get_ticket_id())
    workshop.close_ticket(tickets[7].get_ticket_id())
    workshop.close_ticket(tickets[12].get_ticket_id())
    workshop.close_ticket(tickets[17].get_ticket_id())

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
    print(f"{tickets[2].get_ticket_id()} cost with extras:", tickets[2].total_cost_estimate(25.0, 40.0))

    # --- Additional Usage Examples ---
    # Add notes to a ticket
    tickets[2].add_notes("Customer requested urgent repair.")
    print("\nTicket with notes added:")
    print(tickets[2].description())

    # Re-open a closed ticket
    tickets[0].set_status(TicketStatus.OPEN.value)
    print("\nRe-opened Ticket:")
    print(tickets[0].description())

    # Create a second workshop and transfer a ticket
    secondary_workshop = Workshop("Branch Repair Hub")
    secondary_workshop.add_ticket(tickets[8])
    print("\nSecondary Workshop Report:")
    print(secondary_workshop.report())

    # Iterate over all tickets and print appliance-specific details
    print("\nDetailed Appliance Info:")
    for t in workshop.get_tickets():
        appliance = t.get_appliance()
        print(f"{appliance.get_name()} -> {appliance.description()} | Cost: {t.total_cost_estimate()}")


if __name__ == "__main__":
    main()