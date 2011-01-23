import gzip

class GzipCompress(object):

    @staticmethod
    def process(folder, params):

        class Compressor(object):

            def __init__(self, level):
                self.level = level

            def visit_file(self, thefile):
                file_content = thefile.read_all()
                f = gzip.open('/home/joe/file.txt.gz', 'wb', self.level)
                f.write(file_content)
                f.close()


        filetypes = params.get('filetypes', ['*html', '*.css', '*.js', '*.xml'])
        level = params.get('level', 9)

        for filetype in filetypes:
            folder.walk(Compressor(level), filetype)