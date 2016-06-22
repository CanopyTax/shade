from setuptools import setup
import shade

setup(
    name='shade',
    author='nhumrich',
    version=shade.__version__,
    description='Code coverage tool',
    url='https://github.com/CanopyTax/shade',
    install_requires=[
        'Click',
    ],
    license="Apache License 2.0",
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ),
    entry_points={
        'console_scripts': [
            'shade=shade.main:shade'
        ]
    }
)
