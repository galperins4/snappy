# Python Core3 Snapshot Manager

## Installation

```sh
git clone https://github.com/galperins4/snappy
bash install.sh

#optional - configure AWS CLI for S3 upload/downloads
python3 snappy.py --configureAWS

#optional - configure BackBlaze CLI for B2 upload/downloads
python3 snappy.py --authorizeB2

```

## Usage
Run the script with the appropriate command as follows: `python3 snappy.py --flag`. For available options use the `--help` flag

There is also a bash script `snappy.sh` that has also been included. You can copy the file to your home directory and add the following to crontab `/bin/bash $HOME/snappy.sh > /dev/null 2>&1` in addition to the frequency desired. This will run at a frequency based on the frequency set in crontab. 

If using cloud functionality to back-up make sure to fill out config file in the config folder with bucket names for the relevant service. 

For AWS: Make sure your IAM user you are using credentials for has access to S3 Buckets. 

For BackblazeB2: Make sure to set up an application key with write-access and bucket lifecycle is set to last version only

## To Do

- to be determined

## Changelog

### 0.6
- updated for Ark Core 3.0

### 0.5
- updated to support Ark Core 2.2 and new core-CLI snapshot change

### 0.4
- updated to support new typescript core

### 0.3
- refactor a little more
- Added BackBlaze class functionality to back-up/restore snapshots to/from a BackBlaze B2 bucket

### 0.2
- refactor CLI functions into a seperate utility class
- Added AWS class and functionality to back-up/restore snapshots to/from an AWS S3 bucket

### 0.1
- initial release

## Security

If you discover a security vulnerability within this package, please open an issue. All security vulnerabilities will be promptly addressed.

## Credits

- [galperins4](https://github.com/galperins4)
- [All Contributors](../../contributors)

## License

[MIT](LICENSE) © [galperins4](https://github.com/galperins4)





