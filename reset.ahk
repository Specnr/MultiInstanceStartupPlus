#NoEnv
SetKeyDelay, 0

ControlSend, ahk_parent, {Blind}{Shift down}{Tab}{Shift up}{Enter}, ahk_pid %pid%

while (True) {
  WinGetTitle, title, ahk_pid %pid%
  if (InStr(title, " - "))
    break
}
sleep, 3000
FileDelete, hold.tmp
ExitApp
