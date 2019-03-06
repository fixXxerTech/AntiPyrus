
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#	Name: AntiPyrus                         		    #
#	Author: ThefixXxer [Managwu Ikenna Alfred]		    #
#	Description: AntiPyrus is an antimalware for files  #
#				 of python format, as python files are  #
#                rather diifficult to scan at run time  #
#                by popular antiviruses cause python,   #
#                runs in memory as such is hard to keep #
#                proper tabs on.				        #
#                                                       #
#    /Please contribute ideas, I NEED THINKERS !!/      #
#   / Also please submit all issues. Thank You !/       #
#													    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#  					                                    #
#                        NOTE:                          #
#					    ------	    				    #
#  AntiPyrus was designed as a means to bridge the gap  #
#  in security analysis of files having the python file # 
#  format, it is a free/open-source software, to be     #
#  used and distributed according to the terms of the   #
#                    MIT license.                       #
#                   								    #
#                                    	 			    #
#	       /PLEASE !! I need a banner!.. anyone?/ 	    #
#													    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #





import os
import sys
import time
import getpass
import hashlib
import platform
import argparse
from os.path import join
from termcolor import colored



Notice= '''\n 
			          NOTICE
		                ----------

It appears you are using an older version of windows as such, due to the nature of your command prompt, you will not have a full colorful AntiPyrus experience. Windows 10 so far is the only windows OS which supports colors in command prompt, perharps try the external console 'cmder' ...

		'''


old_cmd= ['8.1','8','7','XP','Vista']
if platform.system()== 'Windows':
	if platform.release() in old_cmd:
		time.sleep(0.9)
		print (Notice)
		try:
			raw_input('[Enter to Continue]')
		except:
			input('[Enter to continue]')
		#---Color Codex---|
		ERROR= '[-] '     
		SUCCESS= '[+] ' 
		NOTICE= '[!] ' 
		WAITING= '[?] '  
		MAYBE= '[=] '
		PINNER= '[*] '
		DANGER= '[!!!] '
		OK= '[***] '
		ALLOW= '[>>>] '
		CRITICAL= '[.CRITICAL.]'
		LOW_CRITICAL= '[.DANGER.]'
		SAFE= '[.CAUTION.]'
		CLEAN= '[.CLEAN.]'
		VERSION="""
	\n\t<<- AntiPyrus [ Malicous Python Scanner ] Version: 1.0. ->>

	"""
		
	else:
		#----------Color Codex------------|
		ERROR= colored('[-] ','red')     
		SUCCESS= colored('[+] ','green') 
		NOTICE= colored('[!] ','yellow') 
		WAITING= colored('[?] ','blue')  
		MAYBE= colored('[=] ','cyan')    
		MAYBE2= colored(' [=]','cyan')
		PINNER= colored('[*] ','magenta')
		DANGER= "\x1b[1m\x1b[31m[!!!] \x1b[0m"
		DANGER= "\x1b[1m\x1b[5m{}\x1b[0m".format(DANGER)
		OK= "\x1b[1m\x1b[32m[***] \x1b[0m"
		OK= "\x1b[1m\x1b[5m{}\x1b[0m".format(OK)
		ALLOW= "\x1b[1m\x1b[34m[>>>] \x1b[0m"
		ALLOW= "\x1b[1m\x1b[5m{}\x1b[0m".format(ALLOW)
		CRITICAL= "\x1b[1m\x1b[31m[.CRITICAL.]\x1b[0m"
		LOW_CRITICAL= colored('[.DANGER.]','red')
		SAFE= '\x1b[1m\x1b[34m[.CAUTION.]\x1b[0m'
		CLEAN='\x1b[1m\x1b[32m[.CLEAN.]\x1b[0m'
		VERSION='\x1b[1m\x1b[32m{}\x1b[0m'.format("""
	\n\t<<- AntiPyrus [ Malicous Python Scanner ] Version: 1.0. ->>

	""") 
