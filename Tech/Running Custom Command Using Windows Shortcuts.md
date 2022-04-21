> I have a personal Obsidian PKM and I edit it in both Obsidian and VSCode (since I have nice LaTEX snippets + git push script in VSCode). I find it way too troublesome to open the PKM folder in VSCode by hand every time, so I searched for a solution online...

**Steps:**
1. Open the `Properties` pane
2. Set `Target` to `%comspec% /c <command>` (`/c` = close command prompt, `/k` = keep command prompt. If you set `c/`, remember to set `Run`  to Minimized to avoid a flashing command prompt.)
3. Set `Start in` to your desired working directory (equivalent to running the command in that directory)
4. Set a fancy icon, see mine :) 
![[obsidian_vscode_shortcut_icon.ico]]
5. Pin it to the Task bar!

**Note**
If you want to open a certain folder in VSCode, use `%comspec% /c code <full_path>` instead of `%comspec% /c code .` even if you have set your `Start in` to `<full_path>`. This is because multiple shortcuts with the same `Target` cannot be pinned to the taskbar together. To avoid future clashes, we should specify the full path in `Target`.