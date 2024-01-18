from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup

VERSION = "1.0"
README_PATH = "README.md"


long_description = ""
with open(README_PATH, "r", encoding="utf-8") as file:
    long_description = file.read()


setup(
    name="permaDB",
    version=VERSION,
    license="MIT License",
    description="PermaDB is a database management library, uses better-sqlite3 under the hood.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="LegendMan46",
    author_email="eposta@gmail.com",
    url="https://github.com/LegendMan46/permaDB",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        # uncomment if you test on these interpreters:
        # "Programming Language :: Python :: Implementation :: IronPython",
        # "Programming Language :: Python :: Implementation :: Jython",
        # "Programming Language :: Python :: Implementation :: Stackless",
        "Topic :: Utilities",
    ],
    project_urls={
        "JS Module": "https://github.com/Rednexie/perma.db",
        "Python Module": "https://github.com/LegendMan46/permaDB/README.md",
    },
    keywords=[],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    install_requires=["requests,json,time,threading,subprocess,sqlite3,os"], # Bağlı olduğu paketler, örn: requests
    extras_require={
    },
    setup_requires=[
        "pytest-runner",
    ],
    entry_points={
        # Komut isteminden çalıştırma
        # örndeğin: ypackage
        # Kullanım: "ypacakge = ypackage.ypackage:main
        "console_scripts": [
        ]
    },
    # tests_require=test_requirements,
)
