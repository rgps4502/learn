@echo off
chcp 1250 > NUL
call pyenv exec %~n0 %*
