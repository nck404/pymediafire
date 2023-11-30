from setuptools import setup, find_packages

setup(
    name="mediafire-dl-ne",
    version="0.1.0",
    description="Simple command-line script to download files from mediafire based on gdown",
    url="pymediafire",
    author="nck",
    author_email="khoavencyti@mail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="audo ai",
    py_modules=['mediafire_dl'],
    install_requires=[
        "requests",
        "six",
        "tqdm",
    ],
    entry_points={
        "console_scripts": ["mediafire-dl=mediafire_dl:main"],
    },
)
