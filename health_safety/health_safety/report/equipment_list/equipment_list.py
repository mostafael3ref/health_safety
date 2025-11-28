import frappe


def execute(filters=None):
    if filters is None:
        filters = {}

    columns = [
        {"fieldname": "name", "label": "ID", "fieldtype": "Data", "width": 120},
        {"fieldname": "stomach_type", "label": "Stomach Type", "fieldtype": "Data", "width": 120},
        {"fieldname": "plate_number", "label": "Plate Number", "fieldtype": "Data", "width": 120},
        {"fieldname": "cameras", "label": "Cameras", "fieldtype": "Data", "width": 110},
        {"fieldname": "color", "label": "Color", "fieldtype": "Data", "width": 90},
        {"fieldname": "tuv_expiry_date", "label": "TUV Expiry Date", "fieldtype": "Date", "width": 110},
        {"fieldname": "chassis_number", "label": "Chassis Number", "fieldtype": "Data", "width": 130},
        {"fieldname": "serial_number", "label": "Serial Number", "fieldtype": "Data", "width": 130},
        {"fieldname": "insurance_expiry_date", "label": "Insurance Expiry Date", "fieldtype": "Date", "width": 130},
        {"fieldname": "owner_name", "label": "Owner", "fieldtype": "Data", "width": 120},
        {"fieldname": "model_year", "label": "Model", "fieldtype": "Int", "width": 80},
        {"fieldname": "registration_type", "label": "Registration Type", "fieldtype": "Data", "width": 120},
        {"fieldname": "size", "label": "Size", "fieldtype": "Data", "width": 90},
    ]

    # تقدر تضيف فلاتر هنا لو حابب بعدين
    data = frappe.get_all(
        "Equipment",
        fields=[
            "name",
            "stomach_type",
            "plate_number",
            "cameras",
            "color",
            "tuv_expiry_date",
            "chassis_number",
            "serial_number",
            "insurance_expiry_date",
            "owner_name",
            "model_year",
            "registration_type",
            "size",
        ],
        order_by="creation desc",
    )

    return columns, data
