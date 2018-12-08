import sys
from util.aws import AWS
from util.cli import CLI


def main_menu():
     cli_options = ["--view","--create","--append","--import","--rollback"]
     aws_options = ["--configureAWS","--uploadAWS","--downloadAWS"]
     db_options = [""]
     
     if len(sys.argv) == 1:
          print("No Arguments Passed, try --help flag for options")
     else:
          option = sys.argv[1]
          if option=="--help":
               menu_options()
          elif option =="--helpCLI":
               cli.menu_options()
          elif option =="--helpAWS":
               aws.menu_options()
          elif option =="--helpDB":
               pass
          elif option in cli_options:
               cli.menu()
          elif option in aws_options:
               aws.menu()
          elif option in db_options:
               pass
               
          
          
          
          
          '''
          elif option=="--view":
               cli.view_snap()
          elif option=="--create":
               cli.create_snap()
               l,f = cli.get_folders()
               cli.verify_snap(l)
               cli.purge_check()
          elif option=="--append":
               l,f = cli.get_folders()
               cli.append_snap(l)
               l,f = cli.get_folders()
               cli.verify_snap(l)
               cli.purge_check()
          elif option=="--import":
               snap_opt = cli.list_folders()
               tmp_menu = {}
               for counter, i in enumerate(snap_opt):
                    tmp_menu[counter+1]=i
                    print(counter+1,"-", i)
               snap_select = int(input("Select one of the options noted above "))
               if snap_select in tmp_menu.keys():
                    cli.import_snap(tmp_menu[snap_select])
               else:
                    print("Something went wrong, please try again")
          elif option=="--rollback":
               block = input("What block would you like to rollback to? ")
               cli.rollback(block)
          elif option=="--configureAWS":
               aws.configure()
          elif option=="--uploadAWS":
               aws.cpBucket()
          elif option=="--downloadAWS":
               aws.restore()
          '''
          else:
               print("Unrecognized, try --help flag for options")
             

def menu_options():
     print("--help","shows available menu options")
     print("--helpCLI", "shows available CLI menu options")
     print("--helpAWS", "shows available AWS menu options")
     print("--helpDB", "shows available DropBox menu options")
     
     
     '''
     print("--view","shows available snapshots to use")
     print("--create","creates a new snapshot")
     print("--append","appends to the most recent snapshot")
     print("--import","imports a specific snapshot")
     print("--rollback","rollback database to specific block")
     print("--configureAWS","configures and connects AWS CLI to AWS account")
     print("--uploadAWS", "uploads most recent snapshot to AWS S3")
     print("--downloadAWS", "downloads most recent snapshot from AWS and imports into database")
     '''

if __name__ == "__main__":
     cli = CLI()
     aws = AWS()
     main_menu()
