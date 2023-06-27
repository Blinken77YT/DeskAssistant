from setuptools import setup, find_packages

VERSION = '0.0.8'
DESCRIPTION = 'A package to help with making a virtual assistant'

# Setting up
setup(
    name="deskAssistant",
    version=VERSION,
    author="Blinken77YT",
    author_email="theonilsson2012@icloud.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pyttsx3', 'speechrecognition', 'pyaudio'],
    keywords=['python', 'virtual', 'assistant', 'assistant virtual', 'virtual assistant'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)