from frappe import _

def get_data():
    return [{
        "module_name": "health_safety",   # لازم يطابق modules.txt
        "category": "Modules",
        "label": _("Health & Safety"),    # ليبل العرض للمستخدم.. خليه زي ما تحب
        "color": "orange",
        "icon": "octicon octicon-shield",
        "type": "module",
        "hidden": 0,
    }]
