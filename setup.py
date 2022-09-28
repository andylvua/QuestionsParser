from setuptools import setup, find_packages

if __name__ == '__main__':
    setup(
        name='QuestionsParser',
        packages=find_packages(),
        version='1.0.1',
        description='A Python package for parsing questions from pdf files.',
        author='Andrew Yaroshevych',
        install_requires=[
            'regex==2022.9.13',
            'cloudscraper==1.2.64',
            'beautifulsoup4==4.11.1',
            'pypdf2==2.11.0',
            'fpdf==1.7.2',
            'python-docx==0.8.11',
            'setuptools==65.4.0',
            'retry==0.9.2',
        ],
    )
