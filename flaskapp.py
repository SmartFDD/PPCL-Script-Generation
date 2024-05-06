from flask import Flask, render_template, request, send_file, make_response, abort
from tkinter import messagebox
from flask import send_file, session
from io import StringIO
import os

# Global variables to store form data
panel_name_data = ''
panel_type_data = ''
IP_address_data = ''
panel_location_data=''
drawing_reference_data=''
rev_data=''
date_data=''
author_data=''
comments_data=''
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
phw_data=''
ph_data=''
phs_data=''
sas_data=''
sps_data=''
oafl_data=''
oaflsp_data=''
ra_data=''
ma_data=''
bldg_num_data=''
template_data=''
unit_data=''
rev2=''
date2=''
author2 =''
comments2 =''
rev3=''
date3=''
author3 =''
comments3 =''

app = Flask(__name__)
app.secret_key = 'your_secret_key'


# Dictionary to map file names to their corresponding paths
file_paths = {
    'filename1': 'OP.txt',
    'filename2': 'OP2.txt',
    'filename3': 'OP3.txt',
    'filename4': 'OP4.txt'
}



# building data = number _ template _ unit

def modify_file1(rev2, date2, author2, comments2, rev3, date3, author3, comments3, unit_data , bldg_num_data, panel_name_data, panel_type_data, IP_address_data, panel_location_data, drawing_reference_data, rev_data, date_data, author_data, comments_data, occ_data, fss_data, static_data, vfds_data, chw_data, hw_data, sa_data, ctl_data, oaz_data, htg_data, hc_data, clg_data, rmt_data, rmh_data):
 

# Read the content of the text file
    with open("FCU FDD TEMPLATE.TXT", "r") as file:
        lines = file.readlines()

# Modify the specific line with custom text

    lines[2] = "00120	C *********************FAN COIL UNIT ["+unit_data+"] SMART FDD***********************************"+"\n"
    lines[7] = "00170	C PANEL NAME - " + panel_name_data +"\n"  
    lines[8] = "00180	C PANEL TYPE - " + panel_type_data +"\n"  
    lines[9] = "00190	C IP ADDRESS - " + IP_address_data +"\n" 

    lines[11] = "00210	C PANEL LOCATION - " + panel_location_data +"\n" 
    lines[12] = "00220	C DRAWING REFERENCES - " + drawing_reference_data +"\n" 

    lines[14] = "00240	C	REV 	DATE			AUTHOR			COMMENTS"+"\n"
    lines[15] = "00250	C       "+rev_data+"       "+date_data+"                       "+author_data+"                       "+comments_data+"\n"
    lines[16] = "00260	C       "+rev2+"       "+date2+"                       "+author2+"                       "+comments2+"\n"
    lines[17] = "00270	C       "+rev3+"       "+date3+"                       "+author3+"                       "+comments3+"\n"
    lines[27] = "00370	DEFINE(OCC," + occ_data + ")"  +"\n"
    lines[29] = "00390	DEFINE(FSS," + fss_data + ")"  +"\n" 
    lines[31] = "00410	DEFINE(STATIC_P," + static_data + ")" +"\n" 
    lines[33] = "00430	DEFINE(VFDS," + vfds_data +")"  +"\n" 
    lines[35] = "00450	DEFINE(CHW,"+ chw_data + ")" +"\n" 
    lines[37] = "00470	DEFINE(HW," + hw_data +")"+"\n" 
    lines[39] = "00490	DEFINE(SA_T," + sa_data + ")"+"\n" 
    lines[41] = "00510	DEFINE(CTL," + ctl_data + ")" +"\n" 
    lines[43] = "00530   DEFINE(OAZ," + oaz_data + ")" +"\n" 
    lines[45] = "00550   DEFINE(HTG," + htg_data + ")" +"\n" 
    lines[47] = "00570   DEFINE(HC," + hc_data +")" + "\n" 
    lines[49] = "00590   DEFINE(CLG," + clg_data + ")" +"\n" 
    lines[51] = "00610   DEFINE(RMT," + rmt_data + ")" +"\n" 
    lines[53] = "00630   DEFINE(RMH,"+ rmh_data + ")" +"\n" 
    lines[73] = "00810   DEFINE(A," + bldg_num_data +"_"+unit_data+")" +"\n"


