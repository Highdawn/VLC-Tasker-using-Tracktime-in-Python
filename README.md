# VLC-Tasker-using-Tracktime-in-Python
Python project for getting functions executed in sync with tracktime of VLC Player

Requirements:
- Python 3.7.1 (Most Recent version in 13 of December 2018)
- VLC Player 3.0.3 (Most Recent version in 13 of December 2018)


Instructions
1- Install Python and VLC Player

Enabling VLC Web Interface
1- Enable Web interface going on Tools -> Preferences -> Show settings -> All -> Interface -> Main interfaces -> Check box "Web"
2- Expand Main interfaces -> Lua
3.1- Configure the Lua HTTP putting a password and in Source directory C:\Program Files\VideoLAN\VLC\lua\http and in Lua Telnet change Port to 8080.
3.2 - Try to access the Web interface using on your browser http://localhost:8080/requests/status.xml and leave user in blank and put the password that you used in the configuration

