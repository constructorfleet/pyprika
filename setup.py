from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    "aiohttp==3.6.2",
    "astroid==2.3.3",
    "async-timeout==3.0.1",
    "attrs==19.3.0",
    "cffi==1.13.2",
    "chardet==3.0.4",
    "cryptography==2.8",
    "future==0.18.2",
    "idna==2.8",
    "isort==4.3.21",
    "lazy-object-proxy==1.4.3",
    "mccabe==0.6.1",
    "multidict==4.7.4",
    "pycparser==2.19",
    "pylint==2.4.4",
    "pyparsing==2.3.1",
    "pyserial==3.4",
    "six==1.13.0",
    "typed-ast==1.4.1",
    "wrapt==1.11.2",
    "yarl==1.4.2"

]

setup(
    name='pyprika',
    version='0.1.0',
    description="AsyncIO Library for Communicating with Paprika backend servers.",
    long_description=readme,
    author="Teagan Glenn",
    author_email='that@teagantotally.rocks',
    url='https://github.com/constructorfleet/pyprika',
    packages=[
        'pyprika',
    ],
    package_dir={'pyprika':
                 'pyprika'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='Paprika, Cooking, Recipes',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)