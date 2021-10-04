from setuptools import setup

setup(
    name='unitypackage_extractor',
    version='1.1.0',
    description='Extractor for .unitypackage files',
    long_description=open('README.md', 'r').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/Cobertos/unitypackage_extractor/',
    author='Cobertos',
    author_email='me@cobertos.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Build Tools',
        'Topic :: System :: Filesystems'
    ],
    install_requires=[
        'tarsafe>=0.0.2',
    ],
    keywords='untiy unity3d unitypackage extract tar extractor',
    packages=['unitypackage_extractor']
)
