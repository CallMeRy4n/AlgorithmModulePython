import os

ValueTxT = [
    "file is undefined: self.file is None",
]

class FILE():
    '''
    
    '''

    def __init__(self, path: str, mode="w+"):
        self.path = self.__check_path()
        self.mode = mode.lower()
        self.file = open(file=self.file, mode=self.mode) or None
        self.orginal_txt = self.content

    def __del__(self):
        self.end()

    @property
    def content(self):
        return self.file.read()

    def end(self):
        '''Shutdown whole stream file'''
        if self.file is None:
            raise ValueError(ValueTxT[0])
        self.path = ""
        self.orginal_txt = ""
        self.mode = ""
        self.file.close()
    
    def write(self, txt: str):
        '''Write into the line, no new line, available for [w, a, w+, a+]'''
        if self.file is None:
            raise ValueError(ValueTxT[0])
        elif self.mode not in ["r", "x", "r+"]:
            self.file.write(txt)
        return

    def return_to_orginal(self, close=False):
        if close:
            self.end()
    
    def writeline(self, txt: str):
        '''Write new line, available for append mode'''
        if self.file is None:
            raise ValueError(ValueTxT[0])
        elif self.mode in ["a", "ab"]:
            self.file.write("/n"+ txt)
        else:
            raise ValueError("Currently mode are not 'a' or 'b'")
    