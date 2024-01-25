import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser , filedialog , messagebox
import os
from tkinter import scrolledtext
import speech_recognition as sr
import pyttsx3
import wikipedia


main_application =tk.Tk()
main_application.geometry('1200x800')
main_application.title('NazarEditor')

######################################### Main Menu ##########################################

main_menu =tk.Menu()

##File Icon########
new_icon = tk.PhotoImage(file='icon2/new.png')
open_icon = tk.PhotoImage(file='icon2/open.png')
save_icon = tk.PhotoImage(file='icon2/save.png')
save_as_icon = tk.PhotoImage(file='icon2/save_as.png')
exit_icon = tk.PhotoImage(file='icon2/exit.png')
#File menu#########<<<<<<<<<<<

file =tk.Menu(main_menu, tearoff=False)

###Ai Menu####<<<<<<<<<<<<<<<<
master_ai = tk.Menu(main_menu, tearoff=False)

#edit Portion of menu######<<<<<<<<
edit =tk.Menu(main_menu, tearoff=False)
######Edit menu icon
copy_icon = tk.PhotoImage(file='icon2/copy.png')
cut_icon = tk.PhotoImage(file='icon2/cut.png')
past_icon = tk.PhotoImage(file='icon2/paste.png')
clear_all_icon = tk.PhotoImage(file='icon2/clear_all.png')
find_icon = tk.PhotoImage(file='icon2/find.png')


#View Check button<<<<<<<<<
view=tk.Menu(main_menu, tearoff=False)

toolbar_icon = tk.PhotoImage(file='icon2/tool_bar.png')
statusbar_icon = tk.PhotoImage(file='icon2/status_bar.png')

###Color_icon########

light_default_icon = tk.PhotoImage(file='icon2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icon2/light_plus.png')
dark_icon = tk.PhotoImage(file='icon2/dark.png')
red_icon = tk.PhotoImage(file='icon2/red.png')
monokai_icon = tk.PhotoImage(file='icon2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icon2/night_blue.png')

#########color theme##
color_theme =tk.Menu(main_menu, tearoff=False)
theme_choice =tk.StringVar()
color_icon = (light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)

color_dict = {
    'Light_default' : ('#000000' , '#ffffff'),
    'Light_plus'  : ('#474747' , '#e0e0e0'),
    'Dark'  :  ('#c4c4c4' ,  '#2d2d2d'),
    'Red'  : ('#2d2d2d' , '#ffe8e8'),
    'Monokai' :  ('#d3b774' ,'#474747'),
    'Night_blue' : ('#ededed' ,'#6b9dc2')
}

#cascade
main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Color Theme',menu=color_theme)
main_menu.add_cascade(label='Master Ai',menu=master_ai)

#------------------------------------->>>End Main Menu <<<----------------------------------
######################################### Tool bar ##########################################

######Tool_bar icons

bold_icon =tk.PhotoImage(file='icon2/bold.png')
italic_icon =tk.PhotoImage(file='icon2/italic.png')
underline_icon =tk.PhotoImage(file='icon2/underline.png')
font_color_icon =tk.PhotoImage(file='icon2/font_color.png')
align_left_icon =tk.PhotoImage(file='icon2/align_left.png')
align_center_icon =tk.PhotoImage(file='icon2/align_center.png')
align_right_icon =tk.PhotoImage(file='icon2/align_right.png')

######Write values

tool_bar =ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)

font_tuple =tk.font.families()
font_family = tk.StringVar()
font_box =ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0 , column=0, padx=5)

#Button for Letter size
size_var =tk.IntVar()
font_size =ttk.Combobox(tool_bar, width=14, textvariable=size_var, state='readonly')
font_size['values'] =tuple(range(8,92))
font_size.current(4)
font_size.grid(row=0 ,column=1,padx=5)

#bold_button
bold_btn = tk.Button(tool_bar , text='Bold',image=bold_icon)
bold_btn.grid(row=0 , column=2 , padx=5)


