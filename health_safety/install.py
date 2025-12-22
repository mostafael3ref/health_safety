import frappe
import json
# ===========================
# أسماء تنسيقات الطباعة
# ===========================

# Equipment
EQUIPMENT_PF_EN = "Equipment Standard"
EQUIPMENT_PF_AR = "Equipment Standard AR"

EQUIPMENT_LIST_PF_EN = "Equipment List Standard"
EQUIPMENT_LIST_PF_AR = "Equipment List AR"

# Cranes Checklist
CRANES_CHECKLIST_PF = "Cranes Checklist Standard"

# Housekeeping Checklist
HOUSEKEEPING_CHECKLIST_PF = "Housekeeping Checklist Standard"

# Ladders Checklist
LADDERS_CHECKLIST_PF = "Ladders Checklist Standard"

# Scaffolding Safety Checklist
SCAFFOLDING_SAFETY_CHECKLIST_PF = "Scaffolding Safety Checklist Standard"

# ===== NEW (3 DocTypes) =====
# Elevator Safety checklist
ELEVATOR_SAFETY_CHECKLIST_PF = "Elevator Safety Checklist Standard"

# Standby Generator Checklist
STANDBY_GENERATOR_CHECKLIST_PF = "Standby Generator Checklist Standard"

# ===== NEW (Machinery & Equipment) =====
MACHINERY_EQUIPMENT_CHECKLIST_PF = "Machinery and Equipment Checklist Standard"

# Letter Head
WATER_LETTER_HEAD_NAME = "Water Company Letter Head"


# ====================================
# 1) Print Formats للـ Equipment DocType
# ====================================

def _make_equipment_pf(name: str, default_lang: str):
    """Create or update Equipment Print Format with given name & default language."""
    template_path = frappe.get_app_path(
        "health_safety", "health_safety", "print_templates", "equipment.html"
    )

    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()

    if frappe.db.exists("Print Format", name):
        pf = frappe.get_doc("Print Format", name)
        pf.update({
            "doc_type": "Equipment",
            "module": "health_safety",
            "print_format_type": "Jinja",
            "custom_format": 1,
            "html": html,
            "disabled": 0,
            "standard": "Yes",
            "default_print_language": default_lang,
        })
        pf.save(ignore_permissions=True)
    else:
        pf = frappe.get_doc({
            "doctype": "Print Format",
            "name": name,
            "doc_type": "Equipment",
            "module": "health_safety",
            "print_format_type": "Jinja",
            "custom_format": 1,
            "html": html,
            "disabled": 0,
            "standard": "Yes",
            "default_print_language": default_lang,
        })
        pf.insert(ignore_if_duplicate=True, ignore_permissions=True)


def create_equipment_print_formats():
    _make_equipment_pf(EQUIPMENT_PF_EN, "en")
    _make_equipment_pf(EQUIPMENT_PF_AR, "ar")


# ====================================
# 2) Print Formats لتقرير Equipment List
# ====================================

def _get_equipment_list_html():
    return """
<style>
  .equipment-title {
    text-align: center;
    color: #e60000;
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 15px;
  }
  .equipment-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 5px;
    font-size: 11px;
  }
  .equipment-table th,
  .equipment-table td {
    border: 1px solid #000;
    padding: 6px 8px;
  }
  .equipment-table th {
    background: #f5f5f5;
    font-weight: bold;
  }
</style>

<div class="equipment-title">
  {{ _("Equipment List") }}
</div>

<table class="equipment-table">
  <thead>
    <tr>
      {% for col in columns %}
        <th>{{ _(col.label or col.fieldname or "") }}</th>
      {% endfor %}
    </tr>
  </thead>
  <tbody>
    {% for row in data %}
      <tr>
        {% for col in columns %}
          {% set fieldname = col.fieldname %}
          <td>{{ row.get(fieldname) if fieldname else "" }}</td>
        {% endfor %}
      </tr>
    {% endfor %}
  </tbody>
</table>
    """