# Write the modified content back to the text file
    with open("OP.txt", "w") as file:
        file.writelines(lines)


def modify_file2(rev2, date2, author2, comments2, rev3, date3, author3, comments3, unit_data , bldg_num_data, panel_name_data, panel_type_data, IP_address_data, panel_location_data, drawing_reference_data, rev_data, date_data, author_data, comments_data, occ_data, fss_data, static_data, vfds_data, chw_data, phw_data, sa_data, ph_data, oaz_data, phs_data, sas_data, sps_data, oafl_data, oaflsp_data):

# Read the content of the text file
    with open("AHU100OA_TEMPLATE.txt", "r") as file:
        lines = file.readlines()

# Modify the specific line with custom text

    lines[2] = "00120     C *********************AIR HANDLER ["+unit_data+"] SMART FDD***********************************"+"\n"
    lines[7] = "00170     C PANEL NAME - " + panel_name_data +"\n"  
    lines[8] = "00180	  C PANEL TYPE - " + panel_type_data +"\n"  
    lines[9] = "00190	  C IP ADDRESS - " + IP_address_data +"\n" 

    lines[11] = "00210     C PANEL LOCATION- " + panel_location_data +"\n" 
    lines[12] = "00220	  C DRAWING REFERENCES - " + drawing_reference_data +"\n" 

    lines[14] = "00240	  C	  REV 	  DATE			  AUTHOR			  COMMENTS"+"\n"
    lines[15] = "00250	  C       "+rev_data+"       "+date_data+"                       "+author_data+"                               "+comments_data+"\n"
    lines[16] = "00260	  C       "+rev2+"       "+date2+"                       "+author2+"                               "+comments2+"\n"
    lines[17] = "00270	  C       "+rev3+"       "+date3+"                       "+author3+"                               "+comments3+"\n"
    
    lines[27] = "00370     DEFINE(OCC," + occ_data + ")"  +"\n"
    lines[29] = "00390	  DEFINE(FSS," + fss_data + ")"  +"\n" 
    lines[31] = "00410	  DEFINE(STATIC_P" + static_data + ")" +"\n" 
    lines[33] = "00430     DEFINE(VFDS," + vfds_data +")"  +"\n" 
    lines[35] = "00450	  DEFINE(CHW,"+ chw_data + ")" +"\n" 
    lines[37] = "00470	  DEFINE(PHW," + phw_data +")"+"\n" 
    lines[39] = "00510	  DEFINE(SA_T," + sa_data + ")"+"\n" 
    lines[41] = "00530	  DEFINE(PH," + ph_data + ")" +"\n" 
    lines[43] = "00550     DEFINE(OAZ," + oaz_data + ")" +"\n" 
    lines[45] = "00570     DEFINE(PHS," + phs_data + ")" +"\n" 
    lines[47] = "00590     DEFINE(SAS," + sas_data +")" + "\n" 
    lines[49] = "00610     DEFINE(SPS," + sps_data + ")" +"\n" 
    lines[51] = "00654     DEFINE(OAFL," + oafl_data + ")" +"\n" 
    lines[53] = "00658     DEFINE(OAFLSP,"+ oaflsp_data + ")" +"\n" 
    lines[75] = "00880     DEFINE(A," + bldg_num_data +"_"+unit_data+")" +"\n"


# Write the modified content back to the text file
    with open("OP2.txt", "w") as file:
        file.writelines(lines)

def modify_file3(rev2, date2, author2, comments2, rev3, date3, author3, comments3, unit_data , bldg_num_data, panel_name_data, panel_type_data, IP_address_data, panel_location_data, drawing_reference_data, rev_data, date_data, author_data, comments_data, occ_data, fss_data, static_data, vfds_data, chw_data, hw_data, ra_data, sa_data, ma_data, oaz_data, sas_data, sps_data, rmt_data, rmh_data, oafl_data, oaflsp_data):
 

# Read the content of the text file
    with open("AHU FDD TEMPLATE .txt", "r") as file:
        lines = file.readlines()

