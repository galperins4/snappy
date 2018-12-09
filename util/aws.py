from util.fileops import FileOps
from util.cli import CLI
import json
import subprocess
import os

class AWS:
    def __init__(self):
        self.fileops = FileOps()
        self.cli = CLI()
        self.bucket=self.import_config()

    
    def import_config(self):
        p = self.fileops.home+ '/snappy/config/bucket.json'
        with open(p) as aws_file:
            aws = json.load(aws_file)
        return aws['aws_bucket']


    def configure(self):
        subprocess.run([self.fileops.aws,"configure"])
    
    
    def lsBucket(self):
        proc = subprocess.run([self.fileops.aws,"s3","ls","s3://"+self.bucket], stdout=subprocess.PIPE)
        outDecode = proc.stdout.decode("utf-8").split()
        try:
            return outDecode[-1]
        except:
            return None
   
    
    def deletes3(self,f):
        subprocess.run([self.fileops.aws,"s3","rm", "s3://"+self.bucket+"/"+f])
    
    
    def cpBucket(self):
        os.chdir(self.fileops.snapshots)
        #delete current S3 snapshot
        currents3 = self.lsBucket()
        if currents3 != None:
            self.deletes3(currents3)
        #get current
        l,f = self.fileops.get_folders()
        #zip current
        self.fileops.createZip(l)
        current = l+".zip"
        #upload current
        subprocess.run([self.fileops.aws,"s3","cp",current,"s3://"+self.bucket+"/"+current])
        #delete zip
        self.fileops.cleanZip(current)
    
    def restore(self):
        os.chdir(self.fileops.snapshots)
        #get current and download
        currents3 = self.lsBucket()
        #download
        subprocess.run([self.fileops.aws,"s3","cp","s3://"+self.bucket+"/"+currents3, currents3])
        #unzip
        self.fileops.unzipZip(currents3)
        #cleanup zip
        self.fileops.cleanZip(currents3)
        #import new snapshot
        self.cli.import_snap(currents3[:-4])

        
    def menu_options(self):
         print("--configureAWS","configures and connects AWS CLI to AWS account")
         print("--uploadAWS", "uploads most recent snapshot to AWS S3")
         print("--downloadAWS", "downloads most recent snapshot from AWS and imports into database")
         
        
    def menu(self, option):
         if option=="--configureAWS":
              self.configure()
         elif option=="--uploadAWS":
              self.cpBucket()
         elif option=="--downloadAWS":
              self.restore()