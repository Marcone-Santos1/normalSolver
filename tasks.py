from invoke import task


@task
def set_version(c):
    c.run("python version.py")
