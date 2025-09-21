import setuptools

with open("README.md" , "r" , encoding="utf-8") as f:
    long_discreption = f.read()

__version__ = "0.0.0"

REPO_NAME = "End-2-End-DL-Chicken-dieseas-classification-MLOps-CI-CD-AWS-Docker-"
AUTHOR_USER_NAME = "Deepak-Byte"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "deepakkpasi@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for cnn app",
    long_description=long_discreption,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)