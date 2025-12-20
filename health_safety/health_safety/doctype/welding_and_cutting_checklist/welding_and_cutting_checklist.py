import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname


class WeldingAndCuttingChecklist(Document):
    def before_insert(self):
        # Auto-generate Checklist ID: WCC-YYYY-0001
        if not self.checklist_id:
            self.checklist_id = make_autoname("WCC-.YYYY.-.####")

        # Use checklist_id as document name
        if not self.name:
            self.name = self.checklist_id
