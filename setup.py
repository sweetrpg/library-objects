from setuptools import setup

# __version__ = "0.0.3"

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="sweetrpg-library-model",
    install_requires=[
        "Flask>=2.0",
        "mongoengine",
        "sweetrpg-db",
        "sweetrpg-model-core",
    ],
)
