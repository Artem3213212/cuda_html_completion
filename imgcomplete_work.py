import os,re

        
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
    for i in os.scandir(folder):
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
    carets = ed.get_carets()
    if len(carets)>1:
        return False
    x,y,x1,y2=carets[0]
    s=ed.get_text_line(y)[:x]
    file_dir=os.path.dirname(ed.get_filename())
    if re.match('''.*<\\s*img\\s+(.*\\s+|)src="[^"]*''',s):
        try:
            for i in range(len(s)-1,-1,-1):
                if s[i]=='"':
                    temp=get_folder_items(file_dir,s[i+1:],'.*\\.(png|bmp)')
                    ed.complete(temp[0],temp[1],0)
                    return True
        except:
            pass
    return False