# Modify the specific line with custom text

    lines[2] = "00120     C *********************AIR HANDLER ["+unit_data+"] SMART FDD***********************************"+"\n"
    lines[7] = "00170	  C PANEL NAME - " + panel_name_data +"\n"  
    lines[8] = "00180	  C PANEL TYPE - " + panel_type_data +"\n"  
    lines[9] = "00190	  C IP ADDRESS - " + IP_address_data +"\n" 

    lines[11] = "00210	  C PANEL LOCATION - " + panel_location_data +"\n" 
    lines[12] = "00220	  C DRAWING REFERENCES - " + drawing_reference_data +"\n" 

    lines[14] = "00240	  C	   REV 	   DATE 			  AUTHOR			 COMMENTS"+"\n"
    lines[15] = "00250	  C        "+rev_data+"       "+date_data+"                            "+author_data+"                            "+comments_data+"\n"
    lines[16] = "00260	  C        "+rev2+"       "+date2+"                            "+author2+"                            "+comments2+"\n"
    lines[17] = "00270	  C        "+rev3+"       "+date3+"                            "+author3+"                            "+comments3+"\n"
    

    lines[27] = "00370	  DEFINE(OCC," + occ_data + ")"  +"\n"
    lines[29] = "00390	  DEFINE(FSS," + fss_data + ")"  +"\n"
    lines[31] = "00410	  DEFINE(STATIC_P" + static_data + ")" +"\n"
    lines[33] = "00430	  DEFINE(VFDS," + vfds_data +")"  +"\n"
    lines[35] = "00450     DEFINE(CHW,"+ chw_data + ")" +"\n"
    lines[37] = "00470 	  DEFINE(HW," + hw_data +")"+"\n"
    lines[39] = "00470 	  DEFINE(RA_T," + ra_data +")"+"\n"
    lines[41] = "00490	  DEFINE(SA_T," + sa_data + ")"+"\n"
    lines[43] = "00510	  DEFINE(MA_T," + ma_data + ")" +"\n"
    lines[45] = "00530     DEFINE(OAZ," + oaz_data + ")" +"\n"
    lines[47] = "00590     DEFINE(SAS," + sas_data + ")" +"\n"
    lines[49] = "00610     DEFINE(SPS," + sps_data +")" + "\n"
    lines[51] = "00630     DEFINE(RMT," + rmt_data + ")" +"\n"
    lines[53] = "00650     DEFINE(RMH," + rmh_data + ")" +"\n"
    lines[55] = "00654     DEFINE(OAFL," + oafl_data + ")" +"\n"
    lines[57] = "00658     DEFINE(OAFLSP," + oaflsp_data + ")" +"\n"
    lines[81] = "00880     DEFINE(A," + bldg_num_data +"_"+unit_data+")" +"\n"


# Write the modified content back to the text file
    with open("OP3.txt", "w") as file:
        file.writelines(lines)



def modify_file4(rev2, date2, author2, comments2, rev3, date3, author3, comments3, unit_data , bldg_num_data, panel_name_data, panel_type_data, IP_address_data, panel_location_data, drawing_reference_data, rev_data, date_data, author_data, comments_data, occ_data, fss_data, static_data, vfds_data, chw_data, hw_data, ra_data, sa_data, ma_data, oaz_data, ras_data, sas_data, sps_data, rmt_data, rmh_data):
 

# Read the content of the text file
    with open("AHU BACNET FDD TEMPLATE.txt", "r") as file:
        lines = file.readlines()

