# health_safety/health_safety/doctype/equipment/equipment.py

import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class Equipment(Document):
    def before_insert(self):
        # Generate unique Stomach Number if empty
        if not self.stomach_number:
            self.stomach_number = make_autoname("EQU-.YYYY.-.####")

        # Set document name as stomach_number
        if not self.name:
            self.name = self.stomach_number
