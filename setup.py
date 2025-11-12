from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='kavin',
    author_email='kavinkrishna.rajen@gmail.com',
    install_requires=["langchain_openai,""langchain,""streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)