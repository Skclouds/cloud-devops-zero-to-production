# Scenario 04: Linux Permission and Access Failure

## Incident ID
INC-004

## Environment
- Ubuntu Linux 24.04 under WSL2
- Deployment user: deployer
- Primary user: kaushalsk07 (new PC)
- Application: permission-lab
- Test destination: /tmp/permission-lab/target

## Incident Description

A deployment process fails while copying application configuration.

Error:
Permission denied

## Environment Preparation

- Created application configuration.
- Created deployment user named deployer.
- Prepared isolated source and destination directories.
- Created deployment script.

## Investigation Evidence

Deployment user:
uid=1002(deployer)
gid=1003(deployer)

Source configuration:
- Owner: root
- Group: root
- Permissions: 644
- Read access: YES

Destination directory:
- Owner: root
- Group: root
- Permissions: 755
- Write access: NO

Deployment command:

sudo -u deployer /tmp/permission-lab/deploy.sh

Observed error:

Starting deployment...
cp: cannot create regular file:
Permission denied

Permission tests:

sudo -u deployer test -r /tmp/permission-lab/source/config.yaml
Exit code: 0

sudo -u deployer test -w /tmp/permission-lab/target
Exit code: 1

## Root Cause

The deployment user can read the source configuration but cannot
write to the destination directory.

The destination is owned by root:root with permissions 755.

## Proposed Remediation

1. Create an appdeploy group.
2. Add deployer to appdeploy.
3. Change destination ownership to root:appdeploy.
4. Apply chmod 2775 to the destination directory.
5. Verify group membership and directory permissions.
6. Retry deployment.
7. Verify deployed file ownership and content.

## Current Status

- Lab environment prepared: COMPLETE
- Permission failure reproduced: COMPLETE
- Root cause identified: COMPLETE
- Group-based remediation: PENDING
- Deployment recovery: PENDING
- Final verification: PENDING

## Lessons Learned

- File read permission and directory write permission are different.
- Directory write permission is needed to create files inside it.
- Linux checks ownership, group membership and permissions.
- Avoid chmod 777 as a deployment workaround.
- Diagnose before changing permissions.
