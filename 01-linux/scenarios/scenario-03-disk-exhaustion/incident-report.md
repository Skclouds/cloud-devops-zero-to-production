# Scenario 03 — Disk and Inode Exhaustion

## Scenario objective

Reproduce two different filesystem capacity failures in isolated ext4 loopback filesystems:

1. Data block exhaustion.
2. Inode exhaustion.

Learn how to distinguish the failures and verify them using filesystem tools.

## Environment

- OS: Ubuntu 24.04.5 LTS under WSL2
- Root filesystem: ext4
- Lab storage: disposable image files attached through loop devices
- Utilities checked: `mkfs.ext4`, `mount`, `losetup`, `fallocate`

## Baseline inspection

Commands used:

```bash
df -h
df -i
findmnt
```

The root filesystem had substantial free block and inode capacity. The `/mnt/c` mount used WSL's 9p filesystem and reported unusual inode values. Those values should not be interpreted like ext4 inode statistics.

## Lab filesystem creation

Two small filesystem images were created:

- Block exhaustion image: 64 MB.
- Inode exhaustion image: 32 MB, formatted with a requested inode count of 128 and zero reserved blocks.

The images were formatted as ext4, attached to loop devices and mounted at separate lab mount points.

The block filesystem reported 16,384 inodes.

The inode filesystem reported 128 inodes.

## Scenario A — Block exhaustion

The block filesystem initially showed:

- Filesystem size: approximately 56 MB.
- Used: approximately 24 KB.
- Available: approximately 52 MB.
- Block usage: approximately 1%.
- Inodes: 16,384 total, 11 used, 16,372 free.

The mount point was initially root-owned. A permission-denied error occurred when attempting to write as the regular user.

The mount-point ownership was changed for the lab user so that the test could proceed.

The following command was used to fill the filesystem:

```bash
dd if=/dev/zero \
  of=mounts/block-test/large-file.bin \
  bs=1M count=80 status=progress
```

The write stopped with `No space left on device` after approximately 51 MiB.

After the attempt:

- Block usage was approximately 100%.
- Approximately 464 KB remained available.
- Inode usage was approximately 1%.
- Most inodes remained free.

**Finding:** Data block exhaustion was reproduced.

## Scenario B — Inode exhaustion

The second filesystem initially showed:

- 128 total inodes.
- 11 used inodes.
- 117 free inodes.

A loop attempted to create up to 150 empty files using `touch`.

The loop stopped at approximately file 118 with `No space left on device`.

The initial 117 free inodes were consumed by the newly created files.

**Finding:** Inode exhaustion was reproduced.

The final `df -i` output should be captured when the lab is repeated or evidence is collected. The initial count and stopping point are recorded from the observed exercise.

## Root-cause distinction

| Failure | Resource exhausted | Diagnostic command |
|---|---|---|
| Block exhaustion | Data blocks | `df -h` |
| Inode exhaustion | Inodes | `df -i` |

Both failures can prevent new files from being created, but the remediation is not necessarily the same.

## Production lessons

- A filesystem can have free gigabytes and still be unable to create files if its inodes are exhausted.
- Many tiny files can exhaust inodes before exhausting data blocks.
- Large log files, database files and artifacts can exhaust data blocks.
- `df` reports filesystem-level allocation; `du` reports usage visible through directory traversal.
- Deleted files held open by processes can explain differences between `df` and `du`.
- WSL's 9p-mounted Windows drives may report inode information differently from ext4.

## Cleanup and safety status

The scenario's cleanup was not verified in the recorded terminal evidence.

Before considering the lab fully closed:

1. Inspect active mounts with `findmnt`.
2. Confirm the loop devices with `sudo losetup -a`.
3. Unmount both test filesystems.
4. Detach their loop devices.
5. Remove disposable image files only after confirming the correct paths.
6. Verify that no test mounts or loop devices remain.

Do not assume cleanup succeeded without checking.

## Status

**Failure reproduction completed for block and inode exhaustion. Cleanup verification remains pending.**

## Evidence

The `evidence/` directory should contain actual outputs from:

- Initial `df -h` and `df -i`.
- `findmnt` output.
- Filesystem formatting and loop-device attachment.
- Block exhaustion result.
- Inode exhaustion result.
- Final filesystem checks.
- Cleanup verification, when performed.

See `commands-explained.md` for command syntax, options, explanations and additional troubleshooting references.
