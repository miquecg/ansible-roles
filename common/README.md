Common setup
============

Common system setup tasks.

Tasks
-----

`main.yml` does not include any. Load them on your playbook using `tasks_from`.

- locale
- timezone

Role Variables
--------------

### defaults

```yaml
system_locale: en_US.UTF-8
```

### required

**`timezone`**

Must be a valid timezone available at `/usr/share/zoneinfo` (e.g. Europe/Berlin).

### optional

**`locale`**

Alternative locale to generate on the system. When this value is supplied no system locale is set.

License
-------

See [LICENSE](https://github.com/miquecg/ansible-roles/blob/master/LICENSE).