def _make_equipment_list_pf(name: str, default_lang: str):
    html = _get_equipment_list_html()

    if frappe.db.exists("Print Format", name):
        pf = frappe.get_doc("Print Format", name)
        pf.update({
            "print_format_for": "Report",
            "report": "Equipment List",
            "module": "health_safety",
            "print_format_type": "Jinja",
            "custom_format": 1,
            "html": html,
            "disabled": 0,
            "standard": "Yes",
            "default_print_language": default_lang,
        })
        pf.save(ignore_permissions=True)
    else:
        pf = frappe.get_doc({
            "doctype": "Print Format",
            "name": name,
            "print_format_for": "Report",
            "report": "Equipment List",
            "module": "health_safety",
            "print_format_type": "Jinja",
            "custom_format": 1,
            "html": html,
            "disabled": 0,
            "standard": "Yes",
            "default_print_language": default_lang,
        })
        pf.insert(ignore_if_duplicate=True, ignore_permissions=True)


def create_equipment_list_report_print_formats():
    _make_equipment_list_pf(EQUIPMENT_LIST_PF_EN, "en")
    _make_equipment_list_pf(EQUIPMENT_LIST_PF_AR, "ar")


# ====================================
# 3) Cranes Checklist Print Format
# ====================================

def create_cranes_checklist_print_format():
    template_path = frappe.get_app_path(
        "health_safety", "health_safety", "print_templates", "cranes_checklist.html"
    )

    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()

    if frappe.db.exists("Print Format", CRANES_CHECKLIST_PF):
        pf = frappe.get_doc("Print Format", CRANES_CHECKLIST_PF)
        pf.update({
            "doc_type": "Cranes Checklist",
            "module": "health_safety",
            "print_format_type": "Jinja",
            "custom_format": 1,
            "html": html,
            "disabled": 0,
            "standard": "Yes",
            "default_print_language": "ar",
        })
        pf.save(ignore_permissions=True)
    else:
        pf = frappe.get_doc({
            "doctype": "Print Format",
            "name": CRANES_CHECKLIST_PF,
            "doc_type": "Cranes Checklist",
            "module": "health_safety",
            "print_format_type": "Jinja",
            "custom_format": 1,
            "html": html,
            "disabled": 0,
            "standard": "Yes",
            "default_print_language": "ar",
        })
        pf.insert(ignore_if_duplicate=True, ignore_permissions=True)


# ====================================
# 3.1) Housekeeping Checklist Print Format
# ====================================

def create_housekeeping_checklist_print_format():
    template_path = frappe.get_app_path(
        "health_safety", "health_safety", "print_templates", "housekeeping_checklist.html"
    )

    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()

    if frappe.db.exists("Print Format", HOUSEKEEPING_CHECKLIST_PF):
        pf = frappe.get_doc("Print Format", HOUSEKEEPING_CHECKLIST_PF)
        pf.update({
            "doc_type": "Housekeeping Checklist",
            "module": "health_safety",
            "print_format_type": "Jinja",
            "custom_format": 1,
            "html": html,
            "disabled": 0,
            "standard": "Yes",
            "default_print_language": "ar",
        })
        pf.save(ignore_permissions=True)
    else:
        pf = frappe.get_doc({
            "doctype": "Print Format",
            "name": HOUSEKEEPING_CHECKLIST_PF,
            "doc_type": "Housekeeping Checklist",
            "module": "health_safety",
            "print_format_type": "Jinja",
            "custom_format": 1,
            "html": html,
            "disabled": 0,
            "standard": "Yes",
            "default_print_language": "ar",
        })
        pf.insert(ignore_if_duplicate=True, ignore_permissions=True)


# ====================================
# 3.2) Ladders Checklist Print Format
# ====================================

def create_ladders_checklist_print_format():
    template_path = frappe.get_app_path(
        "health_safety", "health_safety", "print_templates", "ladders_checklist.html"
    )

    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()

    if frappe.db.exists("Print Format", LADDERS_CHECKLIST_PF):
        pf = frappe.get_doc("Print Format", LADDERS_CHECKLIST_PF)
        pf.update({
            "doc_type": "Ladders Checklist",
            "module": "health_safety",
            "print_format_type": "Jinja",
            "custom_format": 1,
            "html": html,
            "disabled": 0,
            "standard": "Yes",
            "default_print_language": "ar",
        })
        pf.save(ignore_permissions=True)
    else:
        pf = frappe.get_doc({
            "doctype": "Print Format",
            "name": LADDERS_CHECKLIST_PF,
            "doc_type": "Ladders Checklist",
            "module": "health_safety",
            "print_format_type": "Jinja",
            "custom_format": 1,
            "html": html,
            "disabled": 0,
            "standard": "Yes",
            "default_print_language": "ar",
        })
        pf.insert(ignore_if_duplicate=True, ignore_permissions=True)


