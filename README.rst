Hyde Zipper
-----------

This module precompresses all plaintext files so that properly configured
web servers can serve gzip compressed content without compressing it on
every request.

Installation ::

    pip install hyde-zipper

Install Post Processor::

    SITE_POST_PROCESSORS = {
        '/': {
            'zipper.site_post_processors.GzipCompress' : {
                'filetypes': ['*html', '*.css', '*.js', '*.xml'],
                'level': 9,
            },
        }
    }

Settings
--------

Zipper has 2 settings, filetypes, and level.

filetypes
~~~~~~~~~

A list with file extensions to apply precompression too. defaults to ::

    ['*html', '*.css', '*.js', '*.xml']

level
~~~~~

An integer 1 through 9 that controls the level of compression. 1 is the fastest,
but least amount of compression, and 9 is the slowest, but most amount of
compression. defaults to ::

    9