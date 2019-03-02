import os
from dotenv import load_dotenv
from pathlib import Path

class Config():
    def __init__(self):
        self.home = str(Path.home())
        env_path = self.home + '/snappy/config/config'
        load_dotenv(env_path)
        load_network_config()
        load_aws_config()
        load_backblaze_config()
    
    
    def load_network_config(self):
        self.network = os.getenv("NETWORK")
        
        
    def load_aws_config(self):
        self.aws_bucket = os.getenv("AWS_BUCKET")
        
        
    def load_backblaze_config(self):
        self.bb_bucket = os.getenv("BB_BUCKET")
