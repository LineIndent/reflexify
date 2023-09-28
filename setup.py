from setuptools import find_packages, setup

setup(
    name="reflexify",
    version="0.0.9",
    author="S. Ahmad P. Hakimi",
    author_email="pourhakimi@pm.me",
    description="Document, build, and showcase - all in one place, all in Python.",
    long_description="Reflexify is a Python web boilerplate library designed to provide a solid foundation to rapidly build high quality web applications with Python and Reflex. The project comes pre-configured with a range of tools and features to make it easy for developers to get started building their applications, without the need to spend time setting up infrastructure or configuring tools.",  # noqa: E501
    long_description_content_type="text/markdown",
    url="https://github.com/LineIndent/reflexify",
    packages=find_packages(),
    data_files=[("app", ["app/app.py", "app/config.py", "app/router.py"])],
    include_package_data=True,
    install_requires=[
        "click>=8.1.3",
        "reflex>=0.2.4",
        "beautifulsoup4>=4.12.2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "rf-init=reflexify_scripts.create:create",
        ],
    },
    keywords=["python web template", "web application", "documentation"],
)
