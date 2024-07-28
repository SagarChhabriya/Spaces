from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements = []
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]

    return requirements

setup(
    name='genpixel',
    version='0.0.4',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),  # Corrected argument
    author='okela',
    long_description="This is a module for hello application. (sample for testing)"
)
