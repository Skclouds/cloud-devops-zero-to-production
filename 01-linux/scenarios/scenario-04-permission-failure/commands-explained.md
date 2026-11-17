# Scenario 04 — Linux Permissions and Access Control: Command Reference

## 1. Identify the current user and groups

### `whoami`

**Purpose:** Displays the effective username.

```bash
whoami
```

**Why:** To identify which account is executing commands.

### `id`

**Purpose:** Displays user ID, primary group and supplementary groups.

```bash
id
id deployer
```

**Important fields:**
- `uid`: user ID.
- `gid`: primary group ID.
- `groups`: primary and supplementary group memberships.

**Why:** To verify whether the deployment account belongs to the required group.

**Important:** Group membership changes may not appear in an already-running login session. Check the account with `id username`, and start a fresh session when testing normal login behavior.

## 2. Create users and groups

### `useradd`

**Purpose:** Creates a Linux user account.

```bash
sudo useradd -m deployer
```

**Options:**
- `-m`: creates the user's home directory.

**Why:** We created a dedicated deployment identity instead of running the application deployment as root.

### `groupadd`

**Purpose:** Creates a Linux group.

```bash
sudo groupadd appdeploy
```

**Why:** We created a dedicated group to control access to the deployment directory.

**Safer repeatable check:**

```bash
getent group appdeploy || sudo groupadd appdeploy
```

`getent` checks the system's configured account databases. The group is created only if it does not already exist.

### `getent`

**Purpose:** Queries configured system databases such as users and groups.

```bash
getent group appdeploy
getent passwd deployer
```

**Why:** To verify that the group and user exist.

### `usermod -aG`

**Purpose:** Modifies an existing user account.

```bash
sudo usermod -aG appdeploy deployer
```

**Options:**
- `-a`: appends supplementary group membership.
- `-G`: specifies supplementary groups.

**Why:** To add the deployment user to the dedicated deployment group.

**Critical warning:** Using `-G` without `-a` can replace the user's existing supplementary group list. Use `-aG` when adding a group without removing existing memberships.

Verify:

```bash
id deployer
```

Expected group membership includes `appdeploy`.

## 3. Inspect directories and files

### `ls -l`

**Purpose:** Displays file permissions, ownership, size and modification information.

```bash
ls -l /tmp/permission-lab/target
ls -ld /tmp/permission-lab/target
```

**Options:**
- `-l`: long listing.
- `-d`: displays the directory itself rather than its contents.

**Why:** To inspect directory ownership and permissions.

### Understanding permission notation

Example:

```text
drwxrwsr-x
```

Breakdown:

- `d`: directory.
- `rwx`: owner can read, write and traverse.
- `rws`: group can read, write and traverse; the `s` indicates setgid.
- `r-x`: others can read and traverse, but cannot write.

For a directory:
- `r`: list directory entries.
- `w`: create, remove or rename entries, subject to other restrictions.
- `x`: traverse/search the directory.

Directory execute permission is not the same as file execute permission.

### `namei -l`

**Purpose:** Displays each component of a pathname and its permissions.

```bash
namei -l /tmp/permission-lab/target
```

**Options:**
- `-l`: uses long-format permission and ownership information.

**Why:** To investigate every directory in the path.

A user needs execute/traverse permission on each parent directory to reach a target. The final directory's permissions determine whether the user can create entries there.

## 4. Change ownership

### `chown`

**Purpose:** Changes file or directory owner and group.

```bash
sudo chown root:appdeploy /tmp/permission-lab/target
```

**Syntax:**

`chown OWNER:GROUP PATH`

In this case:
- Owner: `root`
- Group: `appdeploy`
- Path: deployment target directory

**Why:** We retained root as the directory owner but assigned the deployment group.

### Verify ownership

```bash
stat -c 'Owner: %U | Group: %G | Mode: %a (%A)' \
  /tmp/permission-lab/target
```

**Options:**
- `-c`: specifies a custom output format.
- `%U`: owner username.
- `%G`: group name.
- `%a`: numeric permission mode.
- `%A`: symbolic permission mode.

## 5. Change permissions

### `chmod`

**Purpose:** Changes file and directory permission bits.

Initial directory permissions:

```bash
sudo chmod 755 /tmp/permission-lab/target
```

`755` means:
- Owner: `rwx` (7)
- Group: `r-x` (5)
- Others: `r-x` (5)

The deployment user could traverse the directory but could not create files in it.

Recovery command:

```bash
sudo chmod 2775 /tmp/permission-lab/target
```

`2775` consists of:
- `2`: setgid special permission.
- `7`: owner `rwx`.
- `7`: group `rwx`.
- `5`: others `r-x`.

**Why:** The deployment group received write access, and the directory's setgid bit caused new entries to inherit the directory group.

### Understanding setgid on directories

When setgid is set on a directory:
- New files normally inherit the directory's group.
- New subdirectories inherit the group.
- New subdirectories generally inherit the setgid bit as well.

**Important:** Setgid group inheritance does not automatically grant group-write permission on new files. The file creation mode and umask still matter.

