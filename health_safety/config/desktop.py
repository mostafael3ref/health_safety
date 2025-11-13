# apps/health_safety/health_safety/config/desktop.py
# -*- coding: utf-8 -*-
from frappe import _

def get_data():
    return [{
        "module_name": "Health and Safety",   # <-- مهم: يطابق modules.txt
        "category": "Modules",
        "label": _("Health & Safety"),        # العرض للمستخدم، عادي فيه &
        "color": "orange",
        "icon": "octicon octicon-shield",
        "type": "module",
        "hidden": 0,
    }]
