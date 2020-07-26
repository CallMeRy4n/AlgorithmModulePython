import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="Algorithm-Ry4n-module",
    version="0.0.1",
    author="Ry4n",
    author_email="minhquan99kk@gmail.com",
    description="Just a module contain many algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CallMeRy4n/AlgirthmRy4nModules",
    packages=[
        "src/algorithm"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)