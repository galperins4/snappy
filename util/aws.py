from util.cli import CLI
import json
from pathlib import Path
import subprocess
import os

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
        try:
            return outDecode[-1]
        except:
            return None
    
    
    def deletes3(self,f):
        subprocess.run(["aws","s3","rm", "s3://"+self.bucket+"/"+f])
   

    def createZip(self,f):
        os.chdir(self.snapshots)
        subprocess.run(["zip","-r",f+".zip",f])
    
    
    def unzipZip(self,f):
        os.chdir(self.snapshots)
        subprocess.run(["unzip",f])
    
    
    def cleanZip(self,f):
        os.chdir(self.snapshots)
        subprocess.run(["rm",f])
    
    
    def cpBucket(self):
        os.chdir(self.snapshots)
        #delete current S3 snapshot
        currents3 = self.lsBucket()
        if currents3 != None:
            self.deletes3(currents3)
        #get current
        l,f = self.cli.get_folders()
        #zip current
        self.createZip(l)
        current = l+".zip"
        #upload current
        subprocess.run(["aws","s3","cp",current, "s3://"+self.bucket+"/"+current])
        #delete zip
        self.cleanZip(current)
    
    def restore(self):
        os.chdir(self.snapshots)
        #get current and download
        currents3 = self.lsBucket()
        #download
        subprocess.run(["aws","s3","cp","s3://"+self.bucket+"/"+currents3, currents3])
        #unzip
        self.unzipZip(currents3)
        #cleanup zip
        self.cleanZip(currents3)
        #import new snapshot
        self.cli.import_snap(currents3[:-4])
