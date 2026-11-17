# Scenario 03 Evidence

Preserve actual terminal output for:

- Initial filesystem block and inode capacity
- Loopback device creation and attachment
- ext4 formatting output
- Mount information
- Block exhaustion and resulting `df -h`
- Inode exhaustion and resulting `df -i`
- Cleanup: unmount, loop-device detach and image removal verification

Do not fabricate missing output. Record any cleanup step as pending until verified.
