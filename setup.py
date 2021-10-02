from setuptools import setup, find_packages


with open('requirements.txt') as req:
    install_packages = req.read()

setup(
    name = "Rest_API_Swagger",
    version = "0.0.1",
    description = "API de usuarios no Swagger",
    url = "https://github.com/lucasharzer/Rest_API_Swagger",
    author = "Lucas Harzer",
    author_email = "lucasmatos592@gmail.com",
    license = "BSD",
    packages = find_packages(),
    install_packages = [install_packages],
    zip_safe = False
)