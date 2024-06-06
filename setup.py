from setuptools import find_packages, setup #map application dir structure
from typing import List

HYPHEN_E_DOT = '-e .' #-e . is not package so it should be removed from setup

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return list of requirments
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n',"") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

setup(
    name="ml_projecgt",
    version="0.0.1",
    author="Himanshu",
    author_email="himanshu720@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)