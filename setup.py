import setuptools

long_description: str

with open("README.md", "r", encoding="utf-8") as readme_file_desc:
    long_description = readme_file_desc.read()
    
setuptools.setup(
  name = 'appwrite',
  packages = [
    'appwrite',
    'appwrite/services',
    'appwrite/encoders',
    'appwrite/enums',
  ],
  version = '7.0.1',
  license='BSD-3-Clause',
  description = 'Appwrite is an open-source self-hosted backend server that abstract and simplify complex and repetitive development tasks behind a very simple REST API',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  author = 'Appwrite Team',
  author_email = 'team@appwrite.io',
  maintainer = 'Appwrite Team',
  maintainer_email = 'team@appwrite.io',
  url = 'https://appwrite.io/support',
  download_url='https://github.com/appwrite/sdk-for-python/archive/7.0.1.tar.gz',
  install_requires=[
    'requests',
  ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Environment :: Web Environment',
    'Topic :: Software Development',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
