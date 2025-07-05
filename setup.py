from setuptools import setup, find_packages

setup(
    name="dottar",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        "cryptography",
    ],
    entry_points={
        'console_scripts': [
            'dottar = dottar:main',   # allows `dottar` as terminal command
        ],
    },
    author="Fork & Flow",
    description="🔐 A secure, Git-inspired version control system",
    url="https://github.com/forkandflow/Dottar",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
