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
       
        
        # TBD capture output somehow
    
    def cpBucket(self,f):
        #remove existing
        #get current
        #zip current
        #upload current
        
        
        subprocess.run(["aws","s3","cp",f, "s3://"+self.bucket+"/"+f])
    
    
    def deletes3(self,f):
        subprocess.run(["aws","s3","rm", "s3://"+self.bucket+"/"+f])
    
    def createZip(self,f)
        os.chdir(self.snapshots)
        subprocess.run(["zip","-r",f+".zip",f])
    
    def unzipZip(self,f)
        os.chdir(self.snapshots)
        subprocess.run(["unzip",f,"-d",f[:-4]])
    
    def cleanZip(self,f)
        os.chdir(self.snapshots)
        subprocess.run(["rm",f])
    
    def restore(self):
        #download
        #unzip
        #import
        #cleanup zip
        pass

    
    
    

    #run(["yarn","import:"+self.db,"-b",s,"--truncate
    #delete - aws s3 rm s3://mybucket/test2.txt
    #copy -  aws s3 cp 1-6590390.zip s3://devnet-tester/1-6590390.zip
    #zip command - zip -r 1-6590390.zip 1-6590390
    #unzip command - unzip file.zip -d destination_folder
    #list command -- aws s3 ls s3://mybucket
