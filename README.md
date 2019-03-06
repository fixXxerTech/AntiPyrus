# AntiPyrus-Scanner
***

# Overview

AntiPyrus Scanner is a antimalware scanner written in python, with support for both python2 and python3.
Its primary function is to scan files having python format for malicious syntax which are usually used in 
the desgin and launch of malicious attacks agains unsuspecting individuals.

Python being an interpreted language runs entirely in memory, as such python type programs which are malicious
in nature can easily slip pass the watchful lens of antivirus and antimalware scanners, thus creating a serious
threat. Python is a beautiful technology that is so diverse, and in this diversity also lies threats, AntiPyrus 
was designed to bridge said gap and aid in the creation of a more secure cyber age.

***

# Mode Of Operation

AntiPyrus operates on a fairly simple logic. It reads a python file, crawling through each line in search of set
key words ands syntax usually used in malware creation, it then;

* **Displays the malicious line.** <br>
* **Displays the malicious syntax in the line.** <br>
* **Assesses the level of potential threat of the file.**<br>
* **Offers recommended action to take to stay safe.**<br> 


# Usage

AntiPyrus is launched by passing desired arguments/options from the available list of options.
To see the options, you can run AntiPyrus without an argument/option or pass the "-h"/"--help"
argument.

Example:

`thefixer@thefixer-# python Anti-Pyrus.py`

result:

`AntiPyrus requires arguments [options] to run.`<br>

`usage:  Anti-Pyrus.py [-h] [--verbose] [--version]`<br>
`              [--file   | --folder_scan   | --full_scan]`<br>
`You can only pass one of the above scan types at once, you can however [optionally],`<br>

`Pass "--verbose" with "--file " for much more detailed scan report.`<br>

`e.g. python Anti-Pyrus.py --file <filename.py> --verbose `<br>

`See the option menu below for detailed help.`<br>

`Overview:`<br>
`=========`<br>

`AntiPyrus is an Anti Malware Scanner for python file formats, because python runs in memory,` 
`Antiviruses normally can't spot malicous python code,`<br>
`AntiPyrus was designed to bridge that security gap, it feaures recursive scanning python files in a specified directory by passing the` <br>`"--folder_scan <folder_name>",or a particular file by passing "--file <python_file_name>", you can also run a full scan or your``entire machine starting from the root drive [ "C:\" on windows ] or "/home" | "/Users" directories on linux and mac respectively.`<br>

`NOTE: You can only pass either "--file","--folder_scan" or "--full_scan", You can't combine, just like you'r regular antivirus software allows.`<br>

`        ======================================`<br>
`        || Author: ThefixXxer               ||`<br>
`        || Linkdin: Ikenna Alfred Managwu   ||`<br>
`        || Follow me on Github: @ThefixXxer ||`<br>
`        ======================================`<br>

`optional arguments:`<br>
    `  -h, --help       show this help message and exit`<br>
    `  --verbose        --> Determines quantity of information to display about discovered threats.`<br>
    `  --version        --> Show AntiPyrus current release version number.`<br>
    `  --file           --> Set a particular file to scan, if not used, all python files will be scanned,`<br>
    `                   Usage: python AntiPyrus.py --file suspicious_py_file.py`<br>
    `  --folder_scan    --> Scans all python files in specified folder,`<br>
    `                   Usage: python AntiPyrus.py --folder_scan /root/parent/.`<br>
    `                   NOTE!!: [ This should not be the path to file, rather a directory!! ].`<br>
    `  --full_scan      --> FULL SYSTEM SCAN !!, Scans all python format files from the root`<br>
    `                  directory for windows or the parent directories on linux and mac`<br>
    `                   ['C:\' or '/home' or '/Users'] respectively,`<br>
    `                   Usage: python AntiPyrus.py --full_scan.`<br>


`The above help text shows all options required to run AntiPyrus.`

***

## TODO
* **Add a banner** 

### Perharps
* **Add scan parameters for other file types**
