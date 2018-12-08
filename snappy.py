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
               cli.menu(option)
          elif option in aws_options:
               aws.menu(option)
          elif option in db_options:
               pass
          else:
               print("Unrecognized, try --help flag for options")

             
def menu_options():
     print("--help","shows available menu options")
     print("--helpCLI", "shows available CLI menu options")
     print("--helpAWS", "shows available AWS menu options")
     print("--helpDB", "shows available DropBox menu options")


if __name__ == "__main__":
     cli = CLI()
     aws = AWS()
     main_menu()
