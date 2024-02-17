from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='subhan',
    author_email='subhan@ineuron.ai',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)