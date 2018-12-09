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
