from setuptools import find_packages, setup

setup(
    name="mkdocs-required-tags-plugin",
    packages=find_packages(),
    version="0.0.2",
    keywords="mkdocs plugin tags required",
    url="https://github.com/unmc-vcr/mkdocs-required-tags-plugin",
    author="James Geiger",
    author_email="james.geiger@unmc.edu",
    license="MIT",
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "mkdocs.plugins": [
            "required-tags = src.plugin:RequiredTagsPlugin"
        ]
    }
)