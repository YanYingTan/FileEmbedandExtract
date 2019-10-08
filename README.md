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
In order to run the bash script successfully, ensure that the permission is properly set for the bash script using chmod command:

```Console
root@kali # chmod 755 EmbedandExtractFile.sh
```
The chmod "755" will give you read, write, and execute permission. 

## Run the bash script on Linux Terminal
```Console
root@kali # ./EmbedandExtractFile.sh
```

## Execution Failed
If execution failed, you will see the error like this..
![Image of Error](/Images/error.PNG)

This error means that there is no such file in that directory. So you will need to change the directory path to the one you saved you script. Then, run the command again.
![Image of cd](/Images/cd.PNG)

## Expected Output
This is what to expect if the execution is successful.
![Image of Output](/Images/successful.PNG)
