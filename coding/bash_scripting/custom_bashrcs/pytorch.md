```bash
# .custom_bashrc4docker
#
############################################
#  Bash Shell Run Commands Customization   #
############################################
# Rev.6: 2020-0326 (Thu)
# Rev.5: 2020-0324 (Tue)
# Rev.4: 2019-1218 (Wed)
# Rev.3: 2019-1128 (Wed)
# Rev.2: 2019-1023 (Wed)
# Rev.1: 2018-0912 (Wed)
# Draft: 2017-1103 (Fri)
#
# Usage
#   1. Open .bashrc, add the following line at the bottom, and save the file.
#      source .custom_bashrc4docker
#   2. Type in the following command to apply the change in the .bashrc.
#      $ source .bashrc
#
# Troubleshooting
#   * Problem
#   $ source .bashrc
#   -bash: .custom_bashrc4docker: No such file or directory
#   $
#   * Solution
#   Check if the file ".custom_bashrc4docker" exists or the file name is correct.
#
#   * Problem
#   $ bash
#   bash: .custom_bashrc: line 91: unexpected EOF while looking for matching `''
#   bash: .custom_bashrc: line 98: syntax error: unexpected end of file
#   $
#   * Cause
#   The command is enclosed with ' and ".
#           '                                     "
#   alias f='find . -name '*.py'|xargs grep -i -n "  # search
#   * Solution
#   ' is replaced to ".
#   alias f="find . -name '*.py'|xargs grep -i -n "  # search

##################
#  Shell Output  #
##################
# 2020-03-24 (Tue) 09:35 (12th week)
export HISTIGNORE='ls:l:pwd:history:h'
echo `date +%F" ("%a") "%H:%M" ("%U"th week)"`  # Display time information

#####################
#  Welcome Message  #
#####################
# Welcome to ubuntu18.04, conda 4.8.2, Python 3.7.6
linux_distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
python_version=`python --version`
anaconda_version=`conda -V`

# PyTorch Versions
pytorch_version=`python -c 'import torch; version=torch.__version__; print(f"pytorch-{version}")'`
torchvision_version=`python -c 'import torchvision; version=torchvision.__version__; print(f"torchvision-{version}")'`
torchtext_version=`python -c 'import torchtext; version=torchtext.__version__; print(f"torchtext-{version}")'`
torchaudio_version=`python -c 'import torchaudio; version=torchaudio.__version__; print(f"torchaudio-{version}")'`

# Welcome to ubuntu18.04, conda 4.8.3, Python 3.7.6, pytorch-1.4.0, torchvision-0.5.0, torchtext-0.5.0, torchaudio-0.4.0
echo "Welcome to $linux_distribution, $anaconda_version, $python_version, $pytorch_version, $torchvision_version, $torchtext_version, $torchaudio_version"

#################
#    History    #
#################
# To clear the previous history, type in:
#   $ history -c
# To recall previous command, type in:
#   $ !8
#   $ !net
export HISTCONTROL=erasedups                    # Erase dup(licate)s
# Add time format as follows:
#   273  2017-11-03 Fri 09:52:01 ls
export HISTTIMEFORMAT="%F %a %T "
HISTSIZE=10000                                  # Default size: 1000
HISTFILESIZE=20000                              # Default size: 2000

#################
#     Alias     #
#################
alias ai='sudo apt-get install -y'
alias ap='sudo apt-get purge'
alias c='cd'
alias d='~/.dropbox-dist/dropboxd'  # If dropbox is used.
alias f="find . -name '*.py'|xargs grep -i -n "  # search
alias g='grep -n'
alias h='history'
alias j='run_jupyter_notebook'
alias ll='ls -alF'  # .bashrc default
alias la='ls -A'    # .bashrc Default
alias l='ls -CF'    # .bashrc Default
alias m='more'
alias n='nano'
alias p='pwd'
alias pi='pip install -y'
alias s='spyder'
alias t='tree'
alias td='tree -d'
alias tl='tree -d -L'

#################
# Alias: Docker #
#################
alias dp='docker ps'
alias di='docker images'
alias dc='docker commit'
alias di='docker login'
alias do='docker logout'

alias dr='docker run -it'
alias da='docker attach'

#################
#     PATH      #
#################
export PATH="/home/user/bin:$PATH"
#export PATH=$PATH:$HOME/bin
```