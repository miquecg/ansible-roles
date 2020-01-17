Common setup
============

Common system setup tasks.

Tasks
-----

This role offers the following tasks:
- locale
- nameservers
- timezone

`main.yml` does not include any. Load them on your playbook using `tasks_from`.

Role Variables
--------------

### defaults

```yaml
locale: en_US.UTF-8
nameservers:
  default: 1.1.1.1
  secondary: 8.8.8.8
```

### required

**`timezone`**

Must be a valid timezone available at `/usr/share/zoneinfo` (e.g. Europe/Berlin). Required by `timezone.yml` task.

License
-------

See [LICENSE](https://github.com/miquecg/ansible-roles/blob/master/LICENSE).
