# Overview

By default in wsl2, windows path is appended to linux path. This can cause performance issues with shells linke ZSH.
These shells and their plugins may scan path, to provide available commands to the user.

This creates a performance issue, because windows drive is mouted as network share, so file access is not the fastest.

This utility allows you to specificaly chose which entries from windows path you want appended to the linux path, therefore improving performance


# Installation

```bash
cd ~
git clone https://git
cd windows_path_wsl2
python3 -m pip install -r requirements.txt
```

Add this line to your `.bashrc` or `.zshrc` file

```bash
source "$HOME/windows_path_wsl2/shell_setup.sh"
```

Done! Reload your terminal session for this to take effect.

# Usage

```bash
./run.sh
```

