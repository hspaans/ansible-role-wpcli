# Role Name

Installs [WP-CLI](https://wp-cli.org), the command-line interface for [WordPress](https://wordpress.org).

## Requirements

Requires PHP to be installed for WP-CLI to function and Bash with completion for users who want command completion on the command-line.

## Role Variables

Default variables are set in `defaults/main.yml` to match the WP-CLI and role version.

## Dependencies

No dependency on other Ansible Galaxy roles.

## Example Playbook

```yaml
---
- hosts: servers
  roles:
    - { role: hspaans.wpcli, become: true }
```

## License

MIT

## Author Information

This role was created in 2020 by [Hans Spaans](https://github.com/hspaans).
