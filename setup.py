from setuptools import setup, find_packages
import note_client

setup(
    name='NoteClient',
    version='0.1.3',
    packages=find_packages(),
    install_requires=[
        'selenium>=4.12.0',
        'janome>=0.5.0',
        'pyautogui',
        'pyperclip'
    ],
    author='Nao Matsukami',
    author_email='info@mr-insane.net',
    description='Automatically posts articles on note',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Mr-SuperInsane/NoteClient',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
