from setuptools import setup

setup(
    name='Weather Forecast',
    packages=['weatherforecast'],
    version='1.0',
    licence='MIT',
    author='Piotr Kluziok',
    author_email='piotrkluziok@gmail.com',
    description='Weather forecast data',
    url='https://github.com/ProjectManiacc/Python-Projects',
    keywords=['weather','forecast','openweather'],
    python_requires='>=3.7, <4',
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Developmemt Statis :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
    ]

)
