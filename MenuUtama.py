from tkinter import Tk, Menu
from tkinter.messagebox import showinfo

# root window
root = Tk()
root.geometry('1366x768')
root.title('...:: MENGENALI WAJAH ::...')


# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create the file_menu
file_menu = Menu(
    menubar,
    tearoff=0
)

def tambah_data():
    #pesan = f"Tambah Data Geys"
    #showinfo(title="Tambah",message=pesan)
    import tambah_data

def test_data():
    #pesan = f"Training Data Geys"
    #showinfo(title="Training",message=pesan)
    import test_data

def scan_wajah():
    #pesan = f"Scan Wajah Geys"
    #showinfo(title="Training",message=pesan)
    import scan_wajah

# add menu items to the File menu
file_menu.add_command(label='TAMBAH DATA',command=tambah_data)
file_menu.add_command(label='TEST DATA',command=test_data)
file_menu.add_command(label='SCAN WAJAH',command=scan_wajah)
file_menu.add_separator()

# add Exit menu item
file_menu.add_command(
    label='KELUAR',
    command=root.destroy
)

menubar.add_cascade(
    label="FILE",
    menu=file_menu,
    underline=0
)
# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label='WELCOME')
help_menu.add_command(label='ABOUT ...')

# add the Help menu to the menubar
menubar.add_cascade(
    label="HELP",
    menu=help_menu,
    underline=0
)

root.mainloop()