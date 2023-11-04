@ECHO OFF
CD /D "%~DP0"
DEL /A /F /Q /S "%~DP0*.JPG"
DEL /A /F /Q /S "%~DP0*.PNG"
PAUSE