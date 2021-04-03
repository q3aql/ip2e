ip2e - Receive your public IP (dynamic) by email when it is renewed.
====================================================================

### Tools:
  
  * [ip2e-daemon.py](https://github.com/q3aql/ip2e/blob/master/src/ip2e-daemon.py) - Daemon to control & send by email your public IP.
  * [ip2e-log.py](https://github.com/q3aql/ip2e/blob/master/src/ip2e-log.py) - Tool to see the log file when daemon is running. 
  * [ip2e-config.py](https://github.com/q3aql/ip2e/blob/master/src/ip2e-config.py) - Tool to create a valid configuration file.
    
### Downloads:

  * [ip2e-1.3.2-all.deb](https://github.com/q3aql/ip2e/releases/download/v1.3.2/ip2e-1.3.2-all.deb)
  * [ip2e-1.3.2-all.rpm](https://github.com/q3aql/ip2e/releases/download/v1.3.2/ip2e-1.3.2-all.rpm)
  * [ip2e-1.3.2.tar.bz2](https://github.com/q3aql/ip2e/releases/download/v1.3.2/ip2e-1.3.2.tar.bz2)
  * [ip2e-1.3.2.tar.gz](https://github.com/q3aql/ip2e/releases/download/v1.3.2/ip2e-1.3.2.tar.gz)

_Dependence: `python3`._

### Installation:

  * **Unix systems (GNU/Linux,BSD,etc..):**
  
    * Open the terminal and type the following comands:
    
      ```shell
      $ git clone https://github.com/q3aql/ip2e.git
      $ cd ip2e
      $ sudo make install
      ````

_Note: You must install `git` previously._

  * **Mac OS X:**
  
    * Open the terminal and type the following comands:
    
      ```shell
      $ git clone https://github.com/q3aql/ip2e.git
      $ cd ip2e
      $ sudo make -f Makefile.OSX
      ````
     
_Note: You must install `git` previously._
     
  * **Windows:**
 
    * Install Python 3.x from https://www.python.org/.
    * Download `ip2e` from [here](https://github.com/q3aql/ip2e/archive/master.zip).
    * Unzip the package in your system. For example in `C:\Program Files\`.
    * Double click on `Install.cmd`.
      
### How to use:

  * **Create a valid configuration file:**
  
    * First, you must create the configuration file needed to run `ip2e` correctly. 
      To do this, run the tool called `ip2e-config.py`:

      ```shell
      $ ip2e-config.py
      ````
     
  * **Run the daemon:**
  
    * When are configured the necessary data of the email sender & receiver, you can 
      run the tool called `ip2e-daemon.py`:
    
      ```shell
      $ ip2e-daemon.py
      ````
      
    * When daemon is running you can see the log file running the `ip2e-log.py` tool:
    
      ```shell
      $ ip2e-log.py
      ````
      
### Images (Screenshots):

<img src="https://raw.githubusercontent.com/q3aql/ip2e/master/img/ip2e-command.png" width="700" />

### External links:

  * [Python3 homepage](https://www.python.org/downloads/)
