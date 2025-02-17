from tkinter import *
class LineNumberCanvas(Canvas):
    def __init__(self, master, text_widget, **kwargs):
        super().__init__(master, **kwargs)
        self.text_widget = text_widget
        self.text_widget.bind('<KeyRelease>', self.redraw)
        self.text_widget.bind('<MouseWheel>', self.redraw)
        self.redraw()
    
    def redraw(self, *args):
        '''Redraws the line numbers'''
        self.delete("all")
        i = self.text_widget.index("@0,0")
        while True:
            dline= self.text_widget.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            linenum = str(i).split('.')[0]
            self.create_text(2, y, anchor="nw", text=linenum)
            i = self.text_widget.index(f"{i}+1line")