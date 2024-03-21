from setuptools import find_packages, setup

setup(
    name="mkdocs-required-tags-plugin",
    packages=find_packages(),
    entry_points={
        "mkdocs.plugins": [
            "required-tags = src.plugin:RequiredTagsPlugin"
        ]
    }
)