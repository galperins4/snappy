import json
import os
from pathlib import Path
from subprocess import run
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
     try:
          folders = [item for item in os.listdir(snapshots) if os.path.isdir(os.path.join(snapshots, item))]
     except:
          print("Oops!!! Looks like no snapshots have been taking. Try --create flag to get started.")
          quit()
    
     if 'rollbackTransactions' in folders:
          folders.remove('rollbackTransactions')
     return sorted(folders)


def view_snap():
     dirlist = list_folders()
     print("Available Snapshots:")
     for i in dirlist:
          print(i)

def get_folders():
     dirlist = list_folders()
     newlist = [int(i[2:]) for i in dirlist]
     last = "1-"+ str(max(newlist))
     first = "1-"+str(min(newlist))
     return last, first


def purge_check():
     dirlist = list_folders()
     if len(dirlist) > 5:
          l,f = get_folders()
          delete_snap(f)


def create_snap():
     os.chdir(cli)
     run(["yarn","create:"+db])

     
def import_snap(s):
     os.chdir(cli)
     run(["pm2","stop","ark-core-relay", "ark-core-forger"])
     run(["yarn","import:"+db,"-b",s,"--truncate"])
     run(["pm2","start","ark-core-relay","ark-core-forger"])


def verify_snap(v):
     os.chdir(cli)
     run(["yarn","verify:"+db,"--blocks",v])


def append_snap(c):
     os.chdir(cli)
     run(["yarn","create:"+db,"--blocks",c])


def rollback(b):
     os.chdir(cli)
     run(["pm2","stop","ark-core-relay","ark-core-forger"])
     run(["yarn","rollback:"+db,"-b",b])
     run(["pm2","start","ark-core-relay","ark-core-forger"])
     
     #delete snaps with blocks beyond rollback value
     dirlist = list_folders()
     newlist = [int(i[2:]) for i in dirlist]
     for i in newlist:
          if i > int(b):
               delete_snap("1-"+str(i))
     

def delete_snap(f):
     print("Purging Snapshot",f)
     os.chdir(snapshots)
     run(["rm","-rf", f])
     

def menu():
     if len(sys.argv) == 1:
          print("No Arguments Passed, try --help flag for options")
     else:
          option = sys.argv[1]
          if option=="--help":
               menu_options()
          elif option=="--view":
               view_snap()
          elif option=="--create":
               create_snap()
               l,f = get_folders()
               verify_snap(l)
               purge_check()
          elif option=="--append":
               l,f = get_folders()
               append_snap(l)
               l,f = get_folders()
               verify_snap(l)
               purge_check()
          elif option=="--import":
               snap_opt = list_folders()
               tmp_menu = {}
               for counter, i in enumerate(snap_opt):
                    tmp_menu[counter+1]=i
                    print(counter+1,"-", i)
               
               snap_select = int(input("Select one of the options noted above "))
               if snap_select in tmp_menu.keys():
                    import_snap(tmp_menu[snap_select])
               else:
                    print("Something went wrong, please try again")
               
               
          elif option=="--rollback":
               block = input("What block would you like to rollback to? ")
               rollback(block)
          else:
               print("Unrecognized, try --help flag for options")
               

def menu_options():
     print("--help","shows available menu options")
     print("--view","shows available snapshots to use")
     print("--create","creates a new snapshot")
     print("--append","appends to the most recent snapshot")
     print("--import","imports a specific snapshot")
     print("--rollback","rollback database to specific block")
   

if __name__ == "__main__":
     db = get_database()
     cli, snapshots = get_paths()
     menu()