else:
	#----------Color Codex------------|
	ERROR= colored('[-] ','red')     
	SUCCESS= colored('[+] ','green') 
	NOTICE= colored('[!] ','yellow') 
	WAITING= colored('[?] ','blue')  
	MAYBE= colored('[=] ','cyan')    
	MAYBE2= colored(' [=]','cyan')
	PINNER= colored('[*] ','magenta')
	DANGER= "\x1b[1m\x1b[31m[!!!] \x1b[0m"
	DANGER= "\x1b[1m\x1b[5m{}\x1b[0m".format(DANGER)
	OK= "\x1b[1m\x1b[32m[***] \x1b[0m"
	OK= "\x1b[1m\x1b[5m{}\x1b[0m".format(OK)
	ALLOW= "\x1b[1m\x1b[34m[>>>] \x1b[0m"
	ALLOW= "\x1b[1m\x1b[5m{}\x1b[0m".format(ALLOW)
	CRITICAL= "\x1b[1m\x1b[31m[.CRITICAL.]\x1b[0m"
	LOW_CRITICAL= colored('[.DANGER.]','red')
	SAFE= '\x1b[1m\x1b[34m[.CAUTION.]\x1b[0m'
	CLEAN='\x1b[1m\x1b[32m[.CLEAN.]\x1b[0m'
	VERSION='\x1b[1m\x1b[32m{}\x1b[0m'.format("""
	\n\t<<- AntiPyrus [ Malicous Python Scanner ] Version: 1.0. ->>

	""") 


if sys.version_info[0]== 3:
	py3= True
	py2= False
elif sys.version_info[0]== 2:
	py3= False
	py2= True

verbose_var= None
user= getpass.getuser()

if platform.system().lower()== 'windows':
	target_path= 'C:\\'
elif platform.system().lower()== 'linux':
	target_path= '/home'
elif platform.system().lower()== 'darwin':
	target_path= '/Users'



