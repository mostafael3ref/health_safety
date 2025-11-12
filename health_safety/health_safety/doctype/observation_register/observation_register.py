import frappe
from frappe.model.document import Document


class ObservationRegister(Document):
    def on_update(self):
        self.update_observation_status()

    def on_submit(self):
        self.update_observation_status()

    def update_observation_status(self):
        """Update status field of linked Observation Record based on counts."""
        if not self.observation_reference:
            return

        if not frappe.db.exists("Observation Record", self.observation_reference):
            return

        obs = frappe.get_doc("Observation Record", self.observation_reference)

        new_obs = self.number_of_new_observation_raised or 0
        old_obs = self.number_of_old_observation_raised or 0
        open_obs = self.observation_currently_open or 0

        # منطق بسيط:
        # - لو مفيش Observation مفتوحة -> Closed
        # - لو في Old + Open -> In Progress
        # - غير كده -> Open
        if open_obs <= 0:
            obs.status = "Closed"
        elif old_obs > 0 and open_obs > 0:
            obs.status = "In Progress"
        else:
            obs.status = "Open"

        obs.save(ignore_permissions=True)