### More restrictive production alternative

```bash
sudo chmod 2770 /tmp/permission-lab/target
```

`2770` allows access to the owner and group, but denies access to others.

Use a permission mode based on the actual application and deployment access requirements. Do not blindly apply `2775` to sensitive production directories.

## 6. Test access as another user

### `sudo -u`

**Purpose:** Executes a command as another user.

```bash
sudo -u deployer id
sudo -u deployer /tmp/permission-lab/deploy.sh
```

**Options:**
- `-u`: specifies the user identity.

**Why:** To reproduce the deployment using the deployment account rather than the administrator account.

### `test -r`

**Purpose:** Tests whether a file is readable by the current user.

```bash
sudo -u deployer test -r \
  /tmp/permission-lab/source/config.yaml

echo $?
```

Exit code:
- `0`: readable.
- Non-zero: not readable.

### `test -w`

**Purpose:** Tests whether a file or directory is writable by the current user.

```bash
sudo -u deployer test -w /tmp/permission-lab/target

echo $?
```

Exit code:
- `0`: writable.
- Non-zero: not writable.

**Why:** We proved that the source file was readable while the original target directory was not writable.

### `test -x`

**Purpose:** Tests execute permission on a file or search/traverse permission on a directory.

```bash
sudo -u deployer test -x /tmp/permission-lab/target
echo $?
```

## 7. Deployment and file operations

### `mkdir -p`

**Purpose:** Creates directories, including missing parent directories.

```bash
sudo mkdir -p /tmp/permission-lab/source \
  /tmp/permission-lab/target
```

**Options:**
- `-p`: creates parent directories when needed and does not fail merely because the directory already exists.

### `cp`

**Purpose:** Copies files or directories.

```bash
sudo cp source/config.yaml target/config.yaml
```

**Why:** The deployment script used `cp` to copy the configuration into the target directory.

**Common errors:**
- `Permission denied`: insufficient access to a path or destination.
- `cannot stat`: source path cannot be found or accessed.
- `No such file or directory`: a required path component is missing.

Do not confuse a missing source file with a permissions failure.

### `chmod 644`

**Purpose:** Sets ordinary file permissions.

```bash
sudo chmod 644 /tmp/permission-lab/source/config.yaml
```

`644` means:
- Owner: read and write.
- Group: read.
- Others: read.

### `sudo tee`

**Purpose:** Writes standard input to a file, allowing privileged file creation when invoked with sudo.

Example:

```bash
printf '%s\n' '#!/bin/bash' \
  | sudo tee /tmp/permission-lab/example.sh
```

**Why:** We used privileged file creation when the normal user could not write into the root-owned lab directory.

## 8. Verify deployment

```bash
ls -l /tmp/permission-lab/target/config.yaml

stat -c 'Owner: %U | Group: %G | Mode: %a (%A)' \
  /tmp/permission-lab/target/config.yaml

cat /tmp/permission-lab/target/config.yaml

diff -u \
  /tmp/permission-lab/source/config.yaml \
  /tmp/permission-lab/target/config.yaml
```

**Commands:**
- `cat`: displays file content.
- `diff -u`: compares files and shows differences in unified format.

If `diff` produces no output and exits with status `0`, the files match.

## 9. Important additional reference

These commands are useful in more advanced Linux permission investigations. They were not all confirmed as executed in this scenario.

### `umask`

Displays or sets the default permission mask for newly created files and directories.

```bash
umask
umask 0002
```

A typical `umask 0022` results in:
- Files created with a requested mode of 666 becoming 644.
- Directories created with a requested mode of 777 becoming 755.

A `umask 0002` commonly permits group-write on newly created files and directories, subject to the requested creation mode.

### `getfacl`

Displays access control lists.

```bash
getfacl /path/to/directory
```

### `setfacl`

Changes access control lists.

```bash
setfacl -m g:appdeploy:rwx /path/to/directory
```

These ACL commands require the ACL utilities to be installed and filesystem support to be available.

### `chmod -R`

Applies permissions recursively.

Use extreme caution. Recursive permission changes can break applications and expose sensitive files.

## 10. Production troubleshooting workflow

1. Identify the exact user running the deployment.
2. Inspect user and supplementary group membership.
3. Inspect the full directory path using `namei -l`.
4. Check source-file readability.
5. Check destination-directory write and traversal permissions.
6. Inspect ownership and permission bits.
7. Apply the smallest suitable ownership or permission change.
8. Re-run the operation as the deployment identity.
9. Verify resulting ownership, group, mode and content.
10. Document the change and review whether access is broader than necessary.

## 11. Key distinctions

- `chown`: changes ownership.
- `chmod`: changes permission bits.
- `usermod -aG`: adds supplementary group membership.
- `setgid` on a directory: controls group inheritance for new entries.
- `umask`: masks permissions requested when new files or directories are created.
- `test -r`: checks read access.
- `test -w`: checks write access.
- `namei -l`: helps identify permission problems in every path component.
