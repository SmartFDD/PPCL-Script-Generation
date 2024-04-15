import tkinter as tk
from tkinter import messagebox

# Global variables to store form data
panel_name_data = ''
panel_type_data = ''
IP_address_data = ''
panel_location_data=''
drawing_reference_data=''
occ_data =''
fss_data=''
static_data=''
vfds_data=''
chw_data=''
hw_data=''
sa_data=''
ctl_data=''
oaz_data=''
htg_data=''
hc_data=''
clg_data=''
rmt_data=''
rmh_data=''

#Modify File
def modify_file(FCU_FDD_TEMPLATE , OP):
# Read the content of the text file
    with open(FCU_FDD_TEMPLATE, "r") as file:
        lines = file.readlines()

# Modify the specific line with custom text
    lines[7] = "00170	C PANEL NAME - " + panel_name_data +"\n"  
    lines[8] = "00180	C PANEL TYPE - " + panel_type_data +"\n"  
    lines[9] = "00190	C IP ADDRESS - " + IP_address_data +"\n" 

    lines[11] = "00210	C PANEL LOCATION - " + panel_location_data +"\n" 
    lines[12] = "00220	C DRAWING REFERENCES - " + drawing_reference_data +"\n" 

    lines[27] = "00370	DEFINE(OCC," + occ_data + ")"  +"\n"
    lines[29] = "00390	DEFINE(FSS," + fss_data + ")"  +"\n" 
    lines[31] = "00410	DEFINE(STATIC_P" + static_data + ")" +"\n" 
    lines[33] = "00430	DEFINE(VFDS," + vfds_data +")"  +"\n" 
    lines[35] = "00450	DEFINE(CHW,"+ chw_data + ")" +"\n" 
    lines[37] = "00470	DEFINE(HW," + hw_data +")"+"\n" 
    lines[39] = "00490	DEFINE(SA_T," + sa_data + ")"+"\n" 
    lines[41] = "00510	DEFINE(CTL," + ctl_data + ")" +"\n" 
    lines[43] = "00530  DEFINE(OAZ," + oaz_data + ")" +"\n" 
    lines[45] = "00550  DEFINE(HTG," + htg_data + ")" +"\n" 
    lines[47] = "00570  DEFINE(HC," + hc_data +")" + "\n" 
    lines[49] = "00590  DEFINE(CLG," + clg_data + ")" +"\n" 
    lines[51] = "00610  DEFINE(RMT," + rmt_data + ")" +"\n" 
    lines[53] = "00630  DEFINE(RMH,"+ rmh_data + ")" +"\n" 

# Write the modified content back to the text file
    with open(OP, "w") as file:
        file.writelines(lines)


#FORM CREATION
def submit_form():
    global panel_name_data, panel_type_data, IP_address_data, panel_location_data, drawing_reference_data, occ_data, fss_data, static_data, vfds_data, chw_data, hw_data, sa_data, ctl_data, oaz_data, htg_data, hc_data, clg_data, rmt_data, rmh_data
    
    # Retrieve data from form fields
    panel_name_data = panel_name.get()
    panel_type_data = panel_type.get()
    IP_address_data = IP_address.get()
    panel_location_data = panel_location.get()
    drawing_reference_data = drawing_reference.get()
    occ_data = occ.get()
    fss_data= fss.get()
    static_data= static.get()
    vfds_data= vfds.get()
    chw_data= chw.get()
    hw_data= hw.get()
    sa_data= sa.get()
    ctl_data= ctl.get()
    oaz_data= oaz.get()
    htg_data= htg.get()
    hc_data= hc.get()
    clg_data= clg.get()
    rmt_data= rmt.get()
    rmh_data= rmh.get()

def on_enter(event):
    submit_form()

    #Close the window
    root.destroy()

    # Modify the file
    modify_file("FCU FDD TEMPLATE.txt", "OP.txt")



# Create main application window
root = tk.Tk()
root.title("Simple Form")

# Create form elements
label_PanelName = tk.Label(root, text="Panel Name:")
label_PanelName.grid(row=0, column=0, padx=5, pady=5)
panel_name = tk.Entry(root)
panel_name.grid(row=0, column=1, padx=5, pady=5)

