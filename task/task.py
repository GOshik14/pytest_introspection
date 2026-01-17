from collections import namedtuple


Task = namedtuple("Task",
                  ["summary", "owner", "done", "id"])
Task.__new__.__defaults__ = (None, None, False, None)

def is_task(t: Task) -> bool:
    if not isinstance(t, Task):
        raise TypeError("Object type should be Task")   
    return True
    

if __name__ == "__main__":
    task = Task()
    print(task)