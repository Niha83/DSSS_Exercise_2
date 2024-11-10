from setuptools import setup, find_packages

setup(
    name="DSSS_Exercise_2", 
    version="0.1",
    packages=find_packages(),
    install_requires=['numpy'],  
    entry_points={
        "console_scripts": [
            "my_command=DSSS_Exercise_2.main:main",  # Replace with your main function or script path
        ]
    },
    author="Niha Nasir",
    author_email="nihanasir83@gmail.com",
    description="A simple math game",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
