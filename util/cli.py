import json
import os
from pathlib import Path
from subprocess import run
import sys


class CLI:
    def __init__(self):
        self.cli_path = '/ark-core/packages/core-snapshots-cli'
        self.snap_path = '/.ark/snapshots/'
        self.env_path = '/.ark/config'
        
        self.db = self.get_database()
        self.cli, self.snapshots = self.get_paths()

        
    def get_paths(self):
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


    def start_proc(self):
        run(["pm2","stop","ark-core-relay", "ark-core-forger"])
     
     
    def stop_proc(self):
        run(["pm2","start","ark-core-relay","ark-core-forger"])
     

    def list_folders(self):
        try:
            folders = [item for item in os.listdir(snapshots) if os.path.isdir(os.path.join(snapshots, item))]
        except:
            print("Oops!!! Looks like no snapshots have been taking. Try --create flag to get started.")
            quit()
    
        if 'rollbackTransactions' in folders:
            folders.remove('rollbackTransactions')
        
        return sorted(folders)


    def view_snap(self):
        dirlist = list_folders()
        print("Available Snapshots:")
        for i in dirlist:
            print(i)

          
    def get_folders(self):
        dirlist = list_folders()
        newlist = [int(i[2:]) for i in dirlist]
        last = "1-"+ str(max(newlist))
        first = "1-"+str(min(newlist))
        return last, first


    def purge_check(self):
        dirlist = list_folders()
        if len(dirlist) > 4:
            l,f = get_folders()
            delete_snap(f)


    def create_snap(self):
        os.chdir(cli)
        run(["yarn","create:"+db])

     
    def import_snap(self,s):
        os.chdir(cli)
        start_proc()
        run(["yarn","import:"+db,"-b",s,"--truncate"])
        stop_proc()


    def verify_snap(self,v):
        os.chdir(cli)
        run(["yarn","verify:"+db,"--blocks",v])


    def append_snap(self,c):
        os.chdir(cli)
        run(["yarn","create:"+db,"--blocks",c])


    def rollback(self,b):
        os.chdir(cli)
        start_proc()
        run(["yarn","rollback:"+db,"-b",b])
        stop_proc()
     
        #delete snaps with blocks beyond rollback value
        dirlist = list_folders()
        newlist = [int(i[2:]) for i in dirlist]
        for i in newlist:
            if i > int(b):
                delete_snap("1-"+str(i))
     

    def delete_snap(self,f):
        print("Purging Snapshot",f)
        os.chdir(snapshots)
        run(["rm","-rf", f])
