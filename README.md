# WW1-game-dependency-edition
Remake of my Lua WW1 game.  
Now works with uv! All dependencies listed in pyproject.toml  
  
TODO:  
    Create inventory system (equippable items, multiple inventories for different bags?)  
    Create a map for the friendly trenches  
    Add NPC's (traders, officers that give quests, and friends who you can barter with)  
    Add movement  
    Add real-time keyboard input using the keyboard library  

How to setup uv:  
install python :D  
run this in the main folder (the one with this readme file):  
python3 -m venv .venv  
then run this:  
source .venv/bin/activate  
then this:  
pip install uv  
and this:  
uv sync  
and finally this to check if you actually have the dependencies:  
uv pip freeze  
  
if these instructions are wrong, look up how to install uv.  
if your wondering: "python dependency hell IS a real place and you will be sent there at  
the first sign of defiance." - balogina 2026  