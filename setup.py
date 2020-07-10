from setuptools import setup, find_packages


def readme(file='', split=False):
    with open(file) as f:
        if split:
            return f.readlines()
        else:
            return f.read()


setup(
    name='Flameboi',
    version='0.0.1dev',
    description='Slack chat bot',
    long_description=readme('README.md'),
    url='https://github.com/ASU-CodeDevils/flameboi-slack-api',
    author='CodeDevil\'s Student Organization',
    author_email='stucampbell.git@gmail.com',
    packages=find_packages(),
    python_requires='>=3.5',
    license='MIT License',
    install_requires=[
        'Flask',
        'python-dotenv',
        'requests',
        'slack',
        'slackclient',
        'slackeventsapi',
    ],
    classifiers=[
        'Topic :: Communications',
        'Topic :: Communications :: Chat',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',

    ],
)
