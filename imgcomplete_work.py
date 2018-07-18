import os, re
from .imgsize import get_image_size

REGEX_PICS = r'.*\.(png|bmp|gif|ico|jpg|jpeg)'
REGEX_SRC = r'.*<\s*img\s+([^<>]*\s+|)src='
PREFIX_FILE = 'image'
PREFIX_DIR = 'folder'
TAG_LINES = 6 # n lines is read above caret, to support complex tags
IS_UNIX = os.name=='posix'


def get_pic_label(fn):

    res = get_image_size(fn)
    if res:
        return '%dx%d'%res
    else:
        return '?'

def get_folder_items(path,old_path,reg):

    s=os.path.dirname(old_path)
    start=os.path.basename(old_path)
    len1=len(start)
    if s=='':
        folder=path
    else:
        folder=os.path.join(path,s)
    s=''
    if folder=='':
        folder='.'
    if not os.path.isdir(folder):
        return False
    l_dirs=[]
    l_files=[]
    for i in os.scandir(folder):
        if IS_UNIX and i.name.startswith('.'):
            continue
        if not i.name.startswith(start):
            continue
        if i.is_dir():
            l_dirs.append(i.name)
        elif re.fullmatch(reg,i.name,re.I):
            l_files.append((i.name, i.path))
    l_dirs.sort()
    l_files.sort()
    l_dirs.insert(0,'..')
    for i in l_dirs:
        s+=PREFIX_DIR+'|'+i+os.path.sep+chr(13)
    for (s_name, s_path) in l_files:
        s+=PREFIX_FILE+'|'+s_name+'|'+get_pic_label(s_path)+chr(13)
    return [s,len1]

def get_end(s):
    for i in range(len(s)):
        if s[i] in ['"',"'",'<','>','']:
            return i
    return len(s)-1

def imgcomplete_on_complete(ed):

    carets=ed.get_carets()
    if len(carets)!=1:
        return

    fname=ed.get_filename()
    if not fname:
        return
    file_dir=os.path.dirname(fname)
    if not os.path.isdir(file_dir):
        return

    x,y,x1,y1=carets[0]
    s=''
    # add n prev lines, support complex tags
    for i in range(max(0,y-TAG_LINES),y):
        s+=ed.get_text_line(i)
    s_last=ed.get_text_line(y)
    s+=s_last[:x]
    len2=get_end(s_last[x:]) # chars righter than caret

    if re.fullmatch(REGEX_SRC+'"[^"]*',s,re.I):
        for i in range(len(s)-1,-1,-1):
            if s[i]=='"':
                temp=get_folder_items(file_dir,s[i+1:],REGEX_PICS)
                if temp:
                    ed.complete(temp[0],temp[1],len2)
                    return True

    if re.fullmatch(REGEX_SRC+"'[^']*",s,re.I):
        for i in range(len(s)-1,-1,-1):
            if s[i]=="'":
                temp=get_folder_items(file_dir,s[i+1:],REGEX_PICS)
                if temp:
                    ed.complete(temp[0],temp[1],len2)
                    return True
