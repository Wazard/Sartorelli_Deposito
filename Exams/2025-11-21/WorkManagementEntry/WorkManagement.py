from datetime import date
from Worker import Worker
from Manager import Manager
from Person import Badge

BADGE_ORDER = [Badge.TIER_1, Badge.TIER_2, Badge.TIER_3]


class WorkManagement:
    def __init__(self):
        # Dictionary: {Person: working_day}
        self.turns = {}

    def add_turn(self, person: Worker, working_day: date):
        # Assign a worker/manager to a working day.
        self.turns[person] = working_day
        print(f"Added turn: {person.name} {person.surname} on {working_day}")

    def remove_turn(self, person: Worker):
        # Remove a worker/manager from the schedule.
        if person in self.turns:
            removed_day = self.turns.pop(person)
            print(f"Removed turn: {person.name} {person.surname} from {removed_day}")
        else:
            print(f"{person.name} {person.surname} has no assigned turn.")

    def promote_manager(self, worker: Worker) -> Manager:
        # Promote a Worker to Manager by moving up one step in BADGE_ORDER.
        idx = BADGE_ORDER.index(worker.badge)
        new_badge = BADGE_ORDER[min(idx + 1, len(BADGE_ORDER) - 1)]
        manager = Manager(worker.name, worker.surname, worker.person_id, new_badge, worker.base_pay)
        if worker in self.turns:
            self.turns[manager] = self.turns.pop(worker)
        print(f"Promoted {worker.name} {worker.surname} to Manager with badge {new_badge}.")
        return manager

    def downgrade_manager(self, manager: Manager) -> Worker:
        # Downgrade a Manager to Worker by moving down one step in BADGE_ORDER.
        idx = BADGE_ORDER.index(manager.badge)
        new_badge = BADGE_ORDER[max(idx - 1, 0)]
        worker = Worker(manager.name, manager.surname, manager.person_id, new_badge, manager.base_pay)
        if manager in self.turns:
            self.turns[worker] = self.turns.pop(manager)
        print(f"Downgraded {manager.name} {manager.surname} to Worker with badge {new_badge}.")
        return worker

    def get_turns(self):
        # Return all scheduled turns.
        return {f"{p.name} {p.surname}": day for p, day in self.turns.items()}