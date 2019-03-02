#import json
import os
import os.path
from pathlib import Path
import subprocess
from config.config import Config


class FileOps:
    def __init__(self):
        self.get_configs()
        self.home = str(Path.home())
        net = self.net.split('_')
        self.coin, self.network = net[0], net[1]
        self.db = net[1]
        
        # get paths
        self.aws_path = '/.local/bin/aws'
        self.blaze_path = '/.local/bin/b2'
        self.snapshots = self.home+'/.local/share/'+self.coin+'-core/'+self.network+'/snapshots/'
        self.aws = self.home+self.aws_path
        self.blaze = self.home+self.blaze_path
        #self.cli_path = self.core_check()
        #self.cli = self.home+self.cli_path

    '''    
    def core_check(self):
        core_path = self.home + '/core'
        if os.path.exists(core_path) is True:
            p = '/core/packages/core-snapshots-cli'
        else:
            p = '/'+self.coin+'-core/packages/core-snapshots-cli'
        return p
    '''
    
    def get_configs(self):
        c = Config()
        self.net = c.network
        self.aws_bucket = c.aws_bucket
        self.bb_bucket = c.bb_bucket


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
            print("Oops!!! Looks like no snapshots have been taken. Try --create flag to get started.")
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