def ScanFile(suspicious_python_file, verbose=verbose_var):
	try:

		#The list of malicious triggers usually used in python malware design. Please feel free to add more. Make sure all are in lowercase.
		dangerlist = ["ngrok.io","servo.net","subprocess","pipe","os.system","sudo rm -rf","socket","connect(","hack","pwn","virus"]
		
		#If you're reading this on your alert pane, don't worry. This is the list of known-bad syntax, so every single one of them will raise flags.
		#It's like checking if 1,2, or 3 is in the list 1,2,3. But props for being paranoid ;)


		#print("AntiPirus 1.0")
		filename= suspicious_python_file
		if os.path.isfile(filename):
			try:
			    f = open(filename,"r")
			except Exception as opn_fle_err:
				time.sleep(0.8)
				print ('\n')
				exit(ERROR+"File could not be opened.\nReason: {} .".format(str(opn_fle_err)))
		else:
			time.sleep(0.8)
			print ('\n')
			exit(ERROR+'Specified file does not exist.')
		contents=f.readlines()

		f.close()

		lines=0
		maliciouslines=0

		for line in contents:
		    line=line.lower().lstrip().strip("   ").strip("\x0B")#Strip extra whitespace mid-code - helps eliminate some obfuscation
		    lines+=1
		    onthisline=0
		    for word in dangerlist:
		        if word in line:
		            if line[:1]=="#" and "hack" not in line and "pwn" not in line:
		                pass #Comments never hurt anybody (Unless they're talking about how someone you were pwnd, in which case it's a danger flag)
		            else:
		                if line[:len("except ")]=="except ":
		                    pass #Who hates error handling?

		                if line[:len("import ")]=="import ":
		                	if verbose:
		                		print('\n'+NOTICE+"WARNING: Potentially hazardous import located on line {}.\nThis may not be malicious, but could be used to assist in malicious deeds.\n{}syntax of alarm:\n{}".format(lines,line,word))
		                	maliciouslines+=1
		                	onthisline+=1
		                else:
		                	if verbose:
		                		print('\n'+NOTICE+"WARNING: Potentially malicious line found on line {0}!\n\n{1}Syntax-->> {2}\n{3}syntax of alarm{4}:\n-------------------\n{5}\n\n=======================================".format(lines,MAYBE,line,PINNER,PINNER,word))
		                	maliciouslines+=1
		                	onthisline+=1
		            
		    if onthisline>=2:
		    	if verbose:
		    		print(NOTICE+"Multiple ({0}) potentially dangerous lines located on line {1}!".format(onthisline,lines))
		    	else:
		    		pass

		print("\n\n---------------------------")
		print(SUCCESS+"File analysis complete.")
		print(NOTICE+"Discovered {0} potentially malicious syntax, out of {1} total lines.".format(maliciouslines,lines))
		print (NOTICE+"Pass '--verbose' argument to view malicious lines.")
		time.sleep(0.8)
		print ('\n')
		print(WAITING+"Final verdict:")
		dangerous=False
		time.sleep(0.8)
		print ('\n')
		Filename= os.path.basename(filename)
		Location= os.path.dirname(filename)
		print (NOTICE+'File Name: {} '.format(Filename))
		time.sleep(0.8)
		print (NOTICE+'Location: {}'.format(str(Location)))
		if maliciouslines>(lines/4) or maliciouslines>20:
			print ('\n')
			print ('Warning Level: {}\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n'.format(CRITICAL))
			print (DANGER+"File is extremely dangerous! Do not execute under any circumstances!")
			dangerous=True
		elif maliciouslines>(lines/10) or maliciouslines>10:
			print ('\n')
			print ('Warning Level: {}\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n'.format(LOW_CRITICAL))
			print (DANGER+"File is deemed highly dangerous, and should not be run.")
			dangerous=True
		elif maliciouslines>(lines/50):
			print ('\n')
			print ('Warning Level: {}\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n'.format(SAFE))
			print (ALLOW+"File is largely safe, but there is a risk of infection. Be cautious when running this file.")
		elif maliciouslines>(lines/100):
			print ('\n')
			print ('Warning Level: {}\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n'.format(CLEAN))
			print (OK+"File is likely safe, and any alerts are likely false positives. However, as always, exercise caution when running this file.")

		else:
			print ('\n')
			print ('Warning Level: {}\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n'.format(CLEAN))
			print(OK+"File is safe, however, please exercise caution when running anyfile, 'security starts in the mind'.")

		print("\n----------------------------")
		print(SUCCESS+"Recommendation:")
		if dangerous:
			print ('\n')
			time.sleep(1.2)
			print("  File is considered potentially dangerous. Manual review is recommended.")
		else:
			print ('\n')
			time.sleep(1.2)
			print("  File is NOT considered particularly dangerous. Manual review is always smart, though ;)")

	except KeyboardInterrupt:
		print ('\n')
		exit(MAYBE+'Ctrl+C passed, Shutting down AntiPyrus...')




