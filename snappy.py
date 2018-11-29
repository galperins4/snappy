import json
import os
from pathlib import Path
from subprocess import call
import sys


cli_path='/ark-core/packages/core-snapshots-cli'
snap_path='/.ark/snapshots/'
env_path='/.ark/config'

def get_paths():
     home = str(Path.home())
     c_path = home+cli_path
     s_path = home+snap_path+db
     
     return c_path, s_path


def get_database():
     home = str(Path.home())
     env = home+env_path
     with open(env + '/network.json') as network_file:
          network = json.load(network_file)

     return network['name']
                
def list_folders():
     return [item for item in os.listdir(snapshots) if os.path.isdir(os.path.join(snapshots, item))]


def get_folders():
     dirlist = list_folders()
     newlist = [int(i[2:]) for i in dirlist]
     last = "1-"+ str(max(newlist))
     first = "1-"+str(min(newlist))
     return last, first


def purge_snap():
     dirlist = list_folders()
     if len(dirlist) > 4:
          l,f = get_folder()
          print("Purging Snapshot",f)
          os.chdir(snapshots)
          call(["rm","-rf", f])


def create_snap():
     os.chdir(cli)
     call(["yarn","create:"+db])

     
def import_snap(s):
     os.chdir(cli)
     call(["pm2","stop","all"])
     call(["yarn","import:"+db,"-b",s,"--truncate"])
     call(["pm2","start","all"])


def verify_snap(v):
     os.chdir(cli)
     call(["yarn","verify:"+db,"--blocks",v])


def append_snap(c):
     os.chdir(cli)
     call(["yarn","create:"+db,"--blocks",c])


def rollback(b):
     os.chdir(cli)
     call(["pm2","stop","all"])
     call(["yarn","rollback:"+db,"-b",b])
     call(["pm2","start","all"])
     
def menu():
     try:
          print(sys.argv[1])
     except:
          print("No Arguments Passed")

     
if __name__ == "__main__":
     db = get_database()
     cli, snapshots = get_paths()
     menu()
     
     
     '''
     l,f = get_folder()
     import_snap(l)
     '''


