import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'appwrite',
  packages = ['appwrite', 'appwrite/services'],
  version = '0.6.1',
  license='BSD-3-Clause',
  description = 'Appwrite is an open-source self-hosted backend server that abstract and simplify complex and repetitive development tasks behind a very simple REST API',
  long_description = long_description,
  author = 'Appwrite Team',
  author_email = 'team@appwrite.io',
  maintainer = 'Appwrite Team',
  maintainer_email = 'team@appwrite.io',
  url = 'https://appwrite.io/support',
  download_url='https://github.com/appwrite/sdk-for-python/archive/0.6.1.tar.gz',
  # keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],
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