# ====================================
# 3.3) Scaffolding Safety Checklist Print Format
# ====================================

def create_scaffolding_safety_checklist_print_format():
    template_path = frappe.get_app_path(
        "health_safety", "health_safety", "print_templates", "scaffolding_safety_checklist.html"
    )

    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()

    if frappe.db.exists("Print Format", SCAFFOLDING_SAFETY_CHECKLIST_PF):
        pf = frappe.get_doc("Print Format", SCAFFOLDING_SAFETY_CHECKLIST_PF)
        pf.update({
            "doc_type": "Scaffolding Safety checklist",
            "module": "health_safety",
            "print_format_type": "Jinja",
            "custom_format": 1,
            "html": html,
            "disabled": 0,
            "standard": "Yes",
            "default_print_language": "ar",
        })
        pf.save(ignore_permissions=True)
    else:
        pf = frappe.get_doc({
            "doctype": "Print Format",
            "name": SCAFFOLDING_SAFETY_CHECKLIST_PF,
            "doc_type": "Scaffolding Safety checklist",
            "module": "health_safety",
            "print_format_type": "Jinja",
            "custom_format": 1,
            "html": html,
            "disabled": 0,
            "standard": "Yes",
            "default_print_language": "ar",
        })
        pf.insert(ignore_if_duplicate=True, ignore_permissions=True)


# ====================================
# 3.4) Elevator Safety Checklist Print Format
# ====================================

def create_elevator_safety_checklist_print_format():
    template_path = frappe.get_app_path(
        "health_safety", "health_safety", "print_templates", "elevator_safety_checklist.html"
    )

    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()

    if frappe.db.exists("Print Format", ELEVATOR_SAFETY_CHECKLIST_PF):
        pf = frappe.get_doc("Print Format", ELEVATOR_SAFETY_CHECKLIST_PF)
        pf.update({
            "doc_type": "Elevator Safety checklist",
            "module": "health_safety",
            "print_format_type": "Jinja",
            "custom_format": 1,
            "html": html,
            "disabled": 0,
            "standard": "Yes",
            "default_print_language": "ar",
        })
        pf.save(ignore_permissions=True)
    else:
        pf = frappe.get_doc({
            "doctype": "Print Format",
            "name": ELEVATOR_SAFETY_CHECKLIST_PF,
            "doc_type": "Elevator Safety checklist",
            "module": "health_safety",
            "print_format_type": "Jinja",
            "custom_format": 1,
            "html": html,
            "disabled": 0,
            "standard": "Yes",
            "default_print_language": "ar",
        })
        pf.insert(ignore_if_duplicate=True, ignore_permissions=True)


# ====================================
# 3.5) Standby Generator Checklist Print Format
# ====================================

def create_standby_generator_checklist_print_format():
    template_path = frappe.get_app_path(
        "health_safety", "health_safety", "print_templates", "standby_generator_checklist.html"
    )

    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()

    if frappe.db.exists("Print Format", STANDBY_GENERATOR_CHECKLIST_PF):
        pf = frappe.get_doc("Print Format", STANDBY_GENERATOR_CHECKLIST_PF)
        pf.update({
            "doc_type": "Standby Generator Checklist",
            "module": "health_safety",
            "print_format_type": "Jinja",
            "custom_format": 1,
            "html": html,
            "disabled": 0,
            "standard": "Yes",
            "default_print_language": "ar",
        })
        pf.save(ignore_permissions=True)
    else:
        pf = frappe.get_doc({
            "doctype": "Print Format",
            "name": STANDBY_GENERATOR_CHECKLIST_PF,
            "doc_type": "Standby Generator Checklist",
            "module": "health_safety",
            "print_format_type": "Jinja",
            "custom_format": 1,
            "html": html,
            "disabled": 0,
            "standard": "Yes",
            "default_print_language": "ar",
        })
        pf.insert(ignore_if_duplicate=True, ignore_permissions=True)



# ====================================
# 3.7) Machinery and Equipment Checklist Print Format (NEW)
# ====================================

def create_machinery_equipment_checklist_print_format():
    template_path = frappe.get_app_path(
        "health_safety",
        "health_safety",
        "print_templates",
        "machinery_and_equipment_checklist.html",
    )

    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()

    if frappe.db.exists("Print Format", MACHINERY_EQUIPMENT_CHECKLIST_PF):
        pf = frappe.get_doc("Print Format", MACHINERY_EQUIPMENT_CHECKLIST_PF)
        pf.update({
            "doc_type": "Machinery and Equipment Checklist",
            "module": "health_safety",
            "print_format_type": "Jinja",
            "custom_format": 1,
            "html": html,
            "disabled": 0,
            "standard": "Yes",
            "default_print_language": "ar",
        })
        pf.save(ignore_permissions=True)
    else:
        pf = frappe.get_doc({
            "doctype": "Print Format",
            "name": MACHINERY_EQUIPMENT_CHECKLIST_PF,
            "doc_type": "Machinery and Equipment Checklist",
            "module": "health_safety",
            "print_format_type": "Jinja",
            "custom_format": 1,
            "html": html,
            "disabled": 0,
            "standard": "Yes",
            "default_print_language": "ar",
        })
        pf.insert(ignore_if_duplicate=True, ignore_permissions=True)


# ====================================
# 4) Letter Head
# ====================================

def create_water_letter_head():
    html = """
    <div style="text-align:right; margin:10px 0;">
      <img src="/assets/health_safety/img/water_logo.webp" style="height:90px;">
    </div>
    """

    if frappe.db.exists("Letter Head", WATER_LETTER_HEAD_NAME):
        lh = frappe.get_doc("Letter Head", WATER_LETTER_HEAD_NAME)
        lh.update({
            "is_default": 1,
            "disabled": 0,
            "source": "HTML",
            "content": html,
        })
        lh.save(ignore_permissions=True)
    else:
        lh = frappe.get_doc({
            "doctype": "Letter Head",
            "letter_head_name": WATER_LETTER_HEAD_NAME,
            "is_default": 1,
            "disabled": 0,
            "source": "HTML",
            "content": html,
        })
        lh.insert(ignore_if_duplicate=True, ignore_permissions=True)


# ====================================
# 4.1) Module Def + Workspace (NEW)
# ====================================

def ensure_module_def():
    if not frappe.db.exists("Module Def", "Health & Safety"):
        frappe.get_doc({
            "doctype": "Module Def",
            "module_name": "Health & Safety",
            "app_name": "health_safety"
        }).insert(ignore_permissions=True)


def ensure_workspace():
    content = [
        {"type": "header", "data": {"text": "Health & Safety"}},
        {"type": "section", "data": {"label": "PPE models"}},
        {
            "type": "card",
            "data": {
                "card_name": "Checklists",
                "items": [
                    {"type": "doctype", "name": "Cranes Checklist"},
                    {"type": "doctype", "name": "Elevator Safety Checklist"},
                    {"type": "doctype", "name": "Housekeeping Checklist"},
                    {"type": "doctype", "name": "Ladders Checklist"},
                    {"type": "doctype", "name": "Machinery and Equipment Checklist"},
                    {"type": "doctype", "name": "Scaffolding Safety Checklist"},
                    {"type": "doctype", "name": "Standby Generator Checklist"},
                ],
            },
        },
    ]

    doc = {
        "doctype": "Workspace",
        "name": "Health & Safety",
        "title": "Health & Safety",
        "module": "health_safety",
        "icon": "shield",
        "public": 1,
        "content": json.dumps(content),
        "roles": [{"role": "System Manager"}],
    }

    if frappe.db.exists("Workspace", "Health & Safety"):
        frappe.get_doc("Workspace", "Health & Safety").update(doc).save(ignore_permissions=True)
    else:
        frappe.get_doc(doc).insert(ignore_permissions=True)


# ====================================
# 5) Hook after install
# ====================================

def after_install():
    create_equipment_print_formats()
    create_equipment_list_report_print_formats()
    create_cranes_checklist_print_format()
    create_housekeeping_checklist_print_format()
    create_ladders_checklist_print_format()
    create_scaffolding_safety_checklist_print_format()

    # NEW (3 DocTypes)
    create_elevator_safety_checklist_print_format()
    create_standby_generator_checklist_print_format()

    # NEW (Machinery & Equipment)
    create_machinery_equipment_checklist_print_format()

    create_water_letter_head()

    # NEW (Module Def + Workspace)
    ensure_module_def()
    ensure_workspace()


def after_migrate():
    # نخلي Workspace + Module Def يرجعوا تلقائي بعد أي migrate
    ensure_module_def()
    ensure_workspace()
