#!/bin/bash

# step 1 go to brew.sh and install 
# Homebrew by running the command provided there
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# step 2 once brew is installed, run "brew install python" to install Python 3
brew install python

# step 3 run "nano .zprofile"
# in your home directory to edit the zprofile file
# (you may need to create this file if it doesn't exist)
cd ~

# Define the file to check
FILE=".zprofile"

# Check if the file does not exist
if [ ! -f "$FILE" ]; then
    echo ".zprofile File does not exist. Running command to create it ..."
    # Replace this with your desired command
    touch "$FILE"
    echo "File created."
fi

nano .zprofile

# step 4 add the following line to the .zprofile file
# export PATH="/opt/homebrew/bin/python3:$PATH"
echo 'export PATH="/opt/homebrew/bin/python3:$PATH"' >> .zprofile

# step 5, save the file by pressing CTRL+X and enter Y to confirm
# and then press Enter to exit nano
# Note: The above step is done in the nano editor, so no command is needed here
# Display a message to indicate that the file has been updated
echo ".zprofile has been updated with the new PATH."
cat .zprofile

# step 6 run "source .zprofile" to apply the changes
source .zprofile

# step 7 run "python3 --version" to verify the installation
python3 --version