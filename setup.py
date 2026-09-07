from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="IP-Spyder",
    version="1.0.0",
    Devloper="BLACK HAMO",
    description="An Excellent OSINT tool to get information of any IP address",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Black-HamoX/IP-Spyder",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        'requests>=2.28.0',
        'colorama>=0.4.6',
        'pyfiglet>=0.8.post1',
        'termcolor>=2.1.0',
    ],
    entry_points={
        'console_scripts': [
            'ipspyder=main:main',
        ],
    },
)