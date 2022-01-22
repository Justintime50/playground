import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

DEV_REQUIREMENTS = [
    "flake8",
]

setuptools.setup(
    name="wordle",
    version="0.1.0",
    description="Solve Wordle with probability",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/Justintime50/wordle",
    author="Justintime50",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require={
        "dev": DEV_REQUIREMENTS,
    },
    python_requires=">=3.7",
)
