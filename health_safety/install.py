import frappe


def create_equipment_print_format():
    """Create standard print format for Equipment if it doesn't exist."""
    print_format_name = "Equipment Standard"

    # لو الفورم موجود خلاص ما نعيدش إنشاؤه
    if frappe.db.exists("Print Format", print_format_name):
        return

    # نقرأ قالب الـ HTML من ملف equipment.html
    template_path = frappe.get_app_path(
        "health_safety", "health_safety", "print_templates", "equipment.html"
    )

    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()

    # IMPORTANT:
    # لو اسم الموديول في modules.txt مختلف غيّر "Health Safety" هنا
    pf = frappe.get_doc({
        "doctype": "Print Format",
        "name": print_format_name,
        "doc_type": "Equipment",
        "module": "health_safety",  # عدّلها لو المسمى مختلف عندك
        "print_format_type": "Jinja",
        "custom_format": 1,
        "html": html,
        "disabled": 0,
        "standard": "Yes",
    })

    pf.insert(ignore_if_duplicate=True, ignore_permissions=True)


def after_install():
    """Hook called by Frappe after installing the app."""
    create_equipment_print_format()
