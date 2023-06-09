from distutils.core import setup
setup(
  name = 'rivalapi',         # How you named your package folder (MyLib)
  packages = ['rivalapi'],   # Chose the same as "name"
  version = '0.01',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = "A Python API wrapper for Rival's API",   # Give a short description about your library
  author = 'Cop',                   # Type in your name
  author_email = 'z@rival.rocks',      # Type in your E-Mail
  url = 'https://github.com/cop-discord/rivalapi/',   # Provide either the link to your github or to your website
  keywords = ['rivalapi', 'rival', 'api'],   # Keywords that define your package best
  install_requires=[
          'aiohttp','orjson','asyncio','humanize','munch'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      # Specify which Python versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
