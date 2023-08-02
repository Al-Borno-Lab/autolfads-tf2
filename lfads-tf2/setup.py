from setuptools import find_packages, setup

setup(
    name="lfads_tf2",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "tensorflow",
        "tensorflow-probability",
        "tensorflow-addons==0.21.0",
        "tensorboard",
        "yacs",
        "PyYAML>=5.1",
        "numpy",
        "pandas",
        "matplotlib",
        "scikit-learn",
        "gitpython",
        "h5py",
        "umap-learn",
        "sphinx",
        "sphinx_rtd_theme",
    ],
    author="Andrew Sedler",
    author_email="arsedler9@gmail.com",
    description="A Tensorflow 2.0 implementation of LFADS",
)
