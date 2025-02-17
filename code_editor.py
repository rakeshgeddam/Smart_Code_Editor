from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
from text_editor_module import LineNumberCanvas
from insert_collection import getClosestErrors

compiler = Tk()
compiler.title('Rakesh\'s Code Editor')
file_path = ''


def auto_indent(event):
    # Get the current line's text
    line = editor.get("insert linestart", "insert")
    # Find the indentation (spaces or tabs)
    indent = ""
    for char in line:
        if char in (" ", "\t"):
            indent += char
        else:
            break
    editor.insert("insert", "\n" + indent)
    return "break"  # Prevent the default newline behavior




def set_file_path(path):
    global file_path
    file_path = path


def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)


def save_as(event=None):
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)


def run(even=None):
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.config(state="normal")
    code_output.delete('1.0', END)

    if process.stdout:
        
        code_output.config(state="disabled")
        code_output.config(state="normal")
        code_output.delete('1.0', END)
        code_output.insert('1.0', output)
        code_output.config(state="disabled")
    if process.stderr:
        code_output.config(state="normal")
        code_output.delete('1.0', END)
        code_output.insert('1.0', error)
        code_output.config(state="disabled")
        error_report.config(state="normal")
        error_report.delete('1.0',END)
        error_report.insert('1.0', str(getClosestErrors(str(error))))
        error_report.config(state="disabled")

menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)
compiler.config(menu=menu_bar)
compiler.bind('<Control-s>',save_as)
compiler.bind('<Control-g>',run)

main_frame = Frame(compiler)
main_frame.pack(fill="both", expand=True)

left_frame = Frame(main_frame)
left_frame.grid(row=0, column=0, sticky="nsew")

right_frame = Frame(main_frame)
right_frame.grid(row=0, column=1, sticky="ns")

main_frame.grid_columnconfigure(0, weight=3)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_rowconfigure(0, weight=1)

editor = Text(left_frame)
editor.pack(fill="both", expand=True)
editor.bind("<Return>", auto_indent)
line_numbers = LineNumberCanvas(left_frame, editor, width=10, bg="lightgrey")
line_numbers.pack(side="left", fill="y")

code_output = Text(left_frame, height=10)
code_output.pack(fill="both", expand=True)
code_output.config(state="disabled")

error_report = Text(right_frame)
error_report.pack(fill="both", expand=True)

compiler.resizable(True, True)

compiler.mainloop()