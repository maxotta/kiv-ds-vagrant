# KIV/DS Vagrant ukázky

## Příprava pod WSL (Windows Subsystem for Linux)

* Nainstalujeme WSL pod lokálním administrátorem
* Provedeme aktualizaci a nainstalujeme Ansible
```
    sudo apt-get update
    sudo apt-get -y install python-pip python-dev libffi-dev libssl-dev
    pip install ansible --user

    wget https://releases.hashicorp.com/vagrant/2.2.5/vagrant_2.2.5_x86_64.deb
    dpkg -i vagrant_2.2.5_x86_64.deb
```
Na konec souboru .bash_profile přidáme:

```
export PATH=~/.local/bin:$PATH
export VAGRANT_WSL_ENABLE_WINDOWS_ACCESS="1"
export PATH="$PATH:/mnt/c/Program Files/Oracle/VirtualBox"
export VAGRANT_WSL_WINDOWS_ACCESS_USER_HOME_PATH="/mnt/c/src"
export VAGRANT_WSL_DISABLE_VAGRANT_HOME="true"
```

## TODOS
- [ ] translate all README.md's into English
- [ ] better description of WSL installation (provide screenshots)
- [ ] add Linux & OSX HOWTOs
- [ ] install Ansible via dpkg


