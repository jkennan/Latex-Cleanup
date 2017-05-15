import os

def latex_cleanup(path):
    print "---------CLEANING LATEX---------"
    dirfiles = os.listdir(path)
    if not os.path.exists(str(path)+"/!LATEX-CLEANUP"):
        os.makedirs(str(path)+"/!LATEX-CLEANUP")

    #DEBUG


    for file in dirfiles:
        full_path = os.path.abspath(file)
        # print full_path
        filename, file_extension = os.path.splitext(file)
        # print "filename " + str(filename) + " ex " + str(file_extension)
        if file_extension.endswith('.aux') or file_extension.endswith('.fdb_latexmk') \
            or file_extension.endswith('.fls') or file_extension.endswith('.gz') \
            or file_extension.endswith('.txt') or file_extension.endswith('.log'):
            print "moving to " + str(path) + "\\" + str(filename) + str(file_extension)
            os.rename(str(path) + "\\" + str(filename) + str(file_extension), str(path) + "\\!LATEX-CLEANUP\\" + str(filename) + str(file_extension))

    print "----------CLEANUP COMPLETED----------"




if __name__ == "__main__":
    print "Enter a filepath to cleanup latex"
    path = raw_input()
    latex_cleanup(path)
