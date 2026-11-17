# Scenario 03 — Disk and Inode Exhaustion: Command Reference

## 1. Inspect filesystem capacity

### `df -h`

**Purpose:** Displays filesystem space usage in human-readable units.

```bash
df -h
```

**Options:**
- `-h`: human-readable sizes such as MiB and GiB.

**Important columns:**
- `Filesystem`: device or filesystem name.
- `Size`: total filesystem capacity.
- `Used`: space consumed.
- `Avail`: available space.
- `Use%`: percentage of blocks used.
- `Mounted on`: mount point.

**Why we used it:** To establish the disk-space baseline and verify block exhaustion.

**Interpretation:** A filesystem at 100% block usage may be unable to allocate additional file data.

### `df -i`

**Purpose:** Displays inode usage.

```bash
df -i
```

**Important columns:**
- `Inodes`: total inode count.
- `IUsed`: allocated inodes.
- `IFree`: free inodes.
- `IUse%`: percentage of inodes used.

**Why we used it:** To distinguish inode exhaustion from block exhaustion.

**Important:** A filesystem can have free disk capacity but no free inodes. Creating another file can then fail.

### `findmnt`

**Purpose:** Displays mounted filesystems and their relationships.

```bash
findmnt
findmnt /
```

**Why we used it:** To identify the filesystem backing the root mount and understand the environment.

**Useful information:**
- Source device
- Target mount point
- Filesystem type
- Mount options

### `ls -lh`

**Purpose:** Displays file sizes in human-readable form.

```bash
ls -lh block-disk.img inode-disk.img
```

**Options:**
- `-l`: long listing with ownership, permissions and size.
- `-h`: human-readable size.

**Important:** A sparse file can have a large logical size but consume much less physical storage. `ls -lh` shows the logical file size, not necessarily the allocated blocks.

### `du -sh`

**Purpose:** Reports disk usage of files or directories.

```bash
du -sh /path/to/directory
```

**Options:**
- `-s`: summary only.
- `-h`: human-readable units.

**Why we used it:** To inspect the space consumed by files.

**Important:** `du` measures space used by visible filesystem objects it can traverse. It can differ from `df`, for example when deleted files remain open by running processes.

## 2. Check available utilities

The lab checked whether required filesystem utilities were available.

### `command -v`

**Purpose:** Identifies the executable that would be run for a command.

```bash
command -v mkfs.ext4
command -v mount
command -v losetup
command -v fallocate
```

**Why:** To confirm that the environment had the utilities needed for loopback filesystem experiments.

## 3. Create loopback disk images

A loopback disk image is an ordinary file used as a virtual block device for filesystem testing.

### `fallocate`

**Purpose:** Allocates space for a file.

Example reproducible commands:

```bash
mkdir -p ~/devops-lab/scenario-03/images
fallocate -l 64M ~/devops-lab/scenario-03/images/block-disk.img
fallocate -l 32M ~/devops-lab/scenario-03/images/inode-disk.img
```

**Options:**
- `-l`: sets the file length.

**Why:** To create small disk-image files for isolated filesystem experiments.

**Important:** Filesystem, host and storage behavior can affect whether allocation is physically reserved. Confirm actual allocation with `du` and `ls`.

## 4. Create ext4 filesystems

### `mkfs.ext4`

**Purpose:** Creates an ext4 filesystem on a device or image.

Example commands for reproducing the lab:

```bash
sudo mkfs.ext4 ~/devops-lab/scenario-03/images/block-disk.img

sudo mkfs.ext4 -N 128 -m 0 \
  ~/devops-lab/scenario-03/images/inode-disk.img
```

**Options:**
- `-N 128`: requests a filesystem with 128 inodes.
- `-m 0`: reserves 0% of filesystem blocks for the privileged user.

**Why:** The second filesystem was deliberately created with a very small inode count so inode exhaustion could be reproduced quickly.

**Warning:** `mkfs.ext4` creates a filesystem and can destroy existing filesystem data on its target. Use only disposable lab images or devices.

## 5. Attach image files to loop devices

### `losetup`

**Purpose:** Associates a regular file with a loop device.

Typical command:

```bash
sudo losetup --find --show \
  ~/devops-lab/scenario-03/images/block-disk.img
```

**Options:**
- `--find`: finds an unused loop device.
- `--show`: prints the assigned loop-device path.

Example output may look like `/dev/loop0`. The actual device number can differ.

Inspect loop devices:

```bash
sudo losetup -a
```

## 6. Mount and inspect the filesystems

### `mount`

**Purpose:** Attaches a filesystem to a directory in the Linux directory tree.

Example:

