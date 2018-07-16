Plugin for CudaText.
Auto-completion plugin, it handles Ctrl+Space command in HTML/PHP files.
Lexer name can be PHP or any name beginning with "HTML". 

1) Auto-completion of CSS class names, while editing HTML "class" and "id" attributes of tags.

Examples:
- If HTML file links to "main.css" and "main.css" defines n class names 
  (for specific tags, or general names for all tags), then HTML editor will show
  these n names while you call auto-completion after "class" attrib. 
  <table class="|" >
- Same for "id" attribs, if css-file contains such id's.
  <div id="|">

CSS may be linked in HTML in such ways:
- with <link type="text/css" href="main.css" rel="stylesheet">
- with <style type="text/css"> styles here... </style>
- with <style type="text/css"> @import "main.css"; </style>


2) Auto-completion of picture file names, when caret is inside "src" value:
<img src="|">.
It handles partially typed filenames, and folder (with sub folders) names.
Supported file extensions: png, gif, jpg, jpeg, ico, bmp.


Authors:
  Alexey T. (CudaText)
  Artem Gavrilov (@Artem3213212)
License: MIT
