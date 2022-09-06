# system-hardening-7
**Category:** Misc
**Difficulty:** Hard
**Author:** Eth007/FIREPONY57

## Description
rooReaper wasn't lying when he said that he would be back. Seems that he's infiltrated the roos' new workstation! Can you investigate and secure the system?

The challenge is best played using VMware workstation player. However, you may be able to get it to work with other software. You will receive the flag when you reach 100 points.

It appears that the scoring binary depended on a specific CPU extension. If the engine does not score, and you are getting a Illegal instruction when you run /opt/engine/engine, run this command on the VM: sudo curl "https://s1.fdow.nl/HgtoW-engine" -o "/opt/engine/engine" and reboot.

## Distribution

https://drive.google.com/file/d/1gyshPKjhQ2o907LQpwB_gq3BeqwmN2ko/view?usp=sharing https://drive.google.com/file/d/1xSwlRWTa2BYhjzUMA_7BKeqrCx3-prGJ/view?usp=sharing (alternate download link)

