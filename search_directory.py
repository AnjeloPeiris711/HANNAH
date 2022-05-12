from ctypes import windll
import string
import os
import stat
file_system_dict= {}
def get_duplicate_key(key,keys):
    count=0
    for k in keys:
        if key in k:
            count+=1
    return count
def is_hidden(path):
    return bool(os.stat(path).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)
def get_drives():
    drives= []
    value=windll.kernel32.GetLogicalDrives()
    for char in string.ascii_uppercase:
        if( value & 1):
            drives.append(char)
        value>>=1
    return drives
print(get_drives())
def find():
 try:
    winpath = os.environ['WINDIR'].split(':')[0]
    drives =get_drives()
    for drive in drives:
        for root,dirs,files in os.walk(drive + ':\\nsbm\\'):
            for f in files:
                    if is_hidden(os.path.join(root,f))==False:
                        key=os.path.join(root,f).rsplit('\\')[-1]
                        print(key+'_{}'.format(get_duplicate_key(key,file_system_dict.keys())),os.path.join(root,f))
                        file_system_dict.update({key+'_{}'.format(get_duplicate_key(key,file_system_dict.keys())):os.path.join(root,f)})
            for dir in dirs:
                    if is_hidden(os.path.join(root,dir))==False:
                        os.path.join(root,dir)
                        key=os.path.join(root,dir).rsplit('\\')[-1]
                        print(key+'_{}'.format(get_duplicate_key(key,file_system_dict.keys())),os.path.join(root,dir))
                        file_system_dict.update({key+'_{}'.format(get_duplicate_key(key,file_system_dict.keys())):os.path.join(root,dir)})
    return file_system_dict            
 except UnicodeEncodeError:
     pass
with open('dict.txt','w')as f:
    f.write(str(find()))
    f.close

