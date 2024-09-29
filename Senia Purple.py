# Senia Purple OS
# Senia Purple by MohamedFatma
# Senia Purple v1.0-2024
# ------------------------------------------------------------
# Imports
import time
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
import os
import sys
# Set variable for open file name
global open_status_name
open_status_name = False
global selected
selected = False
# We define a function called Senia Purple and put all the
# code there to access it later on.


def Senia_Purple():
    #  We put the MohamedFatma copyright and and their properties in a function.
    def MohamedFatma_copyright():
        # Print MohamedFatma then down we put multiple(_)
        # or underscores so we mean or
        # symbolize part/s or different part/s then
        # copyright for MohamedFatma then down we put multiple(-) or
        # hyphens so we mean or
        # symbolize part/s or different part/s then
        # Senia Purple by MohamedFatma then lastly Senia Purple version hyphen(-)
        # then year of release(ex: v1.0-2024 for
        # now this version 1.0 for 2024).
        MohamedFatma_senia_purple_copy_senia_purple_version = print("""
        MohamedFatma
        _________________________________
        Copyright © 2024 MohamedFatma. All rights reserved
        --------------------------------------------------------------
        Senia Purple by MohamedFatma
        Senia Purple v1.0-2024
        """)
    MohamedFatma_copyright()
    # We put the code of the setup and so on... in fuction Start_Purple_computer_setup exept copyright.

    def Start_Purple_computer_setup():
        # Ask the user if the user wants to start the setup or no.
        start_senia_purple_setup = input(
            "Start Senia Purple setup (yes, no): ")
        # If yes we will continue and print ok
        if start_senia_purple_setup.strip().lower() == "yes":
            print("ok")
            # We put Purple name process in a function.

            def Name_of_Purple_computer():
                # We ask the user what Senia Purple computer's name
                # would be like and print it without starting or ending
                # with any spaces --- because it is nonsense to have a name
                # starting or ending with spaces --- in the terminal
                # so the user would be aware of what name it is.
                name_of_senia_purple_computer_name = input(
                    "Name your Senia Purple computer: ")
                global senia_purple_computer_name
                senia_purple_computer_name = name_of_senia_purple_computer_name.strip()
                print(senia_purple_computer_name)
                # We ask the user if he/she is sure about what the user wrote.
                are_you_sure_purple_computer_name = input("Are you sure: ")
                # If yes we print ok and continue.
                if are_you_sure_purple_computer_name.strip().lower() == "yes":
                    print("ok")
                # If no we repeat the naming process.
                elif are_you_sure_purple_computer_name.strip().lower() == "no":
                    Name_of_Purple_computer()
                # Add else statement to the are you sure input for name that
                # if the perrson wrote not yes or no or in other words wrote nonsense or any
                # thing else we will exit the process.
                else:
                    exit()
            # Calling the function Name_of_Purple_computer.
            Name_of_Purple_computer()
            # We put Purple password process in a function.

            def Password_of_Purple_computer():
                # We ask the user what Senia Purple computer's password
                # would be like and print it without starting or ending
                # with any spaces --- because it is nonsense to have a password
                # starting or ending with spaces --- in the terminal
                # so the user would be aware of what password it is.
                password_of_senia_purple_computer_password = input(
                    "Next, what is your Purple password: ")
                global senia_purple_computer_password
                senia_purple_computer_password = password_of_senia_purple_computer_password.strip()
                print(senia_purple_computer_password)
                # We ask the user if the user is sure about what has been written.
                are_you_sure_purple_computer_password = input("Are you sure: ")
                # If yes we print ok and continue.
                if are_you_sure_purple_computer_password.strip().lower() == "yes":
                    print("ok")
                # If no we repeat the password making process.
                elif are_you_sure_purple_computer_password.strip().lower() == "no":
                    Password_of_Purple_computer()
                # Add else statement to the are you sure input for password that
                # if the user wrote not yes or no or in other words wrote nonsense or any
                # thing else we will exit the process.
                else:
                    exit()
            # Calling the function Password_of_Purple_computer.
            Password_of_Purple_computer()
            # make a function to start home that the user can interact with Senia Purple

            def Home():
                # we wait 2 seconds
                time.sleep(2)
                # we print the list of operations so the user can use
                print("""Write one of these operations to start:
1- calculator (abv: calc)
2- exit
3- license
4- grafo (text editor)
5- sign out
6- Change Senia name and password (abv: csnp)
7- rasem (drawing editor)
                        """)
                # we define a variable so it holds the operation or in other words to be the operations reciever
                operation = input(">>> ")
                # we define a calculator function that ==> is an operation to use

                def calculator():
                    # print welcome to the calculator
                    print("Welcome to calculator")
                    # we input all the current math operations to start with
                    choose_operation = input(
                        "add, sub, multi, divi, exith [to exit to home]: ")
                    # if the user inputed add then...
                    if choose_operation == "add":
                        # we ask the user how many places for numbers wanted
                        choose_how_many_numbers = int(input("2~5: "))
                        # if the user chose 2 places
                        if choose_how_many_numbers == 2:
                            # we input what is the first number the user will choose
                            first_num = float(input("First number: "))
                            # we input what is the second number the user will choose
                            second_num = float(input("Second number: "))
                            # we print the first and second numbers floats added
                            print(first_num + second_num)
                        elif choose_how_many_numbers == 3:
                            # we input what is the first number the user will choose
                            first_num = float(input("First number: "))
                            # we input what is the second number the user will choose
                            second_num = float(input("Second number: "))
                            # we input what is the third number the user will choose
                            third_num = float(input("Third number: "))
                            # we print the first, second and third floats added
                            print(first_num + second_num + third_num)
                        elif choose_how_many_numbers == 4:
                            # we input what is the first number the user will choose
                            first_num = float(input("First number: "))
                            # we input what is the second number the user will choose
                            second_num = float(input("Second number: "))
                            # we input what is the third number the user will choose
                            third_num = float(input("Third number: "))
                            # we input what is the fourth number the user will choose
                            fourth_num = float(input("Fourth number: "))
                            # we print the first, second, third and fourth floats added
                            print(first_num + second_num +
                                  third_num + fourth_num)
                        elif choose_how_many_numbers == 5:
                            # we input what is the first number the user will choose
                            first_num = float(input("First number: "))
                            # we input what is the second number the user will choose
                            second_num = float(input("Second number: "))
                            # we input what is the third number the user will choose
                            third_num = float(input("Third number: "))
                            # we input what is the fourth number the user will choose
                            fourth_num = float(input("Fourth number: "))
                            # we input what is the fifth number the user will choose
                            fifth_num = float(input("Fifth number: "))
                            # we print the first, second, third, fourth and fifth floats added
                            print(first_num + second_num +
                                  third_num + fourth_num + fifth_num)
                    if choose_operation == "sub":
                        # we ask the user how many places for numbers wanted
                        choose_how_many_numbers = int(input("2~5: "))
                        # if the user chose 2 places
                        if choose_how_many_numbers == 2:
                            # we input what is the first number the user will choose
                            first_num = float(input("First number: "))
                            # we input what is the second number the user will choose
                            second_num = float(input("Second number: "))
                            # we print the first and second numbers floats subtracted
                            print(first_num - second_num)
                        elif choose_how_many_numbers == 3:
                            # we input what is the first number the user will choose
                            first_num = float(input("First number: "))
                            # we input what is the second number the user will choose
                            second_num = float(input("Second number: "))
                            # we input what is the third number the user will choose
                            third_num = float(input("Third number: "))
                            # we print the first, second and third floats subtracted
                            print(first_num - second_num - third_num)
                        elif choose_how_many_numbers == 4:
                            # we input what is the first number the user will choose
                            first_num = float(input("First number: "))
                            # we input what is the second number the user will choose
                            second_num = float(input("Second number: "))
                            # we input what is the third number the user will choose
                            third_num = float(input("Third number: "))
                            # we input what is the fourth number the user will choose
                            fourth_num = float(input("Fourth number: "))
                            # we print the first, second, third and fourth floats subtracted
                            print(first_num - second_num -
                                  third_num - fourth_num)
                        elif choose_how_many_numbers == 5:
                            # we input what is the first number the user will choose
                            first_num = float(input("First number: "))
                            # we input what is the second number the user will choose
                            second_num = float(input("Second number: "))
                            # we input what is the third number the user will choose
                            third_num = float(input("Third number: "))
                            # we input what is the fourth number the user will choose
                            fourth_num = float(input("Fourth number: "))
                            # we input what is the fifth number the user will choose
                            fifth_num = float(input("Fifth number: "))
                            # we print the first, second, third, fourth and fifth floats subtracted
                            print(first_num - second_num -
                                  third_num - fourth_num - fifth_num)
                    if choose_operation == "multi":
                        # we ask the user how many places for numbers wanted
                        choose_how_many_numbers = int(input("2~5: "))
                        # if the user chose 2 places
                        if choose_how_many_numbers == 2:
                            # we input what is the first number the user will choose
                            first_num = float(input("First number: "))
                            # we input what is the second number the user will choose
                            second_num = float(input("Second number: "))
                            # we print the first and second numbers floats multiplication
                            print(first_num * second_num)
                        elif choose_how_many_numbers == 3:
                            # we input what is the first number the user will choose
                            first_num = float(input("First number: "))
                            # we input what is the second number the user will choose
                            second_num = float(input("Second number: "))
                            # we input what is the third number the user will choose
                            third_num = float(input("Third number: "))
                            # we print the first, second and third floats multiplication
                            print(first_num * second_num * third_num)
                        elif choose_how_many_numbers == 4:
                            # we input what is the first number the user will choose
                            first_num = float(input("First number: "))
                            # we input what is the second number the user will choose
                            second_num = float(input("Second number: "))
                            # we input what is the third number the user will choose
                            third_num = float(input("Third number: "))
                            # we input what is the fourth number the user will choose
                            fourth_num = float(input("Fourth number: "))
                            # we print the first, second, third and fourth floats multiplication
                            print(first_num * second_num *
                                  third_num * fourth_num)
                        elif choose_how_many_numbers == 5:
                            # we input what is the first number the user will choose
                            first_num = float(input("First number: "))
                            # we input what is the second number the user will choose
                            second_num = float(input("Second number: "))
                            # we input what is the third number the user will choose
                            third_num = float(input("Third number: "))
                            # we input what is the fourth number the user will choose
                            fourth_num = float(input("Fourth number: "))
                            # we input what is the fifth number the user will choose
                            fifth_num = float(input("Fifth number: "))
                            # we print the first, second, third, fourth and fifth floats multiplication
                            print(first_num * second_num *
                                  third_num * fourth_num * fifth_num)
                    if choose_operation == "divi":
                        # we ask the user how many places for numbers wanted
                        choose_how_many_numbers = int(input("2~5: "))
                        # if the user chose 2 places
                        if choose_how_many_numbers == 2:
                            # we input what is the first number the user will choose
                            first_num = float(input("First number: "))
                            # we input what is the second number the user will choose
                            second_num = float(input("Second number: "))
                            # we print the first and second numbers floats division
                            print(first_num / second_num)
                        elif choose_how_many_numbers == 3:
                            # we input what is the first number the user will choose
                            first_num = float(input("First number: "))
                            # we input what is the second number the user will choose
                            second_num = float(input("Second number: "))
                            # we input what is the third number the user will choose
                            third_num = float(input("Third number: "))
                            # we print the first, second and third floats division
                            print(first_num / second_num / third_num)
                        elif choose_how_many_numbers == 4:
                            # we input what is the first number the user will choose
                            first_num = float(input("First number: "))
                            # we input what is the second number the user will choose
                            second_num = float(input("Second number: "))
                            # we input what is the third number the user will choose
                            third_num = float(input("Third number: "))
                            # we input what is the fourth number the user will choose
                            fourth_num = float(input("Fourth number: "))
                            # we print the first, second, third and fourth floats division
                            print(first_num / second_num /
                                  third_num / fourth_num)
                        elif choose_how_many_numbers == 5:
                            # we input what is the first number the user will choose
                            first_num = float(input("First number: "))
                            # we input what is the second number the user will choose
                            second_num = float(input("Second number: "))
                            # we input what is the third number the user will choose
                            third_num = float(input("Third number: "))
                            # we input what is the fourth number the user will choose
                            fourth_num = float(input("Fourth number: "))
                            # we input what is the fifth number the user will choose
                            fifth_num = float(input("Fifth number: "))
                            # we print the first, second, third, fourth and fifth floats division
                            print(first_num / second_num /
                                  third_num / fourth_num / fifth_num)
                    # if the user inputed exith then...
                    if choose_operation == "exith":
                        # we exit and go home
                        Home()
                # we make a function to exit the OS

                def exitnow():
                    exit()
                # we make grafo function that is Senia's official text editor

                def grafo():
                    root = Tk()
                    root.title('Senia by MohamedFatma - Grafo')
                    root.iconbitmap('')
                    root.geometry("1200x800")
                    # Create New File Function

                    def new_file():
                        # Delete previous text
                        my_text.delete("1.0", END)
                        # Update status bars
                        root.title('New File | Grafo')
                        status_bar.config(text="New File        ")
                        global open_status_name
                        open_status_name = False
                    # Open Files

                    def open_file():
                        # Delete previous text
                        my_text.delete("1.0", END)
                        # Grab Filename
                        text_file = filedialog.askopenfilename(initialdir="C:/Downloads/", title="Open File", filetypes=(
                            ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
                        # Check to see if there is a file name
                        if text_file:
                            # Make filename global so we can access it later
                            global open_status_name
                            open_status_name = text_file
                        # Update Status bars
                        name = text_file
                        status_bar.config(text=f'{name}        ')
                        name = name.replace("C:/Users/USER/Downloads/", "")
                        root.title(f'{name} | Grafo')
                        # Open the file
                        text_file = open(text_file, 'r')
                        stuff = text_file.read()
                        # Add file to textbox
                        my_text.insert(END, stuff)
                        # Close the opened file
                        text_file.close()
                    # Save As File

                    def save_as_file():
                        text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/Downloads/", title="Save File", filetypes=(
                            ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
                        if text_file:
                            # Update Status Bars
                            name = text_file
                            status_bar.config(text=f'Saved: {name}        ')
                            name = name.replace("C:/Users/USER/Downloads/", "")
                            root.title(f'{name} | Grafo')
                            # Save the file
                            text_file = open(text_file, "w")
                            text_file.write(my_text.get(1.0, END))
                            # Close the file
                            text_file.close()
                    # Save file

                    def save_file():
                        global open_status_name
                        if open_status_name:
                            # Save the file
                            text_file = open(open_status_name, "w")
                            text_file.write(my_text.get(1.0, END))
                            # Close the file
                            text_file.close()
                            status_bar.config(
                                text=f'Saved: {open_status_name}        ')
                        else:
                            save_as_file()
                    # Cut text

                    def cut_text(e):
                        global selected
                        # Check to see if keyboard shortcut used
                        if e:
                            selected = root.clipboard_get()
                        else:
                            if my_text.selection_get():
                                # Grab selected text from text box
                                selected = my_text.selection_get()
                                # Delete selected text from text box
                                my_text.delete("sel.first", "sel.last")
                                # Clear the clipboard then append
                                root.clipboard_clear()
                                root.clipboard_append(selected)
                    # Copy text

                    def copy_text(e):
                        global selected
                        # Check to see if we used keyboard shortcuts
                        if e:
                            selected = root.clipboard_get()
                        if my_text.selection_get():
                            # Grab selected text from text box
                            selected = my_text.selection_get()
                            # Clear the clipboard then append
                            root.clipboard_clear()
                            root.clipboard_append(selected)
                    # Paste text

                    def paste_text(e):
                        global selected
                        # Check to see if keyboard shortcut used
                        if e:
                            selected = root.clipboard_get()
                        else:
                            if selected:
                                position = my_text.index(INSERT)
                                my_text.insert(position, selected)
                    # Bold Text

                    def bold_it():
                        # Create our font
                        bold_font = font.Font(my_text, my_text.cget("font"))
                        bold_font.configure(weight="bold")
                        # Configure a tag
                        my_text.tag_configure("bold", font=bold_font)
                        # Define Current tags
                        current_tags = my_text.tag_names("sel.first")
                        # If statment to see if tag has been set
                        if "bold" in current_tags:
                            my_text.tag_remove("bold", "sel.first", "sel.last")
                        else:
                            my_text.tag_add("bold", "sel.first", "sel.last")
                    # Italic Text

                    def italic_it():
                        # Create our font
                        italic_font = font.Font(my_text, my_text.cget("font"))
                        italic_font.configure(slant="italic")
                        # Configure a tag
                        my_text.tag_configure("italic", font=italic_font)
                        # Define Current tags
                        current_tags = my_text.tag_names("sel.first")
                        # If statment to see if tag has been set
                        if "italic" in current_tags:
                            my_text.tag_remove(
                                "italic", "sel.first", "sel.last")
                        else:
                            my_text.tag_add("italic", "sel.first", "sel.last")
                    # Change color

                    def text_color():
                        # Pick a color
                        my_color = colorchooser.askcolor()[1]
                        if my_color:
                            # Create our font
                            color_font = font.Font(
                                my_text, my_text.cget("font"))
                            # Configure a tag
                            my_text.tag_configure(
                                "colored", font=color_font, foreground=my_color)
                            # Define Current tags
                            current_tags = my_text.tag_names("sel.first")
                            # If statment to see if tag has been set
                            if "colored" in current_tags:
                                my_text.tag_remove(
                                    "colored", "sel.first", "sel.last")
                            else:
                                my_text.tag_add(
                                    "colored", "sel.first", "sel.last")
                    # Change background color

                    def bg_color():
                        my_color = colorchooser.askcolor()[1]
                        if my_color:
                            my_text.config(bg=my_color)
                    # Change all Text Color

                    def all_text_color():
                        my_color = colorchooser.askcolor()[1]
                        if my_color:
                            my_text.config(fg=my_color)
                    # Print File Function

                    def print_file():
                        # Grab Filename
                        file_to_print = filedialog.askopenfilename(initialdir="C:/Downloads/", title="Open File", filetypes=(
                            ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
                        if file_to_print:
                            win32api.ShellExecute(
                                0, "print", file_to_print, None, ".", 0)
                    # Select all Text

                    def select_all(e):
                        # Add sel tag to select all text
                        my_text.tag_add("sel", '1.0', 'end')
                    # Clear all Text

                    def clear_all():
                        my_text.delete(1.0, END)
                    # Turn on Dark Mode

                    def dark_on():
                        main_color = "#000000"
                        second_color = "#373737"
                        text_color = "white"
                        root.config(bg=main_color)
                        status_bar.config(bg=main_color, fg=text_color)
                        my_text.config(bg=second_color, fg=text_color)
                        toolbar_frame.config(bg=main_color)
                        # toolbar buttons
                        bold_button.config(bg=second_color, fg=text_color)
                        italic_button.config(bg=second_color, fg=text_color)
                        redo_button.config(bg=second_color, fg=text_color)
                        undo_button.config(bg=second_color, fg=text_color)
                        color_text_button.config(
                            bg=second_color, fg=text_color)
                        # file menu colors
                        file_menu.config(bg=second_color, fg=text_color)
                        edit_menu.config(bg=second_color, fg=text_color)
                        color_menu.config(bg=second_color, fg=text_color)
                        options_menu.config(bg=second_color, fg=text_color)
                    # Turn Off Dark Mode

                    def dark_off():
                        main_color = "SystemButtonFace"
                        second_color = "SystemButtonFace"
                        text_color = "black"
                        root.config(bg=main_color)
                        status_bar.config(bg=main_color, fg=text_color)
                        my_text.config(bg="white", fg=text_color)
                        toolbar_frame.config(bg=main_color)
                        # toolbar buttons
                        bold_button.config(bg=second_color, fg=text_color)
                        italic_button.config(bg=second_color, fg=text_color)
                        redo_button.config(bg=second_color, fg=text_color)
                        undo_button.config(bg=second_color, fg=text_color)
                        color_text_button.config(
                            bg=second_color, fg=text_color)
                        # file menu colors
                        file_menu.config(bg=second_color, fg=text_color)
                        edit_menu.config(bg=second_color, fg=text_color)
                        color_menu.config(bg=second_color, fg=text_color)
                        options_menu.config(bg=second_color, fg=text_color)
                    # Create a toolbar frame
                    toolbar_frame = Frame(root)
                    toolbar_frame.pack(fill=X)
                    # Create Main Frame
                    my_frame = Frame(root)
                    my_frame.pack(pady=5)
                    # Create our Scrollbar For the Text Box
                    text_scroll = Scrollbar(my_frame)
                    text_scroll.pack(side=RIGHT, fill=Y)
                    # Horizontal Scrollbar
                    hor_scroll = Scrollbar(my_frame, orient='horizontal')
                    hor_scroll.pack(side=BOTTOM, fill=X)
                    # Create Text UI
                    my_text = Text(my_frame, width=97, height=25, font=("Cascadia Mono", 16), selectbackground="grey",
                                   selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=hor_scroll.set)
                    my_text.pack()
                    # Configure our Scrollbar
                    text_scroll.config(command=my_text.yview)
                    hor_scroll.config(command=my_text.xview)
                    # Create Menu
                    my_menu = Menu(root)
                    root.config(menu=my_menu)
                    # Add File Menu
                    file_menu = Menu(my_menu, tearoff=False)
                    my_menu.add_cascade(label="File", menu=file_menu)
                    file_menu.add_command(label="New", command=new_file)
                    file_menu.add_command(label="Open", command=open_file)
                    file_menu.add_command(label="Save", command=save_file)
                    file_menu.add_command(
                        label="Save As", command=save_as_file)
                    file_menu.add_separator()
                    file_menu.add_command(
                        label="Print File", command=print_file)
                    file_menu.add_separator()
                    file_menu.add_command(label="Exit", command=root.quit)
                    # Add Edit Menu
                    edit_menu = Menu(my_menu, tearoff=False)
                    my_menu.add_cascade(label="Edit", menu=edit_menu)
                    edit_menu.add_command(label="Cut", command=lambda: cut_text(
                        False), accelerator="(Ctrl+x)")
                    edit_menu.add_command(label="Copy", command=lambda: copy_text(
                        False), accelerator="(Ctrl+c)")
                    edit_menu.add_command(label="Paste        ", command=lambda: paste_text(
                        False), accelerator="(Ctrl+v)")
                    edit_menu.add_separator()
                    edit_menu.add_command(
                        label="Undo", command=my_text.edit_undo, accelerator="(Ctrl+z)")
                    edit_menu.add_command(
                        label="Redo", command=my_text.edit_redo, accelerator="(Ctrl+y)")
                    edit_menu.add_separator()
                    edit_menu.add_command(label="Select All", command=lambda: select_all(
                        True), accelerator="(Ctrl+a)")
                    edit_menu.add_command(
                        label="CLear", command=clear_all, accelerator="(Ctrl+y)")
                    # Add Color Menu
                    color_menu = Menu(my_menu, tearoff=False)
                    my_menu.add_cascade(label="Colors", menu=color_menu)
                    color_menu.add_command(
                        label="Selected Text", command=text_color)
                    color_menu.add_command(
                        label="All Text", command=all_text_color)
                    color_menu.add_command(
                        label="Background", command=bg_color)
                    # Add Options Menu
                    options_menu = Menu(my_menu, tearoff=False)
                    my_menu.add_cascade(label="Options", menu=options_menu)
                    options_menu.add_command(
                        label="Dark Mode On", command=dark_on)
                    options_menu.add_command(
                        label="Dark Mode Off", command=dark_off)
                    # Add Status Bar To Bottom Of Grafo
                    status_bar = Label(root, text='Ready        ', anchor=E)
                    status_bar.pack(fill=X, side=BOTTOM, ipady=15)
                    # Edit Bindings
                    root.bind('<Control-Key-x>', cut_text)
                    root.bind('<Control-Key-c>', copy_text)
                    root.bind('<Control-Key-v>', paste_text)
                    # Select Binding
                    root.bind('<Control-A>', select_all)
                    root.bind('<Control-a>', select_all)
                    # Create Buttons
                    # Bold button
                    bold_button = Button(
                        toolbar_frame, text="Bold", command=bold_it)
                    bold_button.grid(row=0, column=0, sticky=W, padx=5)
                    # Italic Button
                    italic_button = Button(
                        toolbar_frame, text="Italic", command=italic_it)
                    italic_button.grid(row=0, column=1, padx=5)
                    # Undo/Redo Button
                    undo_button = Button(
                        toolbar_frame, text="Undo", command=my_text.edit_undo)
                    undo_button.grid(row=0, column=2, padx=5)
                    redo_button = Button(
                        toolbar_frame, text="Redo", command=my_text.edit_redo)
                    redo_button.grid(row=0, column=3, padx=5)
                    # Text Color
                    color_text_button = Button(
                        toolbar_frame, text="Text Color", command=text_color)
                    color_text_button.grid(row=0, column=4, padx=5)
                    root.mainloop()
                # we make rasem function that is Senia's official drawing editor

                def rasem():
                    pass
                # if the user wrote grafo
                if operation == "grafo":
                    # call the function to start the grafo:
                    grafo()
                    # Then go home after finishing
                    Home()
                # if the user wrote rasem
                if operation == "rasem":
                    # we call the function to start rasem
                    rasem()
                    # Then go home after finishing
                    Home()
                # if the user wrote exit
                if operation == "exit":
                    # we print that we are exiting right now
                    print("exiting...")
                    # call the function to exit
                    exitnow()
                # if the user wrote calculator
                if operation == "calc":
                    # call the function to start the calculator
                    calculator()
                    # Then go home after finishing
                    Home()
                # if the user wrote license
                if operation == "license":
                    # we print the license for the user
                    print(f"""
        licensed Senia Purple OS for the user {senia_purple_computer_name} by MohamedFatma
        _________________________________
        Copyright © 2024 MohamedFatma. All rights reserved
        --------------------------------------------------------------
        Senia Purple by MohamedFatma
        Senia Purple v1.0-2024""")
                    # Then go home after finishing
                    Home()
                    # if the user wrote sign out
                if operation == "sign out":
                    # we re-ask the user if is sure about what was written
                    are_you_sure_to_sign_out = input(
                        "Are you sure about signing out: ")
                    # if the user said yes
                    if are_you_sure_to_sign_out.lower().strip() == "yes":
                        # we ask the user if then we exit the user or we start the setup so we change the user to another one or something else
                        are_you_sure_to_sign_out_and_exit = input(
                            "Do you want to exit, [or to come back to the signing part] (yes / no): ")
                        # if yes, then exit
                        if are_you_sure_to_sign_out_and_exit == "yes":
                            # exit after the user said yes
                            exitnow()
                        # if no, then repeat the setup all again
                        elif are_you_sure_to_sign_out_and_exit == "no":
                            Senia_Purple()
                    # if the user said no
                    elif are_you_sure_to_sign_out == "no":
                        # we move the user to home again
                        Home()
                if operation == "csnp":
                    def sign_in_verification_for_news():
                        # we wait 0.5 seconds
                        time.sleep(0.5)
                        # then we print that the user must sign in to verify
                        print(
                            f"Sign in to verify {senia_purple_computer_name}")
                        # we wait 1 second
                        time.sleep(1)
                        # So we define a variable so we can retake and use it again for the password
                        username_verify = input("Password: ")
                        # then we check if the user entered the password correct
                        if username_verify == senia_purple_computer_password:
                            # print that success happened
                            print("Verification Success!")

                        # if not we repeat the operation
                        else:
                            # print that failure happened
                            print("Verification Failed!")
                            # repeat
                            sign_in_verification_for_news()
                    sign_in_verification_for_news()

                    def new_name_and_password():
                        your_new_name = input("New name: ")
                        print(your_new_name)
                        your_new_password = input("New password: ")
                        print(your_new_password)
                        global senia_purple_computer_name
                        senia_purple_computer_name = your_new_name
                        global senia_purple_computer_password
                        senia_purple_computer_password = your_new_password
                        Home()
                    new_name_and_password()
            # We put sign_in_verification to handle the verification of the password the user wrote

            def sign_in_verification():
                # we wait 0.5 seconds
                time.sleep(0.5)
                # then we print that the user must sign in to verify
                print(f"Sign in to verify {senia_purple_computer_name}")
                # we wait 1 second
                time.sleep(1)
                # So we define a variable so we can retake and use it again for the password
                username_verify = input("Password: ")
                # then we check if the user entered the password correct
                if username_verify == senia_purple_computer_password:
                    # print that success happened
                    print("Verification Success!")
                    # go home
                    Home()
                # if not we repeat the operation
                else:
                    # print that failure happened
                    print("Verification Failed!")
                    # repeat
                    sign_in_verification()
            # Calling the Function
            sign_in_verification()
        # If no then we exit the setup process.
        elif start_senia_purple_setup.strip().lower() == "no":
            exit()
        #   else if the user writes nonsense or misunderstood
        #   word or keys or numbers ask if the user wants to
        #   restart the process if yes we restart if no we
        #   exit.
        else:
            # we print we didn't understand what was written
            print("Didn't understand")
            # we ask if the user wants to reapeat
            repeat_senia_purple_setup = input("Want to repeat: ")
            # if yes we repeat
            if repeat_senia_purple_setup.strip().lower() == "yes":
                Senia_Purple()
            # if no we exit
            else:
                exit()
    # Calling the function Start_Purple_computer_setup.
    Start_Purple_computer_setup()


# Calling the function Senia_Purple.
Senia_Purple()
