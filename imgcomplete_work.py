import os,re
        
REGEX_PICS='.*\\.(png|bmp|gif|ico|jpg|jpeg)'
REGEX_SRC='.*<\\s*img\\s+(.*\\s+|)src='
TAG_LINES=6
PREFIX_FILE = 'image'
PREFIX_DIR = 'folder'
        
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
        if not i.name.startswith(start):
            continue
        if i.is_dir():
            l_dirs.append(i.name) 
        elif re.fullmatch(reg,i.name,re.I):
            l_files.append(i.name)
    l_dirs.sort()
    l_files.sort()
    l_dirs.insert(0,'..')
    for i in l_dirs:
        s=s+PREFIX_DIR+'|'+i+os.path.sep+chr(13)
    for i in l_files:
        s=s+PREFIX_FILE+'|'+i+chr(13)
    return [s,len1]
    
def imgcomplete_on_complete(ed):

    carets=ed.get_carets()
    if len(carets)!=1:
        return False

    fname=ed.get_filename()
    if not fname:
        return False
    file_dir=os.path.dirname(fname)
    if not os.path.isdir(file_dir):
        return False
        
    x,y,x1,y1=carets[0]
    s=''
    # add n prev lines, support complex tags
    for i in range(max(0,y-TAG_LINES),y):
        s+=ed.get_text_line(i)
    s+=ed.get_text_line(y)[:x]
    
    if re.fullmatch(REGEX_SRC+'"[^"]*',s,re.I):
        try:
            for i in range(len(s)-1,-1,-1):
                if s[i]=='"':
                    temp=get_folder_items(file_dir,s[i+1:],REGEX_PICS)
                    if temp:
                        ed.complete(temp[0],temp[1],0)
                        return True
        except:
            pass

    if re.fullmatch(REGEX_SRC+"'[^']*",s,re.I):
        try:
            for i in range(len(s)-1,-1,-1):
                if s[i]=="'":
                    temp=get_folder_items(file_dir,s[i+1:],REGEX_PICS)
                    if temp:
                        ed.complete(temp[0],temp[1],0)
                        return True
        except:
            pass

    return False
    