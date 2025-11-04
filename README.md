mkdir -p ~/.termux/boot

### Now create a script file:
nano ~/.termux/boot/start.sh

#### Paste this inside
#!/data/data/com.termux/files/usr/bin/bash
cd /data/data/com.termux/files/home
python wol.py

#### Make it excutable
chmod +x ~/.termux/boot/start.sh

#####
Before rebooting, test your script works:
bash ~/.termux/boot/start.sh
