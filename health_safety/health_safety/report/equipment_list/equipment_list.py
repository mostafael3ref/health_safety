# health_safety/health_safety/report/equipment_list/equipment_list.py

import frappe
from frappe import _


def execute(filters=None):
    columns = [
        {
            "label": _("ID"),
            "fieldname": "name",
            "fieldtype": "Link",
            "options": "Equipment",
            "width": 120,
        },
        {
            "label": _("Stomach Type"),
            "fieldname": "stomach_type",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": _("Plate Number"),
            "fieldname": "plate_number",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": _("Cameras"),
            "fieldname": "cameras",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": _("Color"),
            "fieldname": "color",
            "fieldtype": "Data",
            "width": 100,
        },
        {
            "label": _("TUV Expiry Date"),
            "fieldname": "tuv_expiry_date",
            "fieldtype": "Date",
            "width": 120,
        },
        {
            "label": _("Chassis Number"),
            "fieldname": "chassis_number",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": _("Serial Number"),
            "fieldname": "serial_number",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": _("Insurance Expiry Date"),
            "fieldname": "insurance_expiry_date",
            "fieldtype": "Date",
            "width": 130,
        },
        {
            "label": _("Owner"),
            "fieldname": "owner_name",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": _("Model"),
            "fieldname": "model_year",
            "fieldtype": "Int",
            "width": 80,
        },
        {
            "label": _("Registration Type"),
            "fieldname": "registration_type",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": _("Size"),
            "fieldname": "size",
            "fieldtype": "Data",
            "width": 80,
        },
    ]

    data = frappe.get_all(
        "Equipment",
        fields=[c["fieldname"] for c in columns],
        order_by="creation desc",
    )

    # ✅ ترجم قيم حقل Cameras (There is a camera / No camera)
    for row in data:
        if row.get("cameras"):
            row["cameras"] = _(row["cameras"])

    return columns, data