##Italic Button
italic_btn =tk.Button(tool_bar , text='Italic',image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

#underline_button
underline_btn = tk.Button(tool_bar , text='underline',image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)

#font_color_button
font_color_btn = tk.Button(tool_bar , text='Color',image=font_color_icon)
font_color_btn.grid(row=0, column=5, padx=5)


##Align button

align_left_btn = ttk.Button(tool_bar , text='Align_Left',image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

##align center
align_center_btn = ttk.Button(tool_bar , text='Align_Center',image=align_center_icon)
align_center_btn.grid(row=0 , column=7 ,padx=5)

##align right
align_right_btn = ttk.Button(tool_bar , text='Align_Right',image=align_right_icon)
align_right_btn.grid(row=0 , column=8 ,padx=5)



#------------------------------------->>>End Tool bar <<<---------------------------------->>>>>>>>>>>>

######################################### Text editor ##########################################

text_editor = tk.Text(main_application)
text_editor.config(wrap='word' ,relief=tk.FLAT)

scroll_bar =tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT ,fill=tk.Y)
text_editor.pack(fill=tk.BOTH ,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

#font_family and font size functinality

current_font_family ='Arial'
current_font_size =12

def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))
    
    
def change_fontsize(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))
    
    
font_box.bind("<<ComboboxSelected>>" ,change_font)
font_size.bind("<<ComboboxSelected>>" ,change_fontsize)


##button Functinality

###Bold Button Functinality
def change_bold():
    text_property =tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] =='normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] =='bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

bold_btn.configure(command=change_bold)

#italic Button Functinality
def change_italic():
    text_property =tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] =='roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] =='italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'roman'))

italic_btn.configure(command=change_italic)

#underline Button Functinality
def change_underline():
    text_property =tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

underline_btn.configure(command=change_underline)

#font_color_Functinality
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
    
    
font_color_btn.configure(command=change_font_color)

###Left algin button
def align_left():
    text_content = text_editor.get(1.0 , 'end')
    text_editor.tag_config('left' ,justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT ,text_content, 'left')
align_left_btn.configure(command=align_left)


###center algin button
def align_center():
    text_content = text_editor.get(1.0 , 'end')
    text_editor.tag_config('center' ,justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT ,text_content, 'center')
align_center_btn.configure(command=align_center)

###Left algin button
def align_right():
    text_content = text_editor.get(1.0 , 'end')
    text_editor.tag_config('right' ,justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT ,text_content, 'right')
align_right_btn.configure(command=align_right)

text_editor.configure(font=('Arial',12))
#------------------------------------->>>End Text Editor <<<----------------------------------


######################################### Main status bar ##########################################

status_bar =ttk.Label(main_application ,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed=False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words =len(text_editor.get(1.0, 'end-1c').split())
        characters =len(text_editor.get(1.0, 'end-1c'))       #.replace' ' , ''  to not count space
        status_bar.config(text=f'words : {words} characters : {characters}')
    text_editor.edit_modified(False)
    
    
text_editor.bind('<<Modified>>', changed)

#------------------------------------->>>End  status bar <<<----------------------------------

###_____________________________________ Ai  enter gate Function <<< ------
engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)
# print(voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def ai_func(event=None):



    def ai_func_text():
    #to input our voice
        r =sr.Recognizer()
        with sr.Microphone() as source:
            speak("Listening ....!")
            r.pause_threshold = 1
            audio =r.listen(source)
        try:
            speak("Recognizing ----")
            text = r.recognize_google(audio,language='en_in')
            speak(f"User said : {text}\n")
        
        except Exception as e:
            speak(e)
            speak("Say that again please ...")
        
            return "None"
        return text
    while True:
        text = ai_func_text().lower()

    def  text_func2 ():
        text_editor_Var = tk.StringVar()
        text_editor_Var = text.get()
        text_editor.insert(text_editor_Var)


        if 'wikipedia' in text :
            speak('Searching wikipedia ....')
            text =text.replace("wikipedia" , "")
            results =wikipedia.summary(text,sentences=5)
            speak('According to wikepidia')
            print(results)
            speak(results)
        
    def results_Var():
        results_Var =results.get()
        results_Var = tk.StringVar_Var()
        text_editor.insert(results_Var)
        speak("Sir we have copy the text into editor")
        # else:
        #     speak("say that again")
        
    find_ai = tk.Toplevel()
    find_ai.geometry('450x250+500+200')
    find_ai.resizable(0,0)

