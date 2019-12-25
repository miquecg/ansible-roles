Arch Linux container
====================

Creates an Arch Linux container from latest bootstrap tarball available.

Requirements
------------

This role uses [`buildah`](https://github.com/containers/buildah/blob/master/install.md), a tool for building OCI images.

Elevated privileges are needed to create the root filesystem.

Role Variables
--------------

### defaults

```yaml
archive_url: https://archive.archlinux.org/iso
download_path: "{{ playbook_dir }}"
```

### facts
This role sets two facts during execution.

**`bootstrap_release`**

Date formatted as '%Y.%m.01'.

**`working_container`**

Container ID. It's dynamically allocated to avoid collisions with any other existing container in the environment (e.g. previously created by this role).

License
-------

See [LICENSE](https://github.com/miquecg/ansible-roles/blob/master/LICENSE).
