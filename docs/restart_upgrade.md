# Configure Restart and Upgrade over HA Web

Follow below two simple steps to let your HASS to restart and even upgrade to newer version without going to console!
Note: If there are any configuration errors, your upgrade might nor be successful. 

### Step 1: Add the following to the sudoers file using `sudo visudo` command 

The following is my sudoers file contents:

```
#
# This file MUST be edited with the 'visudo' command as root.
#
# Please consider adding local content in /etc/sudoers.d/ instead of
# directly modifying this file.
#
# See the man page for details on how to write a sudoers file.
#
Defaults        env_reset
Defaults        mail_badpass
Defaults        secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"

# Host alias specification

# User alias specification

# Cmnd alias specification

# User privilege specification
root    ALL=(ALL:ALL) ALL

# Members of the admin group may gain root privileges
%admin ALL=(ALL) ALL

# Allow members of group sudo to execute any command
%sudo   ALL=(ALL:ALL) ALL

# See sudoers(5) for more information on "#include" directives:

#includedir /etc/sudoers.d

# Allow homeassistant to use hassctl
homeassistant ALL=(ALL) NOPASSWD: /bin/systemctl
homeassistant ALL=(ALL) NOPASSWD: /bin/journalctl
```

## Step 2: Add the following to a package/file and restart your HASS

```
homeassistant:
  customize:
  
    script.update_hass:
      friendly_name: Update Home Assistant
      icon: mdi:home-assistant

    script.restart_hass:
      friendly_name: Restart Home Assistant
      icon: mdi:home-assistant

script:
  update_hass:
    sequence:
      - service: shell_command.update_hass
  restart_hass:
    sequence:
      - service: shell_command.restart_hass

shell_command:
  restart_hass: >-
    hassctl restart

  update_hass: >-
    hassctl update-hass && hassctl config && hassctl restart

#/srv/homeassistant/homeassistant_venv/bin/pip3 install --upgrade homeassistant && sudo systemctl restart home-assistant.service
```