import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

DEV_REQUIREMENTS = [
    'flake8',
]

setuptools.setup(
    name='sms-to-list',
    version='0.3.0',
    description='Send an SMS to individual numbers from a CSV on macOS.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/Justintime50/sms-to-list',
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
