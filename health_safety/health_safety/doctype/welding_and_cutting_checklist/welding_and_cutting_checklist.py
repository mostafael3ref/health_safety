import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname


class WeldingAndCuttingChecklist(Document):
    def before_insert(self):
        if not self.checklist_id:
            self.checklist_id = make_autoname("WCC-.YYYY.-.####")

        self.name = self.checklist_id