```bash
sudo mkdir -p ~/devops-lab/scenario-03/mounts/block-test
sudo mount /dev/loop0 \
  ~/devops-lab/scenario-03/mounts/block-test
```

The inode image must be attached to its own loop device and mounted at its own mount point.

**Important:** Mounting makes the filesystem accessible through the selected directory. The mount point must exist.

### `chown`

**Purpose:** Changes file or directory ownership.

Command used to make the lab mount directories writable by the regular lab user:

```bash
sudo chown "$USER:$USER" /path/to/mount-point
```

**Options:**
- `-R`: recursive ownership change, if explicitly needed.

**Why:** Newly mounted filesystem roots were root-owned, preventing the regular user from creating test files.

**Caution:** Avoid recursive ownership changes on production filesystem trees unless the impact is understood.

## 7. Reproduce block exhaustion

### `dd`

**Purpose:** Copies data from an input to an output.

Command used in the lab:

```bash
dd if=/dev/zero \
  of=mounts/block-test/large-file.bin \
  bs=1M count=80 status=progress
```

**Options and arguments:**
- `if=/dev/zero`: reads zero-filled data.
- `of=...`: destination file.
- `bs=1M`: reads and writes in 1 MiB blocks.
- `count=80`: attempts 80 blocks.
- `status=progress`: displays progress.

**Why:** To consume the small test filesystem's available data blocks.

**Observed result:** The write stopped with `No space left on device` after approximately 51 MiB had been written.

**Interpretation:** The filesystem had run out of allocatable data blocks. The inode report still showed many free inodes.

## 8. Reproduce inode exhaustion

### `touch`

**Purpose:** Creates empty files or updates file timestamps.

The lab attempted to create files in a loop, up to 150 files:

```bash
for i in $(seq 1 150); do
  touch "mounts/inode-test/file-$i" || break
done
```

**Commands and syntax:**
- `for`: starts a shell loop.
- `$(...)`: command substitution.
- `seq 1 150`: generates numbers from 1 through 150.
- `touch`: creates each file.
- `|| break`: stops the loop if file creation fails.

**Why:** Each newly created file requires an inode. The filesystem was deliberately created with only 128 inodes.

**Observed result:** Creation stopped at approximately file 118 with `No space left on device`.

The filesystem initially had 128 total inodes, 11 already used, and 117 free. Those 117 free inodes were consumed by the new files.

## 9. Verify the two failure modes

After reproducing block exhaustion:

```bash
df -h /path/to/block-test
df -i /path/to/block-test
du -sh /path/to/block-test
```

Expected pattern:
- Block usage near 100%.
- Inodes still mostly available.

After reproducing inode exhaustion:

```bash
df -h /path/to/inode-test
df -i /path/to/inode-test
```

Expected pattern:
- Inode usage at or near 100%.
- Block capacity may still be available.

## 10. Additional troubleshooting reference

These commands are useful for production investigations. They were not all confirmed as executed in this lab.

### `lsof +L1`

Finds open files that have been deleted but are still held open by processes.

Such files can continue consuming disk space even though they no longer appear in directory listings.

### `du --inodes`

Reports inode consumption by directory.

Example:

```bash
sudo du --inodes -x -d 3 /var | sort -nr
```

Options:
- `--inodes`: reports inode counts rather than byte usage.
- `-x`: stays on one filesystem.
- `-d 3`: limits directory depth to three levels.
- `sort -nr`: sorts numerically in reverse order.

### `find`

Can locate large files or large numbers of small files.

Example:

```bash
sudo find /var -xdev -type f | wc -l
```

### `umount`

Detaches a mounted filesystem.

```bash
sudo umount /path/to/mount-point
```

Do not unmount a filesystem while processes are actively using it.

### `losetup -d`

Detaches a loop device after its filesystem has been unmounted.

```bash
sudo losetup -d /dev/loop0
```

### `rm`

Removes files.

```bash
rm /path/to/test-file
```

Use caution. Confirm the target path before deleting files.

## 11. Production troubleshooting workflow

1. Identify the affected mount point.
2. Run `df -h` to check block usage.
3. Run `df -i` to check inode usage.
4. Use `findmnt` to identify the filesystem and mount source.
5. Use `du` or `du --inodes` to locate consumption.
6. Check for deleted-but-open files with `lsof +L1` if `df` and `du` disagree.
7. Identify safe cleanup candidates and confirm ownership.
8. Remediate without deleting application data blindly.
9. Verify both block and inode availability.
10. Check application behavior and logs.

## 12. Key distinction

**Block exhaustion:** The filesystem cannot allocate more data blocks.

**Inode exhaustion:** The filesystem cannot allocate another inode for a new filesystem object.

Both can produce `No space left on device`, but they are different resource failures and must be investigated separately.
