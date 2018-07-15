import os,re

def get_dir(s):
    for i in range(len(s)-1,-1,-1):
        if s[i]=='\\'or s[i]=='/' or s[i]=='"':
            return s[:i]
    return ''
        
def get_floader_items(path,old_path,reg):
    z=len(old_path)
    s=get_dir(old_path)
    z=z-len(s)
    if old_path[-z]=='\\'or old_path[-z]=='/' or old_path[-z]=='"':
        z=z-1
    if z==0:
        start=''
    else:
        start=old_path[-z:]
    if s=='':
        flod=path
    else:
        flod=os.path.join(path,s)
    s=''
    if flod=='':
        flod='.'
    for i in os.scandir(flod):
        if not i.name.startswith(start):
            continue
        if i.is_dir():
            s=s+'|'+i.name+os.path.sep+chr(13)
        else:
            if re.match(reg,i.name):
                s=s+'|'+i.name+chr(13)
    if('..'+os.path.sep).startswith(start):
        s='|..'+os.path.sep+chr(13)+s
    if('.'+os.path.sep).startswith(start):
        s='|.'+os.path.sep+chr(13)+s
    return [s,z]
    
def imgcomplete_on_complete(ed):
    x,y,x1,y2=ed.get_carets()[0]
    s=ed.get_text_line(y)[:x]
    file_dir=get_dir(ed.get_filename())
    if re.match('.*<\\s*img\\s+(.*\\s+|)src="[^"]*',s):
        try:
            for i in range(len(s)-1,-1,-1):
                if s[i]=='"':
                    temp=get_floader_items(file_dir,s[i+1:],'.*\\.(png|bmp)')
                    ed.complete(temp[0],temp[1],0)
                    return True
        finally:
            pass
    return False