###Frame
    find_audio =ttk.LabelFrame(find_ai, text= 'Converet audio to text')
    find_audio.pack(pady=20) 
###label
    ai_find_label =ttk.Label(find_audio, text='Convert :')

####Entry >>>>
    ai_input = ttk.Entry(find_audio, width=40)
##buttns
    ai_find_button =ttk.Button(find_audio,text='Press and say',command= ai_func_text)
### Label grid   
    ai_find_label.grid(row=0,column=0,padx=4,pady=4)

###entry grid>>>>>>>
    ai_input.grid(row=0,column=1,padx=4,pady=4)

###button grid>>>>>>>
    ai_find_button.grid(row=2,column=0,padx=8,pady=4)

    find_ai.mainloop()

master_ai.add_command(label="Ai" ,compound=tk.LEFT ,accelerator='Ctrl+ALT+A',command=ai_func)

########################################  Ai functionaltiy  Ends <<<<  -------------------



######################################### Main Menu functinality ##########################################
#variable
url = ''

######file functinality #####
def new_file(event=None):
    global url
    url =''
    text_editor.delete(1.0,tk.END)

file.add_command(label="New", image =new_icon ,compound=tk.LEFT ,accelerator='Ctrl+N', command=new_file)


#####Open >>>>>>
def open_file(event=None):
    global url
    url =filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File' , filetypes=(('Text file','*.txt'),('Photoimage', '*png'),('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))
    

file.add_command(label="open", image=open_icon ,compound=tk.LEFT ,accelerator='Ctrl+O' ,command=open_file)


##Save >>>



