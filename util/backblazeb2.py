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
        p = self.fileops.home+ '/snappy/config/blaze.json'
        with open(p) as aws_file:
           blaze = json.load(aws_file)
        return blaze['bucket']
