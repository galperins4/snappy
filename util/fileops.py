class FileOps:
    pass

    def createZip(self,f):
        os.chdir(self.snapshots)
        subprocess.run(["zip","-r",f+".zip",f])
    
    
    def unzipZip(self,f):
        os.chdir(self.snapshots)
        subprocess.run(["unzip",f])
    
    
    def cleanZip(self,f):
        os.chdir(self.snapshots)
        subprocess.run(["rm",f])
