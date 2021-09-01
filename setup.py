import setuptools
import src


setuptools.setup(
    name="github-actions-play", 
    version=src.__version__,
    author="Taylor Mitchell",
    author_email="taylor.j.mitchell@gmail.com",
    url="https://github.com/taylormitchell/github-actions-play",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
