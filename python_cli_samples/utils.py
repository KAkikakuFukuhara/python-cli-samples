from typing import Any


def show_dict(dict_:dict[str, Any], title="kwargs"):
    if len(dict_) == 0:
        return

    print(f"┌─{title}{'─'*5}")
    for k, v in dict_.items():
        print(f"│- {k}")
        print(f"│\t-{v}")
    print(f"└─{'─'*5}")