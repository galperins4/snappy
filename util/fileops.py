class FileOps:
    def __init__(self):
        self.cli_path = '/ark-core/packages/core-snapshots-cli'
        self.snap_path = '/.ark/snapshots/'
        self.env_path = '/.ark/config'
        
        self.db = self.get_database()
        self.cli, self.snapshots = self.get_paths()

        
    def get_paths(self):
        home = str(Path.home())
        c_path = home+self.cli_path
        s_path = home+self.snap_path+self.db
     
        return c_path, s_path


    def get_database(self):
        home = str(Path.home())
        env = home+self.env_path
        with open(env + '/network.json') as network_file:
            network = json.load(network_file)

        return network['name']

    def createZip(self,f):
        os.chdir(self.snapshots)
        subprocess.run(["zip","-r",f+".zip",f])
    
    
    def unzipZip(self,f):
        os.chdir(self.snapshots)
        subprocess.run(["unzip",f])
    
    
    def cleanZip(self,f):
        os.chdir(self.snapshots)
        subprocess.run(["rm",f])
