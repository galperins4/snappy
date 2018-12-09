from util.fileops import FileOps
from util.cli import CLI
import json
import subprocess
import os


class BackBlazeB2:
    def __init__(self):
        self.fileops = FileOps()
        self.cli = CLI()
        self.bucket=self.import_config()

    
    def import_config(self):
        p = self.fileops.home+ '/snappy/config/bucket.json'
        with open(p) as blaze_file:
           blaze = json.load(blaze_file)
        return blaze['blaze_bucket']

    def authorize(self):
        subprocess.run([self.fileops.blaze,"authorize-account"])
    
    
    def lsBucket(self):
        proc = subprocess.run([self.fileops.blaze,"ls",self.bucket], stdout=subprocess.PIPE)
        print(proc)
        quit()
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
         print("--authorizeB2","configures authorizes BackBlaze B2 connection")
         print("--uploadB2", "uploads most recent snapshot to BackBlaze B2")
         print("--downloadB2", "downloads most recent snapshot from BackBlaze B2 and imports into database")
         
        
    def menu(self, option):
         if option=="--authorizeB2":
              self.authorize()
         elif option=="--uploadB2":
              self.cpBucket()
         elif option=="--downloadB2":
              self.restore()
