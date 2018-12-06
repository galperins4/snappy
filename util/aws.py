from util.cli import CLI
import json
from pathlib import Path
import subprocess

class AWS:
    def __init__(self):
        self.path = Path().resolve().parent
        self.bucket=self.import_config()
        self.cli=CLI()
        
        self.db = self.cli.db
        self.clip = self.cli.cli 
        self.snapshots = self.cli.snapshots

    
    def import_config(self):
        with open(self.path / 'snappy/config/aws.json') as aws_file:
            aws = json.load(aws_file)
        return aws['bucket']


    def configure(self):
        subprocess.run(["aws","configure"])
    
    
    def lsBucket(self):
        proc = subprocess.run(["aws","s3","ls","s3://"+self.bucket], stdout=subprocess.PIPE)
        outDecode = proc.stdout.decode("utf-8").split()
        #last string split should be snapshot name
        return outDecode[-1]
    
    
    def deletes3(self,f):
        subprocess.run(["aws","s3","rm", "s3://"+self.bucket+"/"+f])
    
    def createZip(self,f):
        os.chdir(self.snapshots)
        subprocess.run(["zip","-r",f+".zip",f])
    
    
    def unzipZip(self,f):
        os.chdir(self.snapshots)
        subprocess.run(["unzip",f,"-d",f[:-4]])
    
    
    def cleanZip(self,f):
        os.chdir(self.snapshots)
        subprocess.run(["rm",f])
    
    
    def cpBucket(self):
        #delete current S3 snapshot
        currents3 = self.lsBucket()
        print(currents3)
        quit()
        self.deletes3(currents3)
        #get current
        l,f = self.cli.get_folders()
        os.chdir(self.snapshots)
        #zip current
        self.createZip(l)
        current = l+".zip"
        #upload current
        subprocess.run(["aws","s3","cp",current, "s3://"+self.bucket+"/"+current])
        #delete zip
        cleanZip(current)
    
    def restore(self):
        #download
        #unzip
        #import
        #cleanup zip
        pass
