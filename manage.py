#!/usr/bin/env python3.4
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sandd.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