def FindFile(file_type, target_path=target_path, verbose=verbose_var):
	try:
		if os.path.exists(target_path):
			if os.path.isdir(target_path):
				print (NOTICE+'Target Folder: --> {}'.format(target_path))
				print ('\n')
				print (SUCCESS+'Starting folder scan...')
				time.sleep(1.2)
				if not verbose:
					print (SUCCESS+'Non-verbose output. ')
				else:
					print (SUCCESS+'Verbose output...')
				time.sleep(1.2)
				print (WAITING+'Scanning...')

			#elif os.path.isfile(target_path):
			#	print ('Target File: --> {}'.format(target_path))
			#	print (SUCCESS+'Starting file scan...')
			#	time.sleep(1.2)
			#	if not verbose:
			#		print (SUCCESS+'Non-verbose output. ')
			#	else:
			#		print (SUCCESS+'Verbose output...')
			#	time.sleep(1.2)
			#	print (WAITING+'Scanning...')

			else:
				print ('\n')
				exit(ERROR+'--folder_scan option, is to be assigned ! A FOLDER ! [ directory ] not a regular file.')


			time.sleep(1)
			if target_path in ('C:\\', '/home', '/Users'):
				print (NOTICE+'A full scan was requested, AntiPyrus will scan all python files from {} directory all the way (...this might take a while)'.format(target_path))
			else:
				pass
			#print ('\n')
			#print (target_path)
			target_file= file_type
			found= 0
			#found_files= ''
			found_files= []
			all_files= 0
			not_found= 0

			for r,d,f in os.walk(target_path):
			# Modifications comming soon here, right now AntiPyrus currently doesn't go layers deep into sub-directories.
			# Of course all contributions are very welcome !!.
				if verbose:
					print ('\n')
					print (WAITING+'Searching --> '+str(r))
				for file in f:
					if file.endswith(target_file):
					#if target_file in file:
						if verbose:
							print ('\n')
							print (SUCCESS+'Found python file at: {}'.format(join(r,file)))
							#found_files += '-> '+join(r,file)+'\n\n'
						found_files.append(join(r,file)) 
						found += 1
						break
					else:
						if verbose:
							print ('\n')
							print (ERROR+'No files with "{}" extension found.'.format(target_file))
						not_found += 1
					all_files += 1
			print ('\n')
			print (SUCCESS+'Found: {0} "{1}" files, out of {2} files scanned'.format(found, target_file, all_files))
			if verbose:
				print ('\n')
				time.sleep(0.8)
				print (SUCCESS+'All files found: ')
				print ('\n')
				if py3:
					input ('[Enter to display them]')
				elif py2:
					raw_input ('[Enter to display them]')
			time.sleep(1)
			print ('\n')
			for File in found_files:
				if verbose:
					print ('=> '+File)
				else:
					pass

			return found_files

		else:
			print (ERROR+'Location {} does not exit.'.format(target_path))
			time.sleep(0.8)
			exit(PINNER+'Re-run with a vaild location.')

	except KeyboardInterrupt:
		print ('\n')
		exit(MAYBE+'Ctrl+C passed, Shutting down AntiPyrus...')

	except Exception as file_scn_err:
		print ('\n')
		print (ERROR+'Error occured while scanning:\n\nError: {}'.format(str(file_scn_err)))
		if py3:
			input (SUCCESS+'Exit AntiPyrus..')
		elif py2:
			raw_input (SUCCESS+'Exit AntiPyrus..')




