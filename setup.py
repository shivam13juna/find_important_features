from setuptools import setup

setup(name="find_important_features",
        version="N/A",
        description="FeatureSelector is a class for removing features for a dataset intended for machine learning",
        url="https://github.com/shivam13juna/find_important_features",
        author="Will Koehrsen",
        author_email="shivam13juna@gmail.com",
        license="N/A",
        packages=["find_important_features"],
        install_requires=[
            "lightgbm>=2.1.1",
            "matplotlib>=2.1.2",
            "seaborn>=0.8.1",
            "numpy>=1.14.5",
            "pandas>=0.23.1",
            "scikit-learn>=0.19.1"
            ],
        zip_safe=False)
