import setuptools

setuptools.setup(
    name="django_academy",
    version="0.0.1",
    packages=['about', 'catalog', 'homepage', 'myserver'],
    install_requires=[
        "asgiref==3.6.0",
        "Django==3.2.16",
        "django-environ",
        "pytz==2022.7.1",
        "sqlparse==0.4.3",
    ],
    extras_require={
        "dev": ["flake8==6.0.0", "black==23.1.0"],
        "test": ["pytest==7.2.1"],
    },
)
