import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname


class ScaffoldingSafetyChecklist(Document):
    def before_insert(self):
        # Generate ID: SSC-YYYY-0001
        if not self.checklist_id:
            self.checklist_id = make_autoname("SSC-.YYYY.-.####")

        if not self.name:
            self.name = self.checklist_id
