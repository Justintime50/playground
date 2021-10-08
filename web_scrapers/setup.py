import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIREMENTS = [
    "beautifulsoup4 == 4.*",
    "requests == 2.*",
    "selenium == 3.*",
]

DEV_REQUIREMENTS = [
    "flake8",
]

setuptools.setup(
    name="web-scrapers",
    version="0.4.0",
    description="A collection of web scrapers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/justintime50/web-scraper",
    author="Justintime50",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIREMENTS,
    extras_require={
        "dev": DEV_REQUIREMENTS,
    },
    python_requires=">=3.7",
)
