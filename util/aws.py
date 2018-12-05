import json
from pathlib import Path

class AWS:
    def __init__(self):
        self.snappy_path = Path().resolve().parent
        self.bucket=self.import_config()
    
    
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
