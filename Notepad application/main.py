import tkinter as tk
from tkinter import filedialog
import tkinter.font as tkfont
class NotedpadApp:
    def __init__(self,root):
        self.root=root
        self.root.title("Simple Notepad")
        self.root.geometry("600x400")
        #DEFAULT FONT STYLE
        self.current_font=tkfont.Font(family="Arial",size=12)
      
        #MENU BAR
        self.menu_bar=tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
      
        #-----File menu (sub menu under menu bar)----
        file_menu=tk.Menu(self.menu_bar,tearoff=0)
        file_menu.add_command(label="Open",command=self.openfd)
        file_menu.add_command(label="Save As",command=self.save)
        file_menu.add_separator()
        file_menu.add_command(label="Exit",command=self.exit_app)
        self.menu_bar.add_cascade(label="File",menu=file_menu)
        #------------EDIT MENU----------------------
        edit_menu=tk.Menu(self.menu_bar,tearoff=0)
        edit_menu.add_command(label="Cut",command=self.cut)
        edit_menu.add_command(label="Copy",command=self.copy)
        edit_menu.add_command(label="Paste",command=self.paste)
        edit_menu.add_separator()
        edit_menu.add_command(label="Clear",command=self.clear)
        self.menu_bar.add_cascade(label="Edit",menu=edit_menu)
        #-----------------FORMAT MENU(FONT SYLES)--------------
        format_menu = tk.Menu(self.menu_bar, tearoff=0)
        font_menu = tk.Menu(format_menu, tearoff=0)
        font_menu.add_command(label="Arial", command=lambda: self.set_font("Arial"))
        font_menu.add_command(label="Courier", command=lambda: self.set_font("Courier"))
        font_menu.add_command(label="Times New Roman", command=lambda: self.set_font("Times New Roman"))
        format_menu.add_cascade(label="Font", menu=font_menu)
        self.menu_bar.add_cascade(label="Format", menu=format_menu)

        #NEW TEXT FRAME TO HOLD BOTH TEXT BOX AND SCROLL BAR
        text_frame=tk.Frame(self.root)
        text_frame.grid(row=0,column=0,sticky="nsew")
        #SCROLL BAR UPSIDE DOWN 
        scrolbar=tk.Scrollbar(text_frame)
        scrolbar.grid(row=0,column=1,sticky="ns")

        #creating text writing area
        self.text_area=tk.Text(text_frame,font=self.current_font,yscrollcommand=scrolbar.set,wrap="word")
        self.text_area.grid(row=0,column=0,sticky="nsew")

        #connect scrollbar to text box area------
        scrolbar.config(command=self.text_area.yview)


        #root grid
        self.root.rowconfigure(0,weight=1)
        self.root.columnconfigure(0,weight=1)
        text_frame.rowconfigure(0,weight=1)
        text_frame.columnconfigure(0,weight=1)
        
        

        #------------------------------------------------------------------------
        #AFTER MENU CREATION USAGE OF BUTTON IS NO LONGER NECESSARY BUT THEIR FUNCTIONS WILL BE USED
        # #creating button frame
        # self.button_frame=tk.Frame(self.root)
        # self.button_frame.grid(row=1,column=0,pady=10)
        # # creating buttons for save clear and exit
        # b1=tk.Button(self.button_frame,text="Save",command=self.save)
        # b2=tk.Button(self.button_frame,text="Clear",command=self.clear)
        # b3=tk.Button(self.button_frame,text="Exit",command=self.exit_app)
        # b4=tk.Button(self.button_frame,text="Open",command=self.openfd)

        # b4.pack(side=tk.LEFT,padx=10)
        # b1.pack(side=tk.LEFT,padx=10)
        # b2.pack(side=tk.LEFT,padx=10)
        # b3.pack(side=tk.LEFT,padx=10)
        #------------------------------------------------------------------------
  
    # FILE METHODS
    def openfd(self):
        file_path=filedialog.askopenfilename(filetypes=[("Text files","*.txt")])
        if file_path:
            with open(file_path,'r') as file:
                content=file.read()
            self.text_area.delete("1.0",tk.END)
            self.text_area.insert("1.0",content)
    

    def save(self):
        file_path=filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text files","*.txt")])
        if file_path:
            with open (file_path,'w')as file:
                file.write(self.text_area.get(1,tk.END))
    
    def clear(self):
        self.text_area.delete(1.0,tk.END)
    
    def exit_app(self):
        self.root.destroy()
    # EDIT METHODS
    def paste(self):
        try:
            cursor_pos=self.text_area.index(tk.INSERT)
            paste_text=self.root.clipboard_get()
            self.text_area.insert(cursor_pos,paste_text)
        except tk.TclError:
            pass  #empty clipboard
    
    def copy(self):
        try:
            selected_text = self.text_area.get("sel.first", "sel.last")
            self.root.clipboard_clear()
            self.root.clipboard_append(selected_text)
        except tk.TclError:
            pass  # No text selected
    
    def cut(self):
        self.copy()
        self.text_area.delete("sel.first","sel.last")
    #FORMAT MENU METHODS
    def set_font(self, font_name):
        self.current_font.config(family=font_name)
        self.text_area.configure(font=self.current_font)

    
# running the app
if __name__=="__main__":
    root=tk.Tk()
    app=NotedpadApp(root)
    root.mainloop()

