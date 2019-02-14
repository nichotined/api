import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="api-nichotined",
    version="0.9.3",
    author="Nicholas Frederick",
    author_email="nicholas.frederich.lagaunne@gmail.com",
    description="API package for testing purpose",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nichotined/api",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
        'pytest',
        'redis',
        'curlify'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
