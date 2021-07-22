from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "An infix-to-postfix expression parser for evaluating math expressions."

setup(
    name="tinypost",
    version=VERSION,
    author="Nathan Abraham",
    author_email="abnathan123@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    keywords=["python", "math", "shunting-yard",
              "parser", "expression evaluation"],
    classifiers=["Operating System :: Unix",
                 "Operating System :: MacOS :: MacOS X",
                 "Operating System :: Microsoft :: Windows",
                 ]
)
