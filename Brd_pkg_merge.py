'''
Board and Package File merge
'''

import os, sys,time

# debug mode for developer
debug_mode = False

# PowerSI installed path on the local machine
powersi_path = "C:\\Cadence\\Sigrity2021.1\\tools\\bin\\PowerSI.exe"



# Key variables
oldckt = "oldckt"
newckt = "newckt"
s_ball = "s_ball"
pkg = "pkg"
measurement = "measurement"
pkgpcb = "pkg&pcb"

# variables values
oldckt_value = "BRDU1"
newckt_value = "PKGA1"
s_ball_value = "SolderBall"
pkg_value = "InheritPkg"
measurement_value = "mm"
pkgpcb_value = "PKG&PCB"

# dict for cmd_import_pkg
pkg_import_data = {oldckt: oldckt_value, newckt: newckt_value, s_ball: s_ball_value, pkg: pkg_value, measurement:measurement_value, pkgpcb: pkgpcb_value}

def cmd_open_pkd_tgz(tgz_path):
    cmd = "sigrity::open document {" + tgz_path + "} {!}\n"
    return cmd


def cmd_import_stkup(stkup_path):
    cmd = "sigrity::import stackup {" + stkup_path + "} {!}\n"
    return cmd


def cmd_save_file():
    cmd = "sigrity::save {!} \n"
    return cmd


def close_pkg_file():
    cmd = "sigrity::close document {!} \n"
    return cmd


def cmd_open_brd(brd_file_path):
    cmd = "sigrity::open document {" + brd_file_path + "} {!}\n"
    return cmd


def cmd_import_pkg(pkg_import_data):
    '''
    pkg_import_data["spd_path_value"]- path of spd file
    pkg_import_data["Height_value"]- solder ball height
    pkg_import_data["Radius_value"]-solder ball radius

    Example: 
    import PKG -SPDFile {E:/Share/VakulabharanamX/pkg_and_brd_files/pkg_file/dg256eu_ww45p3_pisimulation.spd} -OldCkt {BRDU1} 
    -NewCkt {PKGA1} -method {SolderBall} -MatchSel {InheritPkg} -unit {mm} -height {4.7264e-02} -radius {2.4498e-02} -Prefix -ApplyTo {PKG&PCB} {!}

    '''
    cmd = r"sigrity::import PKG -SPDFile {" + pkg_import_data["spd_path_value"] + "} -OldCkt {" + pkg_import_data[oldckt] + "} -NewCkt {" + \
          pkg_import_data[newckt] + "} -method {" + pkg_import_data[s_ball] + "} -MatchSel {" + pkg_import_data[pkg] + "} -unit {" + pkg_import_data[measurement] + "} -height {" + \
          pkg_import_data["Height_value"] + "} -radius {" + pkg_import_data["Radius_value"] + "} -Prefix -ApplyTo {" + pkg_import_data[pkgpcb] + "} {!}" + "\n"
    if debug_mode:
        print("The import package path is:", cmd)
    return cmd


def cmd_save_file():
    cmd = "sigrity::save {!} \n"
    return cmd


def file_updation(cmd_list):
    try:
        with open("brd_pkg_merge.tcl", 'w') as file:
            file.writelines(cmd_list)
        return True
    except Exception as err:
        print("Error while opening file brd_pkg_merge.tcl",err)
        return False


def execute_cmd(tclfile_path):
    execute_cmd = powersi_path + " -PSPowerSI -b -tcl " + tclfile_path

    if debug_mode:
        print("The command executing is:", execute_cmd)
    print("Please wait!! Files are processing to merge...")
    os.system(execute_cmd)
    print("Board and Package files are merged.")
    time.sleep(20)


def my_text_frame(string_lst, width=115):
    g_line = "+{0}+".format("-"*(width-2))
    print(g_line)
    for line in string_lst:
        print("| {0:<{1}} |".format(line, width-4))
    print(g_line)

def get_input_from_user(cmd_list=[]):
    try:
        my_text_frame("                                         BOARD AND PACKAGE FILE MERGE".splitlines())
        tgz_path = input("Enter the pakage(tgz) file path: ")
        if (os.path.isfile(tgz_path)):
            cmd_list.append(cmd_open_pkd_tgz(tgz_path))
        else:
            print("Please recheck the entered path and .tgz file present or not")
            time.sleep(30)
            sys.exit()
        #.spd file path
        pkg_import_data["spd_path_value"] = tgz_path[0:-3] + "spd"

        stkup_path = input("Enter the stackup file path: ")
        if (os.path.isfile(stkup_path)):
            cmd_list.append(cmd_import_stkup(stkup_path))
        else:
            print("Please recheck the entered path and .csv file present or not")
            time.sleep(30)
            sys.exit()

        #Saving the file
        cmd_list.append(cmd_save_file())

        #Closing of package file
        cmd_list.append(close_pkg_file())

        brd_file_path = input("Enter the Board file path: ")
        if (os.path.isfile(brd_file_path)):
            cmd_list.append(cmd_open_brd(brd_file_path))
        else:
            print("Please recheck the entered path and .brd file present or not")
            time.sleep(30)
            sys.exit()
            
        Height_value=input("Enter the solderball height:")
        if Height_value=='':
            print("Please check the entered solderball height")
            time.sleep(30)
            sys.exit()
        else:
            pkg_import_data["Height_value"] = Height_value

        Radius_value=input("Enter the solderball radius:")
        if Radius_value=='':
            print("Please check the entered solderball radius")
            time.sleep(30)
            sys.exit()
        else:
            pkg_import_data["Radius_value"] = Radius_value 
        
        cmd_list.append(cmd_import_pkg(pkg_import_data))
        cmd_list.append(cmd_save_file())
        return cmd_list
    except Exception as error:
        print("The Error raised from get_input_from_user function is:",error)


def tcl_execution():
    tcl_path = input("Enter tcl file path to execute:")
    tclfile_path =tcl_path + "\\brd_pkg_merge.tcl"
    execute_cmd(tclfile_path)



if __name__ == "__main__":
    file_updation(get_input_from_user(cmd_list=[]))

    tcl_execution()
