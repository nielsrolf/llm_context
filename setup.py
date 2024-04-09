from setuptools import find_packages, setup

setup(
    name="llm_context",
    version=0.1,
    description="Description here",
    license="Apache 2.0",
    packages=find_packages(),
    package_data={},
    scripts=[],
    install_requires=[],
    extras_require={},
    entry_points={
        "console_scripts": [
            "concatsrc=llm_context.llm_context:main",
        ],
    },
    classifiers=[],
    keywords="",
)
