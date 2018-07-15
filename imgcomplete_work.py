import os,re
        
REGEX_PICS='.*\\.(png|bmp|gif|ico|jpg|jpeg)'
REGEX_SRC='.*<\\s*img\\s+(.*\\s+|)src='
        
def get_folder_items(path,old_path,reg):
    s=os.path.dirname(old_path)
    start=os.path.basename(old_path)
    z=len(start)
    if s=='':
        folder=path
    else:
        folder=os.path.join(path,s)
    s=''
    if folder=='':
        folder='.'
    lsD=[]
    lsF=[]
    for i in os.scandir(folder):
        if not i.name.startswith(start):
            continue
        if i.is_dir():
            lsD.append(i.name) 
        elif re.fullmatch(reg,i.name,re.I):
            lsF.append(i.name)
    lsD.sort()
    lsF.sort()
    for i in lsD:
        s=s+'|'+i+os.path.sep+chr(13)
    for i in lsF:
        s=s+'|'+i+chr(13)
    if('..'+os.path.sep).startswith(start):
        s='|..'+os.path.sep+chr(13)+s
    return [s,z]
    
def imgcomplete_on_complete(ed):
    carets = ed.get_carets()
    if len(carets)>1:
        return False
    x,y,x1,y2=carets[0]
    s=ed.get_text_line(y)[:x]
    file_dir=os.path.dirname(ed.get_filename())
    if re.fullmatch(REGEX_SRC+'"[^"]*',s):
        try:
            for i in range(len(s)-1,-1,-1):
                if s[i]=='"':
                    temp=get_folder_items(file_dir,s[i+1:],REGEX_PICS)
                    ed.complete(temp[0],temp[1],0)
                    return True
        except:
            pass
    if re.fullmatch(REGEX_SRC+"'[^']*",s):
        try:
            for i in range(len(s)-1,-1,-1):
                if s[i]=="'":
                    temp=get_folder_items(file_dir,s[i+1:],REGEX_PICS)
                    ed.complete(temp[0],temp[1],0)
                    return True
        except:
            pass
    return False