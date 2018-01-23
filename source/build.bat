@echo off
cd res/qt
echo Building app.ui
pyuic5 app.ui -o app_ui.py
echo Building app_ui_res.qrc
pyrcc5 app_ui_res.qrc -o app_ui_res_rc.py
cd ../..
echo Done
pause
