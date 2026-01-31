import os
import sys

os.system('mkdir ~/PythonFiles')
os.system('mkdir ~/PythonProjects')

os.system('clear')

print('Welcome to PyManeg!\n1.Open file\n2.New file\n3.Open project\n4.New project\n5.Launch File\n6.Rename file\n7.Delete file\n0.Exit')

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
        endless = True
        openprojectname = input('Enter project name: ')
        print('\nProject: ' + openprojectname + '\n1.Open main.py\n2.Open file\n3.New file\n0.Exit')
        if endless == True:
            actinopenproject = input('>>')
            if actinopenproject == "1":
                os.system('nvim ~/PythonProjects/' + openprojectname +  'main.py')
                print('Succesfully!')
                actinopenproject = input('>>')
            if actinopenproject == "2":
                openfileipname = input('Enter file name: ')
                os.system('nvim ~/PythonProjects/' + openprojectname + "/" + openfileipname + '.py')
                print('Successfully!')
                actinopenproject = input('>>')
            if actinopenproject == "3":
                newfileipname = input('Enter file name: ')
                os.system('touch ~/PythonProjects/' + openprojectname + '/' + newfileipname + '.py')
                print('Successfully!')
                actinopenproject = input('>>')
            if actinopenproject == "0":
                endless = False

    if act == '4':
        newprojectname = input('Enter project name: ')
        os.system('mkdir ~/PythonProjects/' + newprojectname)
        os.system('python -m venv ~/PythonProjects/' + newprojectname +'/venv')
        os.system('touch ~/PythonProjects/' + newprojectname + '/main.py')
        print('Successfully!')
    if act == '5':
        laucnhnamefile = input('Enter file name: ')
        os.system('python ' + laucnhnamefile + '.py')
    
    if act == '6':
        oldnameoffile = input('Old name: ')
        newnameoffile = input('New name: ')
        os.system('mv ~/PythonFiles/' + oldnameoffile + '.py' + ' ' + newnameoffile + '.py')
        print('Successfully!')
    
    if act == '7':
        deletefilename = input('Enter file name: ')
        really = input('Are you sure?(y/n)')
        
        if really == 'y':
            os.system('rm -rf ~/PythonFiles/' + deletefilename + '.py')
            print('Successfully!')

        if really == 'n':
            print('Canceled')
