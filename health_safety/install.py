import frappe


def create_equipment_print_format():
    """Create standard print format for Equipment if it doesn't exist."""
    print_format_name = "Equipment Standard"

    if frappe.db.exists("Print Format", print_format_name):
        return

    template_path = frappe.get_app_path(
        "health_safety", "health_safety", "print_templates", "equipment.html"
    )

    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()

    pf = frappe.get_doc({
        "doctype": "Print Format",
        "name": print_format_name,
        "doc_type": "Equipment",
        "module": "health_safety",   # لو اسم الموديول مختلف عدّله
        "print_format_type": "Jinja",
        "custom_format": 1,
        "html": html,
        "disabled": 0,
        "standard": "Yes",
    })

    pf.insert(ignore_if_duplicate=True, ignore_permissions=True)


def create_equipment_list_report_print_format():
    """Create print format for Equipment List report if it doesn't exist."""
    print_format_name = "Equipment List Standard"

    if frappe.db.exists("Print Format", print_format_name):
        return

    html = """
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

    pf = frappe.get_doc({
        "doctype": "Print Format",
        "name": print_format_name,
        "print_format_for": "Report",
        "report": "Equipment List",   # لازم يطابق اسم التقرير بالظبط
        "module": "health_safety",
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
    create_equipment_list_report_print_format()
