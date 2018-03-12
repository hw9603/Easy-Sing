import os
import re

def replace():
	folder = "./vocaloid/gui/"
	ui_files = ["mainwindow_ui", "startwindow_ui", "melodywindow_ui", "generatewindow_ui"]
	for file in ui_files:
	    f = open(folder + file + ".py", "r")
	    origin_str = "self.retranslateUi(MainWindow)"
	    new_str = "Ui_MainWindow.retranslateUi(self, MainWindow)"
	    content = f.read().replace(origin_str, new_str)
	    content = re.sub(r'MainWindow\.resize\(\d*, \d*\)\s*' , '',content)
	    f.close()
	    os.remove(folder + file + ".py")
	    f = open(folder + file + ".py", "w")
	    f.write(content)
	    f.close()

if __name__ == "__main__":
	replace()