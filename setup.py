from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="health_safety",
    version="0.0.1",
    description="Proprietary ERPNext module for Health, Safety, and Environment management.",
    author="Mostafa EL-Areef",
    author_email="info@el3ref.com",
    license="Proprietary",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[],
    long_description=long_description,
    long_description_content_type="text/markdown"
)
