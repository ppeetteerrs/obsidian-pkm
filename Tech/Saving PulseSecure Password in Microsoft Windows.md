> I am a lazy person. And I am annoyed that PulseSecure cannot save my VPN credentials. So I decided to force it to do so.

*Disclaimer: this hack only applies to people who are willing to store their VPN passwords in plain text*

**Steps**
1. Create a Windows shortcut (by copying an existing shortcut or creating a new one, doesn't matter)
2. Open the shortcut's `Properties` pane
3. Set the `Target` as `"C:\Program Files (x86)\Common Files\Pulse Secure\Integration\pulselauncher.exe" -url <VPN_URL> -u <username> -p <password> -r <realm/domain>` (replace the placeholders)
4. Set `Start in` as `"C:\Program Files (x86)\Common Files\Pulse Secure\Integration"`
5. Give it a fancy icon using `Change Icon`, or use mine
![[pulse_secure_shortcut_icon.ico]]
6. Pin it to your Taskbar if you want to!
