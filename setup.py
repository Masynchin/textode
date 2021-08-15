from setuptools import find_packages, setup


setup(
    name="textode",
    version="1.1.0",
    description="Make your text-bot with only one handler",
    url="https://guthib.com/Masynchin/textode",
    author_email="masynchin@gmail.com",
    license="MIT",
    packages=find_packages(include=["textode"]),
    python_requires=">=3.7",  # as asyncio does
)
