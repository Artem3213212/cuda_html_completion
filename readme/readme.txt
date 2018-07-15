Plugin for CudaText.
Auto-completion plugin, it handles Ctrl+Space command in HTML/PHP files.
Lexer name can be PHP or any name beginning with "HTML". 

1) It performs auto-completion of CSS class names, while editing HTML "class" and "id" attributes of tags.

For ex:
- If HTML file links to "main.css" and "main.css" defines N class names 
  (for specific tags, or general names for all tags), then HTML editor will show you
  these N names while you call auto-completion after "class=" attrib. 
- Same for "id=" attribs, if css-file contains such id's.

CSS may be linked in HTML in such ways:
- with <link type="text/css" href="main.css" rel="stylesheet">
- with <style type="text/css"> styles here... </style>
- with <style type="text/css"> @import "main.css"; </style>


2) It performs auto-completion of picture file names, when caret is inside <img src="">.
It handles partially typed filenames, and folder (with sub folders) names.


Authors:
  Alexey T. (CudaText)
  Artem Gavrilov (@Artem3213212)
License: MIT
