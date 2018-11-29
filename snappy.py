import os
from pathlib import Path
from subprocess import call


#cli_path='/ark-core/packages/core-snapshots-cli'
#snap_path='/.ark/snapshots/devnet'
#env_path='/.ark'


def get_paths():
     home = str(Path.home())
     c_path = home+cli_path
     s_path = home+snap_path
     e_path = home_e_path
     
     return c_path, s_path, e_path


def list_folders():
     return [item for item in os.listdir(snapshots) if os.path.isdir(os.path.join(snapshots, item))]


def get_folder():
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


def first_snap():
     os.chdir(cli)
     call(["yarn","create:devnet"])

     
def import_snap(s):
     os.chdir(cli)
     call(["pm2","stop","all"])
     call(["yarn","import:devnet","-b",s,"--truncate"])
     call(["pm2","start","all"])


def verify_snap(v):
     os.chdir(cli)
     call(["yarn","verify:devnet","--blocks",v])


def append_snap(c):
     os.chdir(cli)
     call(["yarn","create:devnet","--blocks",c])


def rollback(b):
     os.chdir(cli)
     call(["yarn","rollback:devnet","-b",b])
     
     
def menu(a):
     print("End of Program")

     
if __name__ == "__main__":
     cli, snap, env = get_vars()
     db = get_database()
     
     
     quit()
     
     
     
     '''
     l,f = get_folder()
     import_snap(l)
     '''


