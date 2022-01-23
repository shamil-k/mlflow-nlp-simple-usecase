from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "dvc-nlp-simple-usecase"
AUTHOR_USER_NAME = "shamil-k"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="Asked question regarding python or not by verifying the Tag from  Stack overflow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shamil-k/dvc-nlp-simple-usecase",
    author_email="shamilvs789@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.6",
    install_requires=LIST_OF_REQUIREMENTS
)
