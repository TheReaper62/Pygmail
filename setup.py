from distutils.core import setup
setup(
    name='pygmail',
    packages=['pygmail'],
    version='0.1.0',
    license='MIT',
    description='Latest Gmail API Python Wrapper',
    author='FishballNoodles',
    author_email='joelkhor.work@gmail.com',
    url='https://github.com/TheReaper62/Pygmail',
    download_url='https://github.com/TheReaper62/Pygmail/archive/refs/tags/v0.1.0.tar.gz',
    keywords=['python', 'api', 'wrapper','email','gmail'],
    install_requires=[
        'requests',
        'asyncio'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
    ],
)