label_PanelType = tk.Label(root, text="Panel Type:")
label_PanelType.grid(row=1, column=0, padx=5, pady=5)
panel_type = tk.Entry(root)
panel_type.grid(row=1, column=1, padx=5, pady=5)

label_IPAddress = tk.Label(root, text="IP Address:")
label_IPAddress.grid(row=2, column=0, padx=5, pady=5)
IP_address = tk.Entry(root)
IP_address.grid(row=2, column=1, padx=5, pady=5)

label_location = tk.Label(root, text="Location:")
label_location.grid(row=3, column=0, padx=5, pady=5)
panel_location = tk.Entry(root)
panel_location.grid(row=3, column=1, padx=5, pady=5)

label_reference = tk.Label(root, text="Reference:")
label_reference.grid(row=4, column=0, padx=5, pady=5)
drawing_reference = tk.Entry(root)
drawing_reference.grid(row=4, column=1, padx=5, pady=5)

# OCC
label_OCC = tk.Label(root, text="OCC:")
label_OCC.grid(row=5, column=0, padx=5, pady=5)
occ = tk.Entry(root)
occ.grid(row=5, column=1, padx=5, pady=5)

# FSS
label_fss = tk.Label(root, text="FSS:")
label_fss.grid(row=6, column=0, padx=5, pady=5)
fss = tk.Entry(root)
fss.grid(row=6, column=1, padx=5, pady=5)

# STATIC_P
label_static = tk.Label(root, text="Static:")
label_static.grid(row=7, column=0, padx=5, pady=5)
static = tk.Entry(root)
static.grid(row=7, column=1, padx=5, pady=5)

# VFDS
label_vfds = tk.Label(root, text="VFDS:")
label_vfds.grid(row=8, column=0, padx=5, pady=5)
vfds = tk.Entry(root)
vfds.grid(row=8, column=1, padx=5, pady=5)

# CHW
label_chw = tk.Label(root, text="CHW:")
label_chw.grid(row=9, column=0, padx=5, pady=5)
chw = tk.Entry(root)
chw.grid(row=9, column=1, padx=5, pady=5)

# HW
label_hw = tk.Label(root, text="HW:")
label_hw.grid(row=10, column=0, padx=5, pady=5)
hw = tk.Entry(root)
hw.grid(row=10, column=1, padx=5, pady=5)

# SA_T
label_sa = tk.Label(root, text="SA:")
label_sa.grid(row=11, column=0, padx=5, pady=5)
sa = tk.Entry(root)
sa.grid(row=11, column=1, padx=5, pady=5)

# CTL
label_ctl = tk.Label(root, text="CTL:")
label_ctl.grid(row=12, column=0, padx=5, pady=5)
ctl = tk.Entry(root)
ctl.grid(row=12, column=1, padx=5, pady=5)

# OAZ
label_oaz = tk.Label(root, text="OAZ:")
label_oaz.grid(row=13, column=0, padx=5, pady=5)
oaz = tk.Entry(root)
oaz.grid(row=13, column=1, padx=5, pady=5)

# HTG
label_htg = tk.Label(root, text="HTG:")
label_htg.grid(row=14, column=0, padx=5, pady=5)
htg = tk.Entry(root)
htg.grid(row=14, column=1, padx=5, pady=5)

# HC
label_hc = tk.Label(root, text="HC:")
label_hc.grid(row=15, column=0, padx=5, pady=5)
hc = tk.Entry(root)
hc.grid(row=15, column=1, padx=5, pady=5)

# CLG
label_clg = tk.Label(root, text="CLG:")
label_clg.grid(row=16, column=0, padx=5, pady=5)
clg = tk.Entry(root)
clg.grid(row=16, column=1, padx=5, pady=5)

# RMT
label_rmt= tk.Label(root, text="RMT:")
label_rmt.grid(row=17, column=0, padx=5, pady=5)
rmt = tk.Entry(root)
rmt.grid(row=17, column=1, padx=5, pady=5)

# RMH
label_rmh = tk.Label(root, text="RMH:")
label_rmh.grid(row=18, column=0, padx=5, pady=5)
rmh = tk.Entry(root)
rmh.grid(row=18, column=1, padx=5, pady=5)


submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=19, columnspan=2, padx=5, pady=10)

# Bind the Enter key to submit the form
root.bind('<Return>', on_enter)

# Run the application
root.mainloop()

