import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname


class MachineryandEquipmentChecklist(Document):
    def before_insert(self):
        # Generate unique ID if empty
        if not self.checklist_id:
            self.checklist_id = make_autoname("MEC-.YYYY.-.####")

        # Use checklist_id as the document name
        if not self.name:
            self.name = self.checklist_id
