from datetime import date
from Person import Badge
from Worker import Worker
from Manager import Manager
from WorkManagement import WorkManagement

# Initialize WorkManagement
wm = WorkManagement()

# --- Create Workers and Managers ---
w1 = Worker("Luca", "Rossi", "W123", Badge.TIER_1, base_pay=20.0)
w2 = Worker("Giulia", "Neri", "W456", Badge.TIER_2, base_pay=18.0)
m1 = Manager("Anna", "Bianchi", "M789", Badge.TIER_3, base_pay=30.0)

# --- Add turns ---
wm.add_turn(w1, date(2025, 11, 21))
wm.add_turn(w2, date(2025, 11, 22))
wm.add_turn(m1, date(2025, 11, 23))

print("\nTurns after adding:")
print(wm.get_turns())

# --- Promote a worker to manager ---
promoted = wm.promote_manager(w1)
print("\nAfter promotion:")
print(wm.get_turns())

# --- Downgrade a manager to worker ---
downgraded = wm.downgrade_manager(m1)
print("\nAfter downgrade:")
print(wm.get_turns())

# --- Remove a turn ---
wm.remove_turn(w2)
print("\nAfter removing Giulia's turn:")
print(wm.get_turns())