# Modify the specific line with custom text

    lines[2] = "00030     C *********************AIR HANDLER ["+unit_data+"] SMART FDD***********************************"+"\n"
    lines[7] = "00080     C PANEL NAME - " + panel_name_data +"\n"  
    lines[8] = "00090     C PANEL TYPE - " + panel_type_data +"\n"  
    lines[9] = "00100     C IP ADDRESS - "+ IP_address_data +"\n" 

    lines[12] = "00130	  C PANEL LOCATION - " + panel_location_data +"\n" 
    lines[13] = "00140	  C DRAWING REFERENCES - " + drawing_reference_data +"\n" 

    lines[15] = "00160	  C	 REV 	 DATE			 AUTHOR			 COMMENTS"+"\n"
    lines[16] = "00170	  C      "+rev_data+"       "+date_data+"                       "+author_data+"                       "+comments_data+"\n"
    lines[17] = "00180	  C      "+rev2+"       "+date2+"                       "+author2+"                       "+comments2+"\n"
    lines[18] = "00190     C      "+rev3+"       "+date3+"                       "+author3+"                       "+comments3+"\n"
    

    lines[28] = "00290     DEFINE(OCC,"+ occ_data + ")"  +"\n"
    lines[30] = "00310     DEFINE(FSS," + fss_data + ")"  +"\n" 
    lines[32] = "00330     DEFINE(STATIC_P," + static_data + ")" +"\n" 
    lines[34] = "00350     DEFINE(VFDS," + vfds_data +")"  +"\n" 
    lines[36] = "00370     DEFINE(CHW,"+ chw_data + ")" +"\n" 
    lines[38] = "00390     DEFINE(HW," + hw_data +")"+"\n" 
    lines[40] = "00410     DEFINE(RA_T," + ra_data +")"+"\n" 
    lines[42] = "00430     DEFINE(SA_T," + sa_data +")"+"\n" 
    lines[44] = "00450     DEFINE(MA_T," + ma_data +")"+"\n" 

    lines[46] = "00470     DEFINE(OAZ," + oaz_data + ")" +"\n" 
    lines[48] = "00490     DEFINE(RAS," + ras_data + ")" +"\n" 
    lines[50] = "00501     DEFINE(SAS," + sas_data + ")" +"\n" 
    lines[52] = "00530     DEFINE(SPS," + sps_data +")" + "\n" 

    lines[54] = "00550     DEFINE(RMT," + rmt_data + ")" +"\n" 
    lines[56] = "00570     C DEFINE(RMH,"+ rmh_data + ")" +"\n" 
    lines[79] = "00810     DEFINE(A," + bldg_num_data +"_"+unit_data+")" +"\n"

# Write the modified content back to the text file
    with open("OP4.txt", "w") as file:
        file.writelines(lines)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def form1():

    if request.method == 'POST':
        # Extract form data
        panel_name_data = request.form['panel_name']
        panel_type_data = request.form['panel_type']
        IP_address_data = request.form['IP_address']
        panel_location_data = request.form['panel_location']
        drawing_reference_data = request.form['drawing_reference']
        rev_data = request.form['rev']
        date_data = request.form['date']
        author_data = request.form['author']
        comments_data = request.form['comments']

        occ_data = request.form['occ']
        fss_data= request.form['fss']
        static_data= request.form['static']
        vfds_data= request.form['vfds']
        chw_data= request.form['chw']
        hw_data= request.form['hw']
        sa_data= request.form['sa']
        ctl_data= request.form['ctl']
        oaz_data= request.form['oaz']
        htg_data= request.form['htg']
        hc_data= request.form['hc']
        clg_data= request.form['clg']
        rmt_data= request.form['rmt']
        rmh_data= request.form['rmh']
        bldg_num_data= request.form['bldg_num']
        unit_data= request.form['unit']

        if 'radio_option' in request.form and request.form['radio_option'] == 'yes':
        # If yes, extract additional fields
            rev2 = request.form['rev2']
            date2 = request.form['date2']
            author2 = request.form['author2']
            comments2 = request.form['comments2']

            rev3 = request.form['rev3']
            date3 = request.form['date3']
            author3 = request.form['author3']
            comments3 = request.form['comments3']



        else:
        # If no, set additional fields to empty strings
            rev2 = ''
            date2 =''
            author2 =''
            comments2 =''

            rev3 = ''
            date3 =''
            author3 =''
            comments3 =''



        # Call the modify_file1 function to modify the file
        modify_file1(rev2, date2, author2, comments2, rev3, date3, author3, comments3, unit_data , bldg_num_data, panel_name_data, panel_type_data, IP_address_data, panel_location_data, drawing_reference_data, rev_data, date_data, author_data, comments_data, occ_data, fss_data, static_data, vfds_data, chw_data, hw_data, sa_data, ctl_data, oaz_data, htg_data, hc_data, clg_data, rmt_data, rmh_data)
        filename= "OP.txt"
        # Read the modified content from the file
        with open("OP.txt", "r") as file:
            modified_content = file.read()

        return render_template('preview.html', content=modified_content, fileName=filename)
        

    else:
        return render_template('form.html')



