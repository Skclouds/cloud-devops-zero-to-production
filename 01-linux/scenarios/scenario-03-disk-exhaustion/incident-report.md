# Scenario 03: Linux Disk and Inode Exhaustion

## Incident
Application file uploads fail with:
No space left on device

## Objective
Understand and reproduce block exhaustion and inode exhaustion.

## Environment
- Ubuntu 24.04.5 LTS
- WSL2
- ext4 filesystem
- Loopback devices

## Experiment A: Block exhaustion

Created a 64 MB filesystem image and formatted it as ext4.

Mounted device: /dev/loop0

Initial observations:
- Filesystem size: 56 MB
- Available: 52 MB
- Total inodes: 16384

Created an 80 MiB test write using dd.

Command:
dd if=/dev/zero of=large-file.bin bs=1M count=80 status=progress

Result:
- Write failed with No space left on device.
- Approximately 51 MiB was written.
- Filesystem usage reached 100%.
- Available inodes: 16372.

Root cause:
Filesystem data blocks were exhausted while free inodes remained.

## Experiment B: Inode exhaustion

Created a 32 MB filesystem image with 128 inodes.

Mounted device: /dev/loop1

Initial observations:
- Filesystem size: 28 MB
- Available: 28 MB
- Total inodes: 128
- Used inodes: 11
- Free inodes: 117

Created small files using a shell loop.

Result:
File creation failed at iteration 118 with:
No space left on device.

Root cause:
The filesystem ran out of available inodes even though data blocks remained available.

## Important distinction

Block exhaustion:
- df -h reports full capacity.
- df -i may show free inodes.
- Large and small file creation can fail.

Inode exhaustion:
- df -i reports 100%.
- df -h may still show free space.
- New file creation fails because no inode can be allocated.

## Troubleshooting commands

df -h
df -i
du -sh DIRECTORY
du --inodes -x -d 3 DIRECTORY
findmnt
find
lsof +L1

## Production prevention
- Monitor disk and inode utilization independently.
- Implement log rotation and retention.
- Clean temporary files safely.
- Investigate uncontrolled file generation.
- Configure application cache expiration.
- Alert before filesystem exhaustion.

## Evidence limitation
The original loopback filesystem images were removed or are no longer present in the working directory. Results above are documented from the recorded terminal output.
