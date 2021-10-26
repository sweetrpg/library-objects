from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="sweetrpg-library-objects",
    install_requires=[
        "Flask==2.0.2",
        "mongoengine",
        "sweetrpg-db @ git+https://github.com/sweetrpg/db.git@develop",
        "sweetrpg-model-core @ git+https://github.com/sweetrpg/model-core.git@develop",
        "marshmallow-jsonapi",
    ],
)