@app.route('/form2', methods=['GET', 'POST'])
def form2():
    if request.method == 'POST':
        # Extract form data
        panel_name_data = request.form['panel_name']
        panel_type_data = request.form['panel_type']
        IP_address_data = request.form['IP_address']
        panel_location_data = request.form['panel_location']
        drawing_reference_data = request.form['drawing_reference']
        rev_data = request.form['rev']
        date_data = request.form['date']
        author_data = request.form['author']
        comments_data = request.form['comments']

        occ_data = request.form['occ']
        fss_data = request.form['fss']
        static_data = request.form['static']
        vfds_data = request.form['vfds']
        chw_data = request.form['chw']
        phw_data = request.form['phw']
        sa_data = request.form['sa']
        ph_data = request.form['ph']
        oaz_data = request.form['oaz']
        phs_data = request.form['phs']

        sas_data = request.form['sas']
        sps_data = request.form['sps']
        oafl_data = request.form['oafl']
        oaflsp_data = request.form['oaflsp']
        bldg_num_data = request.form['bldg_num']
        unit_data = request.form['unit']

        if 'radio_option' in request.form and request.form['radio_option'] == 'yes':
            # If yes, extract additional fields
            rev2 = request.form['rev2']
            date2 = request.form['date2']  # Ensure correct field name
            author2 = request.form['author2']
            comments2 = request.form['comments2']

            rev3 = request.form['rev3']
            date3 = request.form['date3']
            author3 = request.form['author3']
            comments3 = request.form['comments3']

        else:
            # If no, set additional fields to empty strings
            rev2 = ''
            date2 = ''
            author2 = ''
            comments2 = ''

            rev3 = ''
            date3 = ''
            author3 = ''
            comments3 = ''

        # Call modify_file2 function with extracted data
        modified_content = modify_file2(rev2, date2, author2, comments2, rev3, date3, author3, comments3, unit_data, bldg_num_data, panel_name_data, panel_type_data, IP_address_data, panel_location_data, drawing_reference_data, rev_data, date_data, author_data, comments_data, occ_data, fss_data, static_data, vfds_data, chw_data, phw_data, sa_data, ph_data, oaz_data, phs_data, sas_data, sps_data, oafl_data, oaflsp_data)
        filename = "OP2.txt"

        # Read the modified content from the file
        with open("OP2.txt", "r") as file:
            modified_content = file.read()

        return render_template('preview.html', content=modified_content, fileName=filename)

    else:
        return render_template('form2.html')


@app.route('/form3', methods=['GET','POST'])
def form3():

    if request.method == 'POST':
        # Extract form data
        panel_name_data = request.form['panel_name']
        panel_type_data = request.form['panel_type']
        IP_address_data = request.form['IP_address']
        panel_location_data = request.form['panel_location']
        drawing_reference_data = request.form['drawing_reference']
        rev_data = request.form['rev']
        date_data = request.form['date']
        author_data = request.form['author']
        comments_data = request.form['comments']

        occ_data = request.form['occ']
        fss_data= request.form['fss']
        static_data= request.form['static']
        vfds_data= request.form['vfds']
        chw_data= request.form['chw']
        hw_data= request.form['hw']
        ra_data= request.form['ra']
        sa_data= request.form['sa']
        ma_data= request.form['ma']
        oaz_data= request.form['oaz']
        sas_data= request.form['sas']
        sps_data= request.form['sps']
        rmt_data= request.form['rmt']
        rmh_data= request.form['rmh']
        oafl_data= request.form['oafl']
        oaflsp_data= request.form['oaflsp']
        bldg_num_data= request.form['bldg_num']
        unit_data= request.form['unit']



        if 'radio_option' in request.form and request.form['radio_option'] == 'yes':
        # If yes, extract additional fields
            rev2 = request.form['rev2']
            date2 = request.form['date2']
            author2 = request.form['author2']
            comments2 = request.form['comments2']

            rev3 = request.form['rev3']
            date3 = request.form['date3']
            author3 = request.form['author3']
            comments3 = request.form['comments3']



        else:
        # If no, set additional fields to empty strings
            rev2 = ''
            date2 =''
            author2 =''
            comments2 =''

            rev3 = ''
            date3 =''
            author3 =''
            comments3 =''




        modified_content = modify_file3(rev2, date2, author2, comments2, rev3, date3, author3, comments3, unit_data , bldg_num_data, panel_name_data, panel_type_data, IP_address_data, panel_location_data, drawing_reference_data, rev_data, date_data, author_data, comments_data, occ_data, fss_data, static_data, vfds_data, chw_data, hw_data, ra_data, sa_data, ma_data, oaz_data, sas_data, sps_data, rmt_data, rmh_data, oafl_data, oaflsp_data)
        filename= "OP3.txt"
        # Read the modified content from the file
        with open("OP3.txt", "r") as file:
            modified_content = file.read()

        return render_template('preview.html', content=modified_content, fileName=filename)

        

    else:
        return render_template('form3.html')


