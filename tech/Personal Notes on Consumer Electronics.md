## Dell XPS 17 and WD19TB Electrical Whine
I have both the Dell XPS 17 9700 and WD19TB and they both have a very noticeable electrical whine / charging noise when plugged into AC power. I found this [solution](https://www.dell.com/community/XPS/XPS-17-9700-Charging-noise/td-p/7669861/page/2) online and it indeed solved the issue.

1. Go to `Control Panel\Hardware and Sound\Power Options\Change plan settings`
2. Select `Change advanced power settings => Processor power management`
3. Change to:
```txt
# Online solution suggest changing to 99%, but 0% works for me. And I'm afraid minimum 99% kills my battery very fast.
Minimum processor state
- On battery: 0%
- Plugged in: 0%

Maximum Processor State
- On battery: 99%
- Plugged in: 99%
```