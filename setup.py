import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata-thomasmcdaniel91", # Replace with your own username
    version="2.0.2",
    author="Thomas McDaniel",
    author_email="thomasm9105@gmail.com",
    description="helper functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThomasMcDaniel91/lambdata-thomasmcdaniel91",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)