@app.route('/form4', methods=['GET','POST'])
def form4():

    if request.method == 'POST':
        # Extract form data
        panel_name_data = request.form['panel_name']
        panel_type_data = request.form['panel_type']
        IP_address_data = request.form['IP_address']
        panel_location_data = request.form['panel_location']
        drawing_reference_data = request.form['drawing_reference']
        rev_data = request.form['rev']
        date_data = request.form['date']
        author_data = request.form['author']
        comments_data = request.form['comments']

        occ_data = request.form['occ']
        fss_data= request.form['fss']
        static_data= request.form['static']
        vfds_data= request.form['vfds']
        chw_data= request.form['chw']
        hw_data= request.form['hw']
        ra_data= request.form['ra']
        sa_data= request.form['sa']
        ma_data= request.form['ma']
        oaz_data= request.form['oaz']
        sas_data= request.form['sas']
        ras_data= request.form['ras']
        sps_data= request.form['sps']
        rmt_data= request.form['rmt']
        rmh_data= request.form['rmh']
        bldg_num_data= request.form['bldg_num']
        unit_data= request.form['unit']

        if 'radio_option' in request.form and request.form['radio_option'] == 'yes':
        # If yes, extract additional fields
            rev2 = request.form['rev2']
            date2 = request.form['date2']
            author2 = request.form['author2']
            comments2 = request.form['comments2']

            rev3 = request.form['rev3']
            date3 = request.form['date3']
            author3 = request.form['author3']
            comments3 = request.form['comments3']



        else:
        # If no, set additional fields to empty strings
            rev2 = ''
            date2 =''
            author2 =''
            comments2 =''

            rev3 = ''
            date3 =''
            author3 =''
            comments3 =''

        

        modified_content = modify_file4(rev2, date2, author2, comments2, rev3, date3, author3, comments3, unit_data , bldg_num_data, panel_name_data, panel_type_data, IP_address_data, panel_location_data, drawing_reference_data, rev_data, date_data, author_data, comments_data, occ_data, fss_data, static_data, vfds_data, chw_data, hw_data, ra_data, sa_data, ma_data, oaz_data, ras_data, sas_data, sps_data, rmt_data, rmh_data)
        filename= "OP4.txt"
        # Read the modified content from the file
        with open("OP4.txt", "r") as file:
            modified_content = file.read()

        return render_template('preview.html', content=modified_content, fileName=filename)

        

    else:
        return render_template('form4.html')
    

@app.route('/form5')
def form5():
    return render_template('form5.html')
    



# Route to render the preview page
@app.route('/preview/<filename>')
def preview(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return render_template('preview.html', content=content, fileName=filename)
    except FileNotFoundError:
        return render_template('preview.html', content=None)
    
    
    # Route for downloading a file


# Route to handle file downloads
@app.route('/download/<filename>')
def download(filename):
    try:
        return send_file(filename, as_attachment=True)
    except FileNotFoundError:
        return "File not found", 404
    






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True) # for port that can be used   app.run(host='128.186.114.123', port=9090, debug=True)   if __name__ == '__main__':    app.run(host='0.0.0.0', port=8080, debug=True)  # Change host and port as needed 

