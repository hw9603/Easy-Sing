ui_files = ["mainwindow_ui", "startwindow_ui", "melodywindow_ui", "generatewindow_ui"]
for file in ui_files:
    f = open(file + ".py", "rw")
    origin_str = "self.retranslateUi(MainWindow)"
    new_str = "Ui_MainWindow.retranslateUi(self, MainWindow)"
    f.write(f.read().replace(origin_str, new_str))
    f.close()