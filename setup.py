from setuptools import setup

##with open("README.md", "r", encoding="utf-8") as f:
##    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Movie-Recommendation-System-Using-Machine-Learning"
AUTHOR_USER_NAME = "Rahul"
SRC_REPO = "SRC"
LIST_OF_REQUIREMENTS = ['streamlit']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small version of Movie Recommendation System",
    long_description="A Movie Recommendation System project",
    long_description_content_type="text/markdown",
    url=f"",
    author_email="rahulbkumar117@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)