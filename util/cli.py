import os
from subprocess import run
from util.fileops import FileOps


class CLI:
    def __init__(self):
        self.fileops = FileOps()
        self.switch = self.control()
        

    def control(self):
        check = self.fileops.home+'/'+self.fileops.coin+'-core'
        if os.path.isdir(check):
            self.token = self.fileops.coin
            self.net = self.fileops.network
            self.path = check+'/packages/core/bin/run'
            return True
        else:
            return False


    def stop_proc(self):
        run(["pm2","stop",self.fileops.coin+"-relay"])
        run(["pm2","stop",self.fileops.coin+"-forger"])
        run(["pm2","stop",self.fileops.coin+"-core"])    
     
     
    def start_proc(self):
        run(["pm2","start",self.fileops.coin+"-relay"])
        run(["pm2","start",self.fileops.coin+"-forger"])
        run(["pm2","start",self.fileops.coin+"-core"])

        
    def view_snap(self):
        dirlist = self.fileops.list_folders()
        print("Available Snapshots:")
        for i in dirlist:
            print(i)


    def purge_check(self):
        dirlist = self.fileops.list_folders()
        if len(dirlist) > 4:
            l,f = self.fileops.get_folders()
            self.delete_snap(f)


    def create_snap(self):
        if self.switch:
            run([self.path, "snapshot:dump", "--network", 
                 self.net, "--token", self.token])
        else:
            run([self.fileops.coin,"snapshot:dump"])

     
    def import_snap(self,s):
        self.stop_proc()
        if self.switch:
            run([self.path, "snapshot:truncate", "--network", 
                 self.net, "--token", self.token])
            run([self.path, "snapshot:restore", "--blocks", s, "--network", 
                 self.net, "--token", self.token])
        else:
            run([self.fileops.coin,"snapshot:truncate"])
            run([self.fileops.coin,"snapshot:restore", "--blocks",s])
        self.start_proc()


    def verify_snap(self,v):
        if self.switch:
            run([self.path, "snapshot:verify", "--blocks", v, "--network", 
                 self.net, "--token", self.token])
        else:
            run([self.fileops.coin,"snapshot:verify","--blocks",v])


    def append_snap(self,c):
        increment = int(c.split('-')[1])+1
        if self.switch:
            run([self.path, "snapshot:dump", "--blocks", c, "--network", 
                 self.net, "--token", self.token])
        else:
            run([self.fileops.coin,"snapshot:dump","--start",str(increment)])

            
    def rollback(self,b):
        self.stop_proc()
        if self.switch:
            run([self.path, "snapshot:rollback", "--height", b, "--network", 
                 self.net, "--token", self.token])
        else:
            run([self.fileops.coin,"snapshot:rollback","--height",b])
        self.start_proc()
     
        #delete snaps with blocks beyond rollback value
        dirlist = self.fileops.list_folders()
        newlist = [int(i[2:]) for i in dirlist]
        for i in newlist:
            if i > int(b):
                self.delete_snap("1-"+str(i))
     

    def delete_snap(self,f):
        print("Purging Snapshot",f)
        os.chdir(self.fileops.snapshots)
        run(["rm","-rf", f])

        
    def menu_options(self):
        print("--view","shows available snapshots to use")
        print("--create","creates a new snapshot")
        # print("--append","appends to the most recent snapshot")
        print("--import","imports a specific snapshot")
        print("--rollback","rollback database to specific block")

        
    def menu(self, option):
        if option=="--view":
               self.view_snap()
        elif option=="--create":
               self.create_snap()
               l,f = self.fileops.get_folders()
               self.verify_snap(l)
               self.purge_check()
        # elif option=="--append":
          #      l,f = self.fileops.get_folders()
          #      self.append_snap(l)
          #      l,f = self.fileops.get_folders()
          #      self.verify_snap(l)
          #      self.purge_check()
        elif option=="--import":
               snap_opt = self.fileops.list_folders()
               tmp_menu = {}
               for counter, i in enumerate(snap_opt):
                    tmp_menu[counter+1]=i
                    print(counter+1,"-", i)
               snap_select = int(input("Select one of the options noted above "))
               if snap_select in tmp_menu.keys():
                    self.verify_snap(tmp_menu[snap_select])
                    self.import_snap(tmp_menu[snap_select])
               else:
                    print("Something went wrong, please try again")
        elif option=="--rollback":
               block = input("What block would you like to rollback to? ")
               self.rollback(block)
