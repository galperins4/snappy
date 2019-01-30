import json
import os
from pathlib import Path
import subprocess
from dotenv import load_dotenv


class FileOps:
    def __init__(self):
        self.home = str(Path.home())
        self.cli_path = '/ark-core/packages/core-snapshots-cli'
        self.snap_path = '/.ark/snapshots/'
        self.env_file = '/.ark/.env'
        self.aws_path = '/.local/bin/aws'
        self.blaze_path = '/.local/bin/b2'
        
        self.db = self.get_database()
        self.cli, self.snapshots, self.aws, self.blaze = self.get_paths()

        
    def get_paths(self):
        c_path = self.home+self.cli_path
        s_path = self.home+self.snap_path+self.db
        a_path = self.home+self.aws_path
        b_path = self.home+self.blaze_path
    
        return c_path, s_path, a_path, b_path


    def get_database(self):
        #get dot path for load_env and load
        dot = self.home+self.env_file
        load_dotenv(dot)
        return os.getenv("ARK_DB_DATABASE").split('_')[1]

    def createZip(self,f):
        os.chdir(self.snapshots)
        subprocess.run(["zip","-r",f+".zip",f])
    
    
    def unzipZip(self,f):
        os.chdir(self.snapshots)
        subprocess.run(["unzip",f])
    
    
    def cleanZip(self,f):
        os.chdir(self.snapshots)
        subprocess.run(["rm",f])
        
    def list_folders(self):
        try:
            folders = [item for item in os.listdir(self.snapshots) if os.path.isdir(os.path.join(self.snapshots, item))]
        except:
            print("Oops!!! Looks like no snapshots have been taking. Try --create flag to get started.")
            quit()
    
        if 'rollbackTransactions' in folders:
            folders.remove('rollbackTransactions')
        
        return sorted(folders)

    
    def get_folders(self):
        dirlist = self.list_folders()
        newlist = [int(i[2:]) for i in dirlist]
        last = "1-"+ str(max(newlist))
        first = "1-"+str(min(newlist))
        return last, first
