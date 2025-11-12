# -*- coding: utf-8 -*-
from . import __version__ as app_version

app_name = "health_safety"
app_title = "Health & Safety"
app_publisher = "Mostafa EL-Areef"
app_description = "HSE module for ERPNext"
app_email = "info@el3ref.com"
app_license = "Proprietary"

# واجهة
app_logo_url = "/assets/health_safety/logo.svg"  # لو ما عندك لوجو، اشطب السطر

# ضمّن الأصول بعد البناء (esbuild يقرأ build.json ويولّد bundles تحت assets/)
app_include_js = ["assets/health_safety/js/health_safety.bundle.js"]
app_include_css = ["assets/health_safety/css/health_safety.bundle.css"]

# (اختياري) Fixtures لاحقًا
# fixtures = []
