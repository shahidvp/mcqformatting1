from tkinter import *
import re
re_str=r"\(?(\d+\))"
q_str=r"(\d+\.)"


def convertText():
    global text_in
    label.delete(1.0,END)
    a=text_in.get().replace("\n"," ")
    op_list=re.findall(re_str,a)
    ac=re.sub(q_str,"\n"+r"\1",a)
    ab=re.sub(re_str,"\n"+r"\1",ac)
    label.insert(1.0,ab)
    label.pack()
    #label.configure(state="disabled")
    
    

root=Tk()
root.title="Text Formatting"

text_in=Entry(root)
text_in.pack()
text_in.focus_set()
label=Text(root)
cb=Button(root,text="Format",command=convertText)
cb.pack(side='bottom')
root.mainloop()
