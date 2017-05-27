from setuptools import setup

setup (name = "pychain",
       version = "0.1",
       description = "simple blockchain implementation",
       url = "http://github.com/anax32/pychain",
       author = "anax32",
       author_email = "anax@hotmail.co.uk",
       license = "MIT",
       packages = ["pychain"],
       install_requires = [
         "time",
         "hashlib"
       ],
       zip_safe = True)
