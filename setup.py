from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    page_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='image_processing_phds',
    version='0.0.1',
    author='Paulo Sanches',
    author_email='paulohdsanches@gmail.com',
    description='Pacote criado no curso DIO',
    long_description=page_description,
    long_description_content_type='text/markdown',
    url='https://github.com/paulohdsanches/image-processing-package',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',    
)