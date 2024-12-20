from setuptools import find_packages, setup

from typing import List


def get_requirements() -> List[str]:

    requrements_list: List[str] = []

    return requrements_list


setup(
    name="sensor",
    version="0.0.1",
    author="Nikhil",
    author_email="nikhillashyap07@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),  # ['pymongo==4.2.0']
)