def drop_file_to_scanner(target_directory, verbose_var=verbose_var):
	file_index= 1
	target_path= target_directory
	#target_file= target_File
	files= FindFile (
				'.py',
				target_path=target_path,
				verbose=verbose_var
				)
	nxt_note= len(files)
	for file in files:
		print ('\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
		print ('\n-------------------------------------------------------------------------------')
		print ('\n')
		print (WAITING+'File number: {}'.format(file_index))
		file_index += 1
		#if verbose_var:
		ScanFile(
			file,
			verbose=verbose_var
			)
		print ('\n-------------------------------------------------------------------------------')
		print ('\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
		time.sleep(0.9)
		print ('\n')
		if nxt_note== file_index:
			print ('\n')
			print (WAITING+'File number: {}'.format(file_index))
			print ('\n')
			exit(SUCCESS+'Scan complete \n   Target folder: {}.'.format(target_path))
		else:
			print (SUCCESS+'Next file...')

#drop_file_to_scanner(
#					'C:\\Users\\hp pc\\Desktop',
#					verbose_var=False
#					)
usage=""" Anti-Pyrus.py [-h] [--verbose] [--version]
              [--file   | --folder_scan   | --full_scan]

You can only pass one of the above scan types at once, you can however [optionally],\n
Pass "--verbose" with "--file" for much more detailed scan report.

e.g. python Anti-Pyrus.py --file <filename.py> --verbose  

See the option menu below for detailed help.

"""



parser = argparse.ArgumentParser( 
	formatter_class=argparse.RawDescriptionHelpFormatter,
	description="""

Overview:
=========

AntiPyrus is an Anti Malware Scanner for python file formats, because python runs in memory, Antiviruses normally can't spot malicous python code,

AntiPyrus was designed to bridge that security gap, it feaures recursive scanning python files in a specified directory by passing the "--folder_scan <folder_name>",\
or a particular file by passing "--file <python_file_name>", you can also run a full scan or your entire machine \
starting from the root drive [ "C:\\" on windows ] or "/home" | "/Users" directories on linux and mac respectively.


NOTE: You can only pass either "--file","--folder_scan" or "--full_scan", You can't combine, just like you'r regular antivirus software allows.   

	======================================
	|| Author: ThefixXxer               ||
	|| Linkdin: Ikenna Alfred Managwu   ||
	|| Follow me on Github: @ThefixXxer ||
	======================================
 	""",
 	usage=usage, 
 	)

parser.add_argument( 
	"--verbose",
	action="store_true",
	help="--> Determines quantity of information to display about discovered threats."
	)

parser.add_argument(
	"--version",
	action="version",
	version=VERSION,
	help="--> Show AntiPyrus current release version number."
	)


only_one = parser.add_mutually_exclusive_group(
	#required=True
	)
 		

only_one.add_argument(
	"--file", 
	#action= "store_true", If uncommented will cause an error as it confilcts with the argument value passed.
	metavar=" ",
	help="--> Set a particular file to scan, if not used, all python files will be scanned,\
	Usage: python AntiPyrus.py --file suspicious_py_file.py."
	)

only_one.add_argument(
	"--folder_scan",
	#action="store_true", If uncommented will cause an error as it confilcts with the argument value passed.
	metavar=" ",
	help="--> Scans all python files in specified folder, Usage: python AntiPyrus.py --folder_scan /root/parent/. \
	NOTE!!: [ This should not be the path to file, rather a directory!! ]."
	)

only_one.add_argument(
	"--full_scan",
	action="store_true",
	help="--> FULL SYSTEM SCAN !!, Scans all python format files from the root directory for windows or the parent directories on linux and mac ['C:\\' or '/home' or '/Usersspecified folder,\
	Usage: python AntiPyrus.py --full_scan."
	)

options= parser.parse_args()


if options.file:
	time.sleep(1)
	print ('\n')
	print (SUCCESS+'File argument used...\n')
	if options.verbose:
		if py3:
			print ('\n') 
			print (NOTICE+'Verbose can display !! A WHOLE LOT !! of information if you use --folder_scan or --full_scan with it.')
			time.sleep(0.8)
			cont= input (WAITING+'Continue with verbose activated? [y/n]: ').lower()
			if cont in ('y','yes'):
				verbose_var= True
				time.sleep(1)
				ScanFile(options.file,
					verbose=verbose_var)
			elif cont in ('n','no'):
				time.sleep(0.8)
				print ('\n')
				print (NOTICE+'Re-run without the "--verbose" flag then.')
				time.sleep(0.8)
				exit(SUCCESS+'Shutting down AntiPyrus...')
			else:
				print ('\n')
				exit(ERROR+'Invalid input, Shutting down AntiPyrus.')

		elif py2:
			print ('\n')
			print (NOTICE+'Verbose can display !! A WHOLE LOT !! of information if you use --folder_scan or --full_scan with it.')
			time.sleep(0.8)
			cont= raw_input (WAITING+'Continue with verbose activated? [y/n]: ').lower()
			if cont in ('y','yes'):
				verbose_var= True
				time.sleep(1)
				ScanFile(options.file,
					verbose=verbose_var)
			elif cont in ('n','no'):
				time.sleep(0.8)
				print ('\n')
				print (NOTICE+'Re-run without the "--verbose" flag then.')
				time.sleep(0.8)
				exit(SUCCESS+'Shutting down AntiPyrus...')
			else:
				print ('\n')
				exit(ERROR+'Invalid input, Shutting down AntiPyrus.')

	else:
		time.sleep(1)
		ScanFile(options.file)


if options.folder_scan:
	time.sleep(1)
	print ('\n')
	print (SUCCESS+'Specific folder passed.\n')
	if options.verbose:
		if py3:
			print ('\n') 
			print (NOTICE+'Verbose can display !! A WHOLE LOT !! of information if you use --folder_scan or --full_scan with it.')
			time.sleep(0.8)
			cont= input (WAITING+'Continue with verbose activated? [y/n]: ').lower()
			if cont in ('y','yes'):
				verbose_var= True
				time.sleep(1)
				target_path= options.folder_scan
				drop_file_to_scanner(
					options.folder_scan,
					verbose_var=verbose_var
					)
			elif cont in ('n','no'):
				time.sleep(0.8)
				print ('\n')
				print (NOTICE+'Re-run without the "--verbose" flag then.')
				time.sleep(0.8)
				exit(SUCCESS+'Shutting down AntiPyrus...')
			else:
				print ('\n')
				exit(ERROR+'Invalid input, Shutting down AntiPyrus.')
		elif py2:
			print ('\n')
			print (NOTICE+'Verbose can display !! A WHOLE LOT !! of information if you use --folder_scan or --full_scan with it.')
			time.sleep(0.8)
			cont= raw_input (WAITING+'Continue with verbose activated? [y/n]: ').lower()
			if cont in ('y','yes'):
				verbose_var= True
				time.sleep(1)
				target_path= options.folder_scan
				drop_file_to_scanner(
					options.folder_scan,
					verbose_var=verbose_var
					)
			elif cont in ('n','no'):
				time.sleep(0.8)
				print ('\n')
				print (NOTICE+'Re-run without the "--verbose" flag then.')
				time.sleep(0.8)
				exit(SUCCESS+'Shutting down AntiPyrus...')
			else:
				print ('\n')
				exit(ERROR+'Invalid input, Shutting down AntiPyrus.')

	else:
		target_path= options.folder_scan
		drop_file_to_scanner(
			options.folder_scan,
			verbose_var=False
			)


if options.full_scan:
	time.sleep(1)
	print ('\n')
	print (SUCCESS+'Starting FULL SYSTEM SCAN [...this could take a while].\n')
	if options.verbose:
		if py3:
			print ('\n') 
			print (NOTICE+'Verbose can display !! A WHOLE LOT !! of information if you use --folder_scan or --full_scan with it.')
			time.sleep(0.8)
			cont= input (WAITING+'Continue with verbose activated? [y/n]: ').lower()
			if cont in ('y','yes'):
				verbose_var= True
				time.sleep(1)
				drop_file_to_scanner(
					target_path,
					verbose_var=verbose_var
					)
			elif cont in ('n','no'):
				time.sleep(0.8)
				print ('\n')
				print (NOTICE+'Re-run without the "--verbose" flag then.')
				time.sleep(0.8)
				exit(SUCCESS+'Shutting down AntiPyrus...')
			else:
				print ('\n')
				exit(ERROR+'Invalid input, Shutting down AntiPyrus.')
		elif py2:
			print ('\n')
			print (NOTICE+'Verbose can display !! A WHOLE LOT !! of information if you use --folder_scan or --full_scan with it.')
			time.sleep(0.8)
			cont= raw_input (WAITING+'Continue with verbose activated? [y/n]: ').lower()
			if cont in ('y','yes'):
				verbose_var= True
				time.sleep(1)
				drop_file_to_scanner(
					target_path,
					verbose_var=verbose_var
					)
			elif cont in ('n','no'):
				time.sleep(0.8)
				print ('\n')
				print (NOTICE+'Re-run without the "--verbose" flag then.')
				time.sleep(0.8)
				exit(SUCCESS+'Shutting down AntiPyrus...')
			else:
				print ('\n')
				exit(ERROR+'Invalid input, Shutting down AntiPyrus.')

	else:
		target_path= options.folder_scan
		drop_file_to_scanner(
			target_path,
			verbose_var=False
			)

#	drop_file_to_scanner(
#		target_path,
#		verbose_var=verbose_var
#		)

elif not options.file and not options.folder_scan and not options.full_scan and not options.verbose:
	print ('\n')
	print ('AntiPyrus requires arguments [options] to run.')
	print ('\n')
	time.sleep(0.8)
	parser.print_help()





# STILL STRUGGLING WITH THE BANNER, ANY HELP WOULD BE GREAT..

#AntiPyrus_help_stack= r''' 

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$
# $$       ____
# $$      /    \         ____     __
# $$     /  /\  \       / |   \  |  |__
# $$    /  /__\  \     |    \    |     \
# $$   /  /    \  \   | |     |  |      \
# $$  /__/      \__\  | |     |  |      |                         
# $$
# $$
# $$
# $$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$




