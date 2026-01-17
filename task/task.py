from collections import namedtuple


Task = namedtuple("Task",
                  ["summary", "owner", "done", "id"])
Task.__new__.__defaults__ = (None, None, False, None)


if __name__ == "__main__":
    task = Task()
    print(task)