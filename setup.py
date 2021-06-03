from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="tf-keras-vis",
    version="0.6.2",
    author="keisen",
    author_email="k.keisen@gmail.com",
    description="Neural network visualization toolkit for tf.keras",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/keisen/tf-keras-vis",
    packages=find_packages(),
    classifiers=[
        "Environment :: GPU :: NVIDIA CUDA",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Education",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.6, <3.10',
    install_requires=['scipy', 'pillow', 'deprecated', 'imageio', 'packaging'],
    extras_require={
        'develop': ['flake8', 'isort', 'yapf', 'pytest', 'pytest-pycodestyle', 'pytest-cov'],
        'examples': ['jupyterlab==2.*', 'jedi==0.17.*', 'matplotlib'],
    },
    include_package_data=True,
)
