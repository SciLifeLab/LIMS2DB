from setuptools import setup, find_packages
import glob
import subprocess


def get_version():
    return "1.0+{}".format(
        subprocess.check_output(["git", "rev-parse", "HEAD"]).strip().decode("utf-8")
    )


try:
    with open("requirements.txt", "r") as f:
        install_requires = [x.strip() for x in f.readlines()]
except IOError:
    install_requires = []

setup(
    name="LIMS2DB",
    version=get_version(),
    author="Maya Brandi, Denis Moreno",
    author_email="maya.brandi@scilifelab.se, denis.moreno@scilifelab.se",
    description="Fetching data from Genologics LIMS and pushing it to statusdb",
    install_requires=install_requires,
    packages=find_packages(),
    scripts=glob.glob("scripts/*.py"),
)
