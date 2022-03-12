from pathlib import Path
from setuptools import find_packages, setup


CURRENT_DIR = Path(__file__).parent


def get_long_description() -> str:
    """Get long description from README.md."""
    return (CURRENT_DIR / "README.md").read_text(encoding="u8")


setup(
    name="textode",
    version="2.0.0",
    description="Make your text-bot with only one handler.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/Masynchin/textode",
    author_email="masynchin@gmail.com",
    license="MIT",
    packages=find_packages(include=["textode"]),
    python_requires=">=3.7",
)
