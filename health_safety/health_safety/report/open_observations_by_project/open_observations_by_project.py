import frappe


def execute(filters=None):
    if filters is None:
        filters = {}

    columns = [
        {
            "label": "Project",
            "fieldname": "project_name",
            "fieldtype": "Link",
            "options": "Project",
            "width": 200,
        },
        {
            "label": "Open Observations",
            "fieldname": "open_count",
            "fieldtype": "Int",
            "width": 150,
        },
    ]

    conditions = "status = 'Open'"
    query_filters = {}

    if filters.get("project_name"):
        conditions += " and project_name = %(project_name)s"
        query_filters["project_name"] = filters["project_name"]

    data = frappe.db.sql(
        f"""
        SELECT
            project_name,
            COUNT(*) AS open_count
        FROM `tabObservation Record`
        WHERE {conditions}
        GROUP BY project_name
        ORDER BY open_count DESC
        """,
        query_filters,
        as_dict=True,
    )

    return columns, data
