from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="sweetrpg-library-model",
    install_requires=[
        "Flask>=2.0",
        "marshmallow==3.13.0",
        "PyMongo[srv,tls]==3.12.0",
        "sweetrpg-db @ git+https://github.com/sweetrpg/db.git@develop",
    ],
    extras_require={},
)
