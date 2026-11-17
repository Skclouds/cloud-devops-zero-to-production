# Scenario 04 — Linux Permission and Deployment Failure

## Scenario objective

Simulate a deployment failure caused by Linux directory permissions, identify the exact access-control problem, and recover the deployment using a dedicated group.

## Environment

- Original lab environment: Ubuntu under WSL2
- Host used for restored documentation and recovery: DESKTOP-MKUE3GK
- Deployment account: `deployer`
- Deployment group: `appdeploy`
- Source: `/tmp/permission-lab/source/config.yaml`
- Target: `/tmp/permission-lab/target`
- Script: `/tmp/permission-lab/deploy.sh`

## Initial permission configuration

The lab used:

- Source configuration owned by `root:root`, mode `644`.
- Target directory owned by `root:root`, mode `755`.

This allowed the deployment account to read the source file but not write into the target directory.

## Incident simulation

The deployment was executed as the deployment user:

```bash
sudo -u deployer /tmp/permission-lab/deploy.sh
```

Observed failure:

`cp: cannot create regular file '/tmp/permission-lab/target/config.yaml': Permission denied`

## Investigation

The following checks were performed:

```bash
id deployer

ls -ld /tmp/permission-lab/target

namei -l /tmp/permission-lab/target

sudo -u deployer test -r \
  /tmp/permission-lab/source/config.yaml
echo $?

sudo -u deployer test -w \
  /tmp/permission-lab/target
echo $?
```

The source readability test returned `0`.

The target writeability test returned `1`.

The directory was owned by `root:root` and had mode `755`. The deployment user could traverse the directory but could not create files inside it.

## Root cause

The deployment account did not have write permission on the destination directory.

The source file was readable, so the failure was not caused by source-file permissions.

## Remediation performed

The deployment user was created:

```bash
sudo useradd -m deployer
```

A dedicated group was created if it did not already exist:

```bash
getent group appdeploy || sudo groupadd appdeploy
```

The deployment user was added to the supplementary group:

```bash
sudo usermod -aG appdeploy deployer
```

The target directory ownership was changed:

```bash
sudo chown root:appdeploy /tmp/permission-lab/target
```

The directory permissions were changed:

```bash
sudo chmod 2775 /tmp/permission-lab/target
```

The resulting directory listing showed:

```text
drwxrwsr-x root appdeploy ... /tmp/permission-lab/target
```

The `s` in the group permission position confirms the directory's setgid bit.

The deployment account was verified to belong to `appdeploy`.

## Environment setup issue encountered during recovery

The first recovery attempt failed with:

`cp: cannot stat '/tmp/permission-lab/source/config.yaml': No such file or directory`

Investigation showed that the source directory did not exist in the restored lab environment.

This was a separate setup problem, not a recurrence of the original permission failure.

The source directory and configuration were restored from the repository. The source file was verified as readable by `deployer`.

## Successful recovery

The deployment was run again:

```bash
sudo -u deployer /tmp/permission-lab/deploy.sh
```

Observed output:

```text
Starting deployment...
Deployment successful
```

## Verification still required

The successful script output confirms that the copy operation completed. For full artifact verification, also inspect:

```bash
ls -l /tmp/permission-lab/target/config.yaml

stat -c 'Owner: %U | Group: %G | Mode: %a (%A)' \
  /tmp/permission-lab/target/config.yaml

cat /tmp/permission-lab/target/config.yaml

diff -u \
  /tmp/permission-lab/source/config.yaml \
  /tmp/permission-lab/target/config.yaml
```

The destination file's group should inherit `appdeploy` from the setgid directory. Its group-write bit is not guaranteed by setgid; it depends on the source mode and file creation behavior.

## Status

**Completed — deployment recovery and artifact verification succeeded.**

Verified destination:
- Owner: `deployer`
- Group: `appdeploy`
- Mode: `644` (`-rw-r--r--`)
- Source and destination comparison: `diff` exit code `0`

The destination inherited the `appdeploy` group from the setgid directory. The file is not group-writable, which is consistent with its resulting mode `644`.

## Production lessons

- Use a dedicated deployment identity rather than running all deployment operations as root.
- Grant access through narrowly scoped groups or ACLs.
- Directory write permission controls the ability to create or remove directory entries.
- Directory execute permission controls traversal.
- Setgid on directories helps maintain group ownership consistency.
- Setgid does not automatically make new files group-writable.
- Avoid broad recursive permission changes.
- Use the least privilege required by the deployment and application.

## Security consideration

The lab used `2775` to demonstrate group-based access and setgid inheritance.

For a sensitive production deployment directory, consider `2770` or an appropriate ACL so unrelated users cannot read directory contents.

## Evidence

Preserve actual outputs for:

- Initial directory ownership and permissions.
- `id deployer`.
- `namei -l` path inspection.
- Source read test and target write test.
- Group membership and updated directory permissions.
- Successful deployment.
- Final file ownership, mode and content comparison.

See `commands-explained.md` for detailed command syntax and explanations.
