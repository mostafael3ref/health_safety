import frappe
from frappe.utils import getdate


def execute(filters=None):
    if filters is None:
        filters = {}

    columns = [
        {
            "label": "Year",
            "fieldname": "year",
            "fieldtype": "Int",
            "width": 80,
        },
        {
            "label": "Month",
            "fieldname": "month",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": "Toolbox Talks Count",
            "fieldname": "tbt_count",
            "fieldtype": "Int",
            "width": 180,
        },
    ]

    # Filters اختيارية: from_date, to_date
    conditions = "1=1"
    query_filters = {}

    if filters.get("from_date"):
        conditions += " and date >= %(from_date)s"
        query_filters["from_date"] = filters["from_date"]

    if filters.get("to_date"):
        conditions += " and date <= %(to_date)s"
        query_filters["to_date"] = filters["to_date"]

    data = frappe.db.sql(
        f"""
        SELECT
            YEAR(date) AS year,
            MONTH(date) AS month_number,
            DATE_FORMAT(date, '%%M') AS month,
            COUNT(*) AS tbt_count
        FROM `tabToolbox Talk`
        WHERE {conditions}
        GROUP BY YEAR(date), MONTH(date)
        ORDER BY YEAR(date) DESC, MONTH(date) DESC
        """,
        query_filters,
        as_dict=True,
    )

    return columns, data
