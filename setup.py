 
from setuptools import setup


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
    url='https://gitlab.com/ASU-CodeDevils/flameboi-slack-api',
    author='CodeDevil\'s Student Organization',
    author_email='stucampbell.git@gmail.com',
    #package_dir={'': 'canvasscraper',
    #            'fileops': 'canvasscraper/fileops',
    #            'objects': 'canvasscraper/objects',
    #            },
    packages=[
        'canvasscraper',
        'canvasscraper.fileops',
        'canvasscraper.objects',
    ],
    python_requires='>=3.5',
    license='MIT License',
    install_requires=[
        'pyderman',
        'selenium',
        'youtube-dl',
    ],
    classifiers=[
        'Topic :: Education',
        'Topic :: Education :: Computer Aided Instruction (CAI)',
        'Topic :: Multimedia :: Video',
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)