def save_file(event=None):
    global url
    try:
        if url:
            content =str(text_editor.get(1.0,tk.END))
            with open(url, 'w' ,encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode= 'w',defaultextension='.txt',filetypes=(('Text file','*.txt'),('Photoimage', '*png'),('All files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return
    
    
file.add_command(label="Save",image=save_icon ,compound=tk.LEFT ,accelerator='Ctrl+S', command=save_file)

###save file 
def save_as_file(event=None):
    global url
    try:
        content =str(text_editor.get(1.0,tk.END))
        url = filedialog.asksaveasfile(mode= 'w',defaultextension='.txt',filetypes=(('Text file','*.txt'),('Photoimage', '*png'),('All files', '*.*')))
        content = text_editor.get(1.0, tk.END)
        url.write(content)
        url.close()
    except:
        return
file.add_command(label="Save_as",image=save_as_icon ,compound=tk.LEFT ,accelerator='Ctrl+Alt+S',command=save_as_file)

##Exit >>>>>>>>>>>

def exit_func(event=None):
    global url
    try:
        if text_changed:
            mbox=messagebox.askyesnocancel('Warning' ,'Do you want to save your File !!!')
            if mbox is True:
                if url:
                    content= str(text_editor.get(1.0,tk.END))
                    with open(url, 'w' ,encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    url = filedialog.asksaveasfile(mode= 'w',defaultextension='.txt',filetypes=(('Text file','*.txt'),('Photoimage', '*png'),('All files', '*.*')))
                    content = text_editor.get(1.0, tk.END)
                    url.write(content)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return
    
file.add_command(label="Exit", image=exit_icon ,compound=tk.LEFT ,accelerator='Ctrl+Q',command=exit_func) 

########Edit Commands
edit.add_command(label="Copy",image=copy_icon ,compound=tk.LEFT ,accelerator='Ctrl+C',command=lambda:text_editor.event_generate("<Control c>")) 
edit.add_command(label="Past",image=past_icon ,compound=tk.LEFT ,accelerator='Ctrl+v',command=lambda:text_editor.event_generate("<Control v>")) 
edit.add_command(label="Cut", image=cut_icon,compound=tk.LEFT ,accelerator='Ctrl+X',command=lambda:text_editor.event_generate("<Control x>")) 
edit.add_command(label="Clear_all", image=clear_all_icon,compound=tk.LEFT ,accelerator='Ctrl+Backspace',command=lambda:text_editor.delete(1.0,tk.END)) 
#######Find Functionality
def find_func(event=None):
    
    
    def find():
        word =find_input.get()
        text_editor.tag_remove('match' ,'1.0',tk.END)
        matches = 0
        if word:
            start_pos ='1.0'
            while True:
                start_pos =text_editor.search(word, start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match',foreground='red',background='green')
                
    def replace():
        word =find_input.get()
        replace_text= replace_input.get()
        content =text_editor.get(1.0, tk.END)
        new_content = content.replace(word,replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)
        
    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.resizable(0,0)
    
####Frame >>>>>
    find_frame =ttk.LabelFrame(find_dialogue, text= 'Find/Replace')
    find_frame.pack(pady=20)
    
####Labels >>>>>>>
    text_find_label =ttk.Label(find_frame, text='Find :')
    text_replace_label =ttk.Label(find_frame ,text='Replace')
    
####Entry >>>>
    find_input = ttk.Entry(find_frame, width=30)
    replace_input =ttk.Entry(find_frame ,width=30)
    
###button>>>
    find_button =ttk.Button(find_frame,text='Find',command= find)
    replace_button=ttk.Button(find_frame,text='Replace',command=replace)
    
###label grid>>>>
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=1,column=0,padx=4,pady=4)
    
###entry grid>>>>>>>
    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input.grid(row=1,column=1,padx=4,pady=4)
    
###button grid>>>>>>>
    find_button.grid(row=2,column=0,padx=8,pady=4)
    replace_button.grid(row=2,column=1,padx=8,pady=4)
    
    
    
    find_dialogue.mainloop()

edit.add_command(label="Find",image=find_icon ,compound=tk.LEFT ,accelerator='Ctrl+F',command=find_func)


#########views Buttons####

show_status_bar =tk.BooleanVar()
show_status_bar.set(True)       
show_tool_bar =tk.BooleanVar()
show_tool_bar.set(True)


def hide_tool_bar():
    global show_tool_bar
    if show_tool_bar:
        tool_bar.pack_forget()
        show_tool_bar =False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_tool_bar =True
        

def hide_status_bar():
    global show_status_bar
    if show_status_bar:
        status_bar.pack_forget()
        show_status_bar =False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_status_bar =True
        
view.add_checkbutton(label='Tool bar',image=toolbar_icon,onvalue=True,offvalue=0,variable=show_tool_bar,compound=tk.LEFT,command=hide_tool_bar)
view.add_checkbutton(label='Status bar',image=statusbar_icon,onvalue=1,offvalue=False,variable=show_status_bar,compound=tk.LEFT,command=hide_status_bar)

########Color theme Commands######

def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple =color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)
    
count =0
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_icon[count],variable=theme_choice,compound=tk.LEFT ,command=change_theme)
    count +=1
    
#------------------------------------->>>End Main functinality <<<----------------------------------

main_application.config(menu=main_menu)

###bind shortcut keys
main_application.bind("<Control-n>",new_file)
main_application.bind("<Control-o>",open_file)
main_application.bind("<Control-s>",save_file)
main_application.bind("<Control-Alt-s>",save_as_file)
main_application.bind("<Control-q>",exit_func)
main_application.bind("<Control-f>",find_func)






main_application.mainloop()