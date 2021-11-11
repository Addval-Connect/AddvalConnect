import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
with open(HERE / "README.md", encoding="utf-8") as f:
    README = f.read()

# This call to setup() does all the work
setup(
    name="addval-connect-tools",
    version="1.0.0",
    description="Herramientas para conexion a bases de datos y generación de informes para Addval Connect",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/DHerrmannP/AddvalConnect.git",
    author="Daniel Herrmann",
    author_email="dherrmann@addval.com",
    license="None",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=[  "analisis_cuentas",
                "excel_writer",
                "online_indicators",
                "read_data_base"],
    include_package_data=True,
    install_requires=["pyodbc", "pandas", "xlsxwriter"]
)