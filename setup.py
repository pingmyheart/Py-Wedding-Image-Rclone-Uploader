import warnings

from setuptools import setup, find_packages

# Suppress all warnings
warnings.filterwarnings("ignore")

setup(
    name='py-wedding-image-rclone-uploader',
    version='0.0.1.dev0',
    packages=find_packages()
)
