# WW1-game-dependency-edition
Remake of my Lua WW1 game.  
Now works with uv! All dependencies listed in pyproject.toml  
  
TODO:  
    Create inventory system (equippable items, multiple inventories for different bags?)  
    Create a map for the friendly trenches  
    Add NPC's (traders, officers that give quests, and friends who you can barter with)  
    Add movement  
    Add real-time keyboard input using the keyboard library  

## Setup Python Dependencies
Make sure python is installed.
```
# install uv by running this:
curl -LsSf https://astral.sh/uv/install.sh | sh
# (if your on windows, run this instead):
wget -qO- https://astral.sh/uv/install.sh | sh

# Run this in the main folder (the one with this readme file)
uv sync

# Finally this to check if you actually have the dependencies:  
uv export --format requirements.txt > requirements.txt
```

  
If these instructions are wrong, look up how to install uv.
If your wondering: Yes, Python dependency hell IS a real place and you will be sent there at the first sign of defiance.