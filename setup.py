from os import path

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='envparsing',
    version='0.1.0',

    description='Parsing and validation of environment variables',
    long_description=long_description,

    url='https://github.com/cknv/envparse',

    author='Esben Sonne',
    author_email='esbensonne+code@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    packages=['envparse'],
)