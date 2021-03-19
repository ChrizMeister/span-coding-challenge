import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="span-challenge-pkg-chrizmeister",
    version="1.0",
    author="Christopher Sommerville",
    author_email="cssommer@uci.edu",
    description="Span Internship Coding Challenge",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChrizMeister/span-coding-challenge",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)