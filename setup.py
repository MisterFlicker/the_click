import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="The_click",
    version="1.0",
    author="Mister_Flicker",
    author_email="lutecequantum@gmail.com",
    description="Clicker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
)