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
ControlSend, ahk_parent, {Blind}{Shift Down}{F3}{Shift Up}, ahk_pid %pid%
Sleep, 1000
ControlSend, ahk_parent, {Blind}{1}{1}{1}, ahk_pid %pid%
ControlSend, ahk_parent, {Blind}{%sprintKey%}{%perspKey%}{F3}, ahk_pid %pid%
Sleep, 1000
ControlSend, ahk_parent, {Blind}{F3 Down}{B}{Esc}{F3 Up}, ahk_pid %pid%
ExitApp
