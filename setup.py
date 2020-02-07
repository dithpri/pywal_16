"""wal - setup.py"""
import sys
import setuptools

try:
    import pywal_16
except ImportError:
    print("error: pywal_16 requires Python 3.5 or greater.")
    sys.exit(1)

LONG_DESC = open('README.md').read()
VERSION = pywal_16.__version__

setuptools.setup(
    name="pywal_16",
    version=VERSION,
    author="Dylan Araps, cheshyre, dithpri",
    # author_email="dylan.araps@gmail.com",
    description="Generate and change color-schemes on the fly",
    long_description_content_type="text/markdown",
    long_description=LONG_DESC,
    keywords="wal colorscheme terminal-emulators changing-colorschemes",
    license="MIT",
    url="https://github.com/dithpri/pywal_16",
    classifiers=[
        "Environment :: X11 Applications",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["pywal_16"],
    entry_points={"console_scripts": ["wal=pywal_16.__main__:main"]},
    python_requires=">=3.5",
    install_requires=list(open("requirements.txt")),
    test_suite="tests",
    include_package_data=True,
    zip_safe=False)
