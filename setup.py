from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)-> list[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements if req.strip() and not req.startswith('-')]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup( 
name="MLProject",
version='0.0.1',
author="Garima",
author_email="jaingarima1616@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)