from setuptools import setup, find_packages

setup(
    name="montiro",
    version="0.1.0",
    description="Montiro - File Integrity Monitoring Tool",
    author="Qawam Musiliu",
    author_email="",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'montiro=montiro.montiro:main',
        ],
    },
)