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
        outDecode = proc.stdout.decode("utf-8").split()
        
        try:
            # outDecode[0]
            get_id = subprocess.run([self.fileops.blaze,"list-file-names",self.bucket, outDecode[0]], stdout=subprocess.PIPE)
            idDecode = get_id.stdout.decode("utf-8").split()
            fileName=outDecode[0]
            fileId=idDecode[17]
            return fileName, fileId[1:-2]
            
        except:
            return None, None

    
    def deleteb2(self,fn, fid):
        subprocess.run([self.fileops.blaze,"delete-file-version", fn, fid])
    
    
    def cpBucket(self):
        os.chdir(self.fileops.snapshots)
        #delete current S3 snapshot
        currentb2_name, currentb2_id = self.lsBucket()
        if currentb2_name != None:
            self.deleteb2(currentb2_name, currentb2_id)
        #get current
        l,f = self.fileops.get_folders()
        #zip current
        self.fileops.createZip(l)
        current = l+".zip"
        #upload current
        subprocess.run([self.fileops.blaze,"upload-file",self.bucket,current,current])
        #delete zip
        self.fileops.cleanZip(current)
    
    def restore(self):
        os.chdir(self.fileops.snapshots)
        #get current and download
        currentb2_name, currentb2_id = self.lsBucket()
        #download
        subprocess.run([self.fileops.blaze,"download-file-by-name",self.bucket,currentb2_name,currentb2_name])
        quit()
        #unzip
        self.fileops.unzipZip(currentb2_name)
        #cleanup zip
        self.fileops.cleanZip(currentb2_name)
        #import new snapshot
        self.cli.import_snap(currentb2_name[:-4])

        
            
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
