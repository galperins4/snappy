from cli import CLI
import json
from pathlib import Path

class AWS:
    def __init__(self):
        self.snappy_path = Path().resolve().parent
        self.bucket=self.import_config()
        self.cli=CLI()
        
        self.db = self.cli.get_database()
        self.cli, self.snapshots = cli.self.get_paths()

    
    def import_config(self):
        with open(self.snappy_path / 'config/aws.json') as aws_file:
        aws = json.load(aws_file)
        return aws['bucket']


    def lsBucket(self):
        pass
    
    
    def cpBucket(self):
        pass
    
    
    def rotate(self):
        pass
    
    
    def restore(self):
        pass

    
    #os.chdir(self.cli)
    #run(["yarn","import:"+self.db,"-b",s,"--truncate
    #delete - aws s3 rm s3://mybucket/test2.txt
    #copy -  aws s3 cp 1-6590390.zip s3://devnet-tester/1-6590390.zip
    #zip command - zip -r 1-6590390.zip 1-6590390
    #unzip command - unzip file.zip -d destination_folder
