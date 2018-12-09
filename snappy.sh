#!/bin/bash
cd ~/snappy
python3 snappy.py --append
#optional upload to S3 bucket after latest snapshot is taken
#python3 snappy.py --uploadAWS
#optional upload to B2 bucket after latest snapshot is taken
#python3 snappy.py --uploadB2
