# Python Core2 Snapshot Manager

## Installation

```sh
git clone https://github.com/galperins4/snappy
```

## Usage
Install dependencies by running `bash install.sh` comment. If using AWS functionality to back-up to S3 make sure to fill out aws.json in the config folder with bucket name.

Run the script with the appropriate command as follows: `python3 snappy.py --flag`. For available options use the `--help` flag

There is also a bash script `snappy.sh` that has also been included. You can copy the file to your home directory and add the following to crontab `/bin/bash $HOME/snappy.sh > /dev/null 2>&1` in addition to the frequency desired. This will run the append flag based on the frequency set in crontab. A prerequisite of this is that the --create flag has been used at least once to create the initial snapshot to append to. 

## To Do

- to be determined

## Changelog

### 0.2
- refactor CLI functions into a seperate utility class
- Added AWS class and functionality to back-up/rotate snapshots to S3 bucket

### 0.1
- initial release

## Security

If you discover a security vulnerability within this package, please open an issue. All security vulnerabilities will be promptly addressed.

## Credits

- [galperins4](https://github.com/galperins4)
- [All Contributors](../../contributors)

## License

[MIT](LICENSE) © [galperins4](https://github.com/galperins4)





