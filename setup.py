import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="population",
    version="0.0.1",
    author="miyu iwamoto",
    author_email="s2022006@stu.musashino-u.ac.jp",
    description="Output a graph of population densities in 15 populous countries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MiyuIwamoto/Population",
    project_urls={
        "Bug Tracker": "https://github.com/MiyuIwamoto/Population",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['population'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    entry_points = {
        'console_scripts': [
            'population = population:main'
        ]
    },
)
