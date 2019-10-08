# FileEmbedandExtract

## Overview
This software helps embedding python file into the PCAP and extracting it from the PCAP directly using Wireshark command line.

## Dependencies
This program runs on Linux/Ubtunu.

It needs python, wireshark, tshark, mergecap, hexdump, text2pcap... 

By default, all the dependencies are installed beforehand for Linux. If not, you will need to install manually.

## Installation Guide
```Console
root@kali # sudo apt-get install python
root@kali # sudo apt-get install wireshark
root@kali # sudo apt-get install tshark
root@kali # sudo apt-get install mergecap
root@kali # sudo apt-get install hexdump
root@kali # sudo apt-get install text2pcap
```

## Making the bash script executable on terminal
In order to run the bash script successfully, please ensure that the directory path is correct and the permission is properly set for the bash script using chmod command:

```Console
root@kali # chmod 755 EmbedandExtractFile.sh
```
The chmod "755" will give you read, write, and execute permission. 

## Run the bash script on Linux Terminal
```Console
root@kali # ./EmbedandExtractFile.sh
```
