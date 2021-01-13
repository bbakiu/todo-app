from setuptools import setup, find_packages

setup(
    name = "todobackend",
    version = "0.1.0",
    description = "Todobackend django rest services",
    packages = find_packages(),
    include_package_data = True,
    scripts = ["manage.py"],
    install_requires = [""],
    extras_require = {}

)