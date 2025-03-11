from invoke import task


@task
def nburl(c):
    print("Jupyter Notebook URL")
    c.run(
        'docker logs jupyter 2>&1 | grep "token=" | grep -v "ServerApp" | sed "s/127.0.0.1/jupyter/" | grep jupyter | sed "s/^[ \t]*//" | sed "s/[ \t]*$//"'
    )
