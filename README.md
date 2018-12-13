# VLC-Tasker-using-Tracktime-in-Python
Python project for getting functions executed in sync with tracktime of VLC Player

## Requirements:
- Python 3.7.1 (latest version in 13 of December 2018)
- VLC Player 3.0.3 (latest Recent version in 13 of December 2018)


## Instructions
### Install latest version of Python and VLC Player
1. Python - www.python.org
2. VLC Player - www.videolan.org

### Enabling VLC Web Interface
1. Enable Web interface going on Tools -> Preferences -> Show settings -> All -> Interface -> Main interfaces -> Check box "Web"
2. Expand Main interfaces -> Lua
3. Configure the Lua HTTP putting a password and in Source directory C:\Program Files\VideoLAN\VLC\lua\http and in Lua Telnet change Port to 8080.
4. Try to access the Web interface using on your browser http://localhost:8080/requests/status.xml and leave user in blank and put the password that you used in the configuration

## Funcionality
The code will extrack the time from whatever is playing on VLC Player and with that information a function that will identify the stages of the song. The reprouction can be from web or local, the only things is required is that both the code and the VLC Player be running at the same time.

## Example
- Song: The Chainsmokers - This Feelings (Afrojack & Disto Remix - Official Audio)
- Link: www.youtube.com/watch?v=pB_45kwdd6o

## Future Improvements
- [ ] Make code more efficient using the VLC state information
- [ ] New features for the code and implementations with VLC Player
- [ ] Make code more dynamic to other types of content
- [ ] Develop Timestamp + Task file creator 
