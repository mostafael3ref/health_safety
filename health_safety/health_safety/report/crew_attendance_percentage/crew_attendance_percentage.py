import frappe


def execute(filters=None):
    if filters is None:
        filters = {}

    columns = [
        {
            "label": "Date",
            "fieldname": "date",
            "fieldtype": "Date",
            "width": 120,
        },
        {
            "label": "Supervisor",
            "fieldname": "supervisor",
            "fieldtype": "Data",
            "width": 180,
        },
        {
            "label": "Planned Crew",
            "fieldname": "planned_crew",
            "fieldtype": "Int",
            "width": 130,
        },
        {
            "label": "Crew Attending",
            "fieldname": "crew_attending",
            "fieldtype": "Int",
            "width": 130,
        },
        {
            "label": "Attendance %",
            "fieldname": "attendance_percentage",
            "fieldtype": "Percent",
            "width": 130,
        },
    ]

    conditions = "1=1"
    query_filters = {}

    if filters.get("from_date"):
        conditions += " and date >= %(from_date)s"
        query_filters["from_date"] = filters["from_date"]

    if filters.get("to_date"):
        conditions += " and date <= %(to_date)s"
        query_filters["to_date"] = filters["to_date"]

    # ممكن نفلتر على Supervisor
    if filters.get("supervisor"):
        conditions += " and supervisor = %(supervisor)s"
        query_filters["supervisor"] = filters["supervisor"]

    data = frappe.db.sql(
        f"""
        SELECT
            date,
            supervisor,
            SUM(planned_crew) AS planned_crew,
            SUM(crew_attending) AS crew_attending,
            CASE
                WHEN SUM(planned_crew) > 0
                    THEN (SUM(crew_attending) / SUM(planned_crew)) * 100
                ELSE 0
            END AS attendance_percentage
        FROM `tabHSE Attendance`
        WHERE {conditions}
        GROUP BY date, supervisor
        ORDER BY date DESC
        """,
        query_filters,
        as_dict=True,
    )

    return columns, data
