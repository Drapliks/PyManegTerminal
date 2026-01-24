import os
import sys

os.system('mkdir ~/PythonFiles')
os.system('mkdir ~/PythonProjects')

os.system('clear')

print('Welcome to PyManeg!\n1.Open file\n2.New file\n3.Launch File\n4.Rename file\n5.Delete file\n0.Exit')

while True:
    act = input('>')
    
    if act == '0':
        sys.exit()

    if act == '1':
        opennamefile = input('Enter file name: ')
        os.system('nvim ~/PythonFiles/' + opennamefile + '.py')
        print('Successfully!')

    if act == '2':
        newfilename = input('Enter file name: ')
        os.system('touch ~/PythonFiles/' + newfilename + '.py')
        print('Successfully!')
       
    if act == '3':
        laucnhnamefile = input('Enter file name: ')
        os.system('python ' + laucnhnamefile + '.py')
    
    if act == '4':
        oldnameoffile = input('Old name: ')
        newnameoffile = input('New name: ')
        os.system('mv ~/PythonFiles/' + oldnameoffile + '.py' + ' ' + newnameoffile + '.py')
        print('Successfully!')
    
    if act == '5':
        deletefilename = input('Enter file name: ')
        really = input('Are you sure?(y/n)')
        
        if really == 'y':
            os.system('rm -rf ~/PythonFiles/' + deletefilename + '.py')
            print('Successfully!')

        if really == 'n':
            print('Canceled')
