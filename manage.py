<<<<<<< HEAD
#!/usr/bin/env python3.4
=======
#!/usr/bin/env python
>>>>>>> 8052b7ec016c37e91a9217b06d5337059ac7581f
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sandd.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
