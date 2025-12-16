# health_safety/health_safety/doctype/housekeeping_checklist/housekeeping_checklist.py

import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname


class HousekeepingChecklist(Document):
    def before_insert(self):
        # Generate unique ID if empty (HC-YYYY-0001)
        if not self.checklist_id:
            self.checklist_id = make_autoname("HC-.YYYY.-.####")

        # Use checklist_id as the document name
        if not self.name:
            self.name = self.checklist_id
