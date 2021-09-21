import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

REQUIREMENTS = [
    'Flask == 2.*',
]

DEV_REQUIREMENTS = [
    'flake8',
]

setuptools.setup(
    name='webhook-server',
    version='0.1.0',
    description='Send an SMS to individual numbers from a CSV on macOS.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/Justintime50/webhook-server',
    author='Justintime50',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require={
        'dev': DEV_REQUIREMENTS,
    },
    python_requires='>=3.7',
)
