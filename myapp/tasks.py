from time import sleep

def foo(sec):
    print("We are now inside the foo")
    sleep(sec)
    print("Foo endeds")


def hook_after_foo(task):
    print("Task: ",task)
    print("We are now inside the hook.")
