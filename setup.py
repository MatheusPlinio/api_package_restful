from setuptools import setup, find_packages

setup(
    name='restaPy',
    version='0.0.1',
    description='Pacote para implementação de sistema de autenticação de desenvolvimento de outras aplicações web com oauth2 ou jwt',
    author='Matheus Plinio Batista, Ou MatthewNoctis',
    author_email="mplinio13@gmail.com",
    url='https://github.com/MatheusPlinio/api_package_restful',
    packages=find_packages(),
    install_requires=[
        'django',
        'oauth2',
        'jwt'
    ],
    entry_point={
        'console_scripts': [
            'restaPy'
        ]
    },
)