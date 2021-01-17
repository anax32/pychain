import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

exec(open("pychain/version.py").read())

setuptools.setup (
    name = "pychain",
    version = __version__,
    author = "anax32",
    author_email = "anax@hotmail.co.uk",
    description = "simple blockchain implementation",
    url = "http://github.com/anax32/pychain",
    packages = [
        "pychain",
        "pychain.hash",
        "pychain.block"
    ],
    classifiers=[
        "Operating System :: OS Independent"
    ],
    license = "MIT",
    zip_safe = True
)
