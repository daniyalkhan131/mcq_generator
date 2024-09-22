from setuptools import find_packages, setup

setup(
    name= 'mcq_generator',
    version= '0.0.1',
    author= 'Daniyal Khan',
    author_email= '-------',
    install_requires= ['openai', 'langchain', 'streamlit', 'python-dotenv', 'PyPDF2'],
    packages= find_packages()  #where ever it finds __init__ file it will consider that folder as package
    )