#NoEnv
SetKeyDelay, 0

ControlSend, ahk_parent, {Blind}{Shift Down}{Tab}{Shift Up}{Enter}, ahk_pid %pid%

while (True) {
  WinGetTitle, title, ahk_pid %pid%
  if (InStr(title, " - "))
    break
}
sleep, 3000
FileDelete, C:\MultiInstanceMC\Skin Startup\hold.tmp
ControlClick, x0 y0, ahk_pid %pid%
ControlSend, ahk_parent, {Blind}{Esc}, ahk_pid %pid%
ExitApp
