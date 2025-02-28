class Sert:
    def __init__(self, root_path='/Uswrs/admin/Library/', dir_path='', root_path_new='',
                 pattern='№\s[0-9][0-9][0-9][0-9]'):
        self._root_path = root_path
        self._dir_path = dir_path
        self._root_path_new = root_path_new
        self._pattern = pattern

    @property
    def root_path(self):
        return self._root_path

    @root_path.setter
    def root_path(self, value):
        self._root_path = value

    @property
    def dir_path(self):
        try:
            return self._dir_path
        except:
            'no dir_path'

    @dir_path.setter
    def dir_path(self, value):
        self._dir_path = value

    @dir_path.deleter
    def dir_path(self):
        del self._dir_path


if __name__ == '__main__':
    q1 = Sert()
    print(q1.root_path)
    q1.root_path = '/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/'
    print(q1.root_path)
    print(f'dir_path: {q1.dir_path}')
    q1.dir_path = '10.07.24/'
    print(f'dir_path: {q1.dir_path}')
    del q1.dir_path
    print(f'dir_path: {q1.dir_path}')
    q1.dir_path = '10.07.24/'
    print(f'dir_path: {q1.dir_path}')
