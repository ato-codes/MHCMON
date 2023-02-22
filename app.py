import os
from time import sleep
class MHCMON:
    def __init__(self,file_name):
        self.file_name = file_name
        self.file_path = f'{os.getcwd()}/{file_name}'
        self.extensions = ['.sh','.cs']
        self.first_time_init = True
        self.appName = "MHCMON"
    
    def bash(self):
        os.system(f'bash {self.file_path}')

    def cSharp(self):
        os.system('dotnet run')

    def get_extension(self):
        return self.file_name[self.file_name.index('.'):] if '.' in self.file_name else '.sh'

    def init(self,initilized):
        ext = self.get_extension()
        excuter = 'bash' if ext == '.sh' else 'dotnet run'
        if initilized:
            os.system(f"echo \"$(tput setaf 2)[ {self.appName} ] 0.0.1\"")
            os.system(f"echo \"[ {self.appName} ] watching path/s: {self.file_name}\"")
            os.system(f"echo \"[ {self.appName} ] watching extensions: {ext} $(tput setaf 7)\"")
        else:
            os.system(f"echo \"$(tput setaf 3)[ {self.appName} ] clean exit - waiting for changes before restart\"")
            os.system(f"echo \"[ {self.appName} ] starting : \`{excuter} {self.file_name}\`$(tput setaf 7)\"")
            
        

    def read(self):
        ext = self.get_extension()
        tmp = ''
        while True:
            sleep(.3)
            with open(self.file_path) as f:
                content = f.read()
                if content != tmp:
                    
                    self.init(self.first_time_init)
                    self.first_time_init = False

                    if ext == '.sh':
                        self.bash()
                    elif ext == '.cs':
                        self.cSharp()
                    tmp = content
                    
    def start(self):
        ext = self.get_extension()

        if ext not in self.extensions:
            raise Exception(f"This Program dont run {ext} files.")
            os._exit(1)   

        try:
            self.read()
        except KeyboardInterrupt:
            os._exit(1)
