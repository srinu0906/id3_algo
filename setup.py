# setup.py

from setuptools import setup, find_packages

setup(
    name="id3_algo",
    version="0.1",
    packages=find_packages(),
    install_requires=[  # Any dependencies like pandas
        'pandas',
    ],
    author="Your Name",
    author_email="your-email@example.com",
    description="A simple ID3 algorithm package for decision trees.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/id3_algo",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
