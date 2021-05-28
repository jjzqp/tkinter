@echo off

copy .\project.bin ..\..\..\..\tools\res\JL.sty
copy .\result.bin  ..\..\..\..\tools\res\menu.res
copy .\result.str  ..\..\..\..\tools\res\str.res
if exist "..\..\..\..\..\..\..\apps\watch\include\ui\" (
    copy .\ename.h     ..\..\..\..\..\..\..\apps\watch\include\ui\style_JL.h
)
pause
exit
