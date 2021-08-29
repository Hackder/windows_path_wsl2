alias reload-path="zsh $HOME/windows_path_wsl2/shell_setup.sh"

p="$PATH"

if ! [ "$WINDOWS_PATHS_WSL2_SETUP" = "1" ]
then
  win_path_orig=$(echo -e "${PATH//:/\n}" | grep -E "^/mnt/c" | awk '!x[$0]++' | tr "\n" ":" | sed -e "s/:$//g" -e "s/'//g")
  echo "$win_path_orig" > $HOME/windows_path_wsl2/windows_paths.txt
fi

linux_path=$(echo -e "${PATH//:/\n}" | grep -v -E "^/mnt/c" | tr "\n" ":" | sed -e "s/:$//g" -e "s/'//g")
touch $HOME/windows_path_wsl2/active_paths.txt
win_path=$(cat $HOME/windows_path_wsl2/active_paths.txt)

if ! [ -z "$win_path" ]
then
  p="$linux_path:$win_path"
else
  p="$linux_path"
fi

export PATH="$p"
export WINDOWS_PATHS_WSL2_SETUP="1"