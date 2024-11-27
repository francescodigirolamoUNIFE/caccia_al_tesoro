from setuptools import setup

setup(
    name="caccia_al_tesoro",
    version="0.0.1",
    packages=["caccia_al_tesoro"],
    entry_points={
        'console_scripts': [
            'caccia_al_tesoro = caccia_al_tesoro.__main__:main',  # Assicurati che il percorso sia corretto
        ],
    },
)
