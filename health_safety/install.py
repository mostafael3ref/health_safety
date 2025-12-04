import frappe

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
        # لو موجود نعمل update
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
        # لو مش موجود نعمله insert
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
    """Create EN + AR print formats for Equipment DocType."""
    # الإنجليزي
    _make_equipment_pf(EQUIPMENT_PF_EN, "en")
    # العربي
    _make_equipment_pf(EQUIPMENT_PF_AR, "ar")


# ====================================
# 2) Print Formats لتقرير Equipment List
# ====================================

def _get_equipment_list_html():
    """Base HTML for Equipment List report print format."""
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
    """Create or update Print Format for Equipment List report."""
    html = _get_equipment_list_html()

    if frappe.db.exists("Print Format", name):
        pf = frappe.get_doc("Print Format", name)
        pf.update({
            "print_format_for": "Report",
            "report": "Equipment List",  # لازم يطابق اسم التقرير
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
    """Create EN + AR print formats for Equipment List report."""
    _make_equipment_list_pf(EQUIPMENT_LIST_PF_EN, "en")
    _make_equipment_list_pf(EQUIPMENT_LIST_PF_AR, "ar")


# ====================================
# 3) Print Format للـ Cranes Checklist
# ====================================

def create_cranes_checklist_print_format():
    """Create or update Print Format for Cranes Checklist DocType."""
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
            # لو حابة تطبعي عربي افتراضيًا خليه "ar"
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
# 4) Hook بعد التثبيت
# ====================================

def after_install():
    """Hook called by Frappe after installing the app."""
    create_equipment_print_formats()
    create_equipment_list_report_print_formats()
    create_cranes_checklist_print_format()
