from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    "aiohttp==3.5.4",
    "async-timeout==3.0.1",
    "attrs==19.3.0",
    "chardet==3.0.4",
    "idna==2.8",
    "multidict==4.6.1",
    "yarl==1.4.2",
]

setup(
    name='pyprika-client',
    version='0.1.0',
    description="AsyncIO Library for Communicating with Paprika backend servers.",
    long_description=readme,
    long_description_content_type="text/markdown; charset=UTF-8",
    author="Teagan Glenn",
    author_email='that@teagantotally.rocks',
    url='https://github.com/constructorfleet/pyprika',
    packages=find_packages(),
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
