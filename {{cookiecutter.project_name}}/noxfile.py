import nox

versions = ["3.7", "3.8", "3.9", "3.10"]


@nox.session(python=versions)
def tests(session):
    session.run("poetry", "install", external=True)
    session.run("poetry", "run", "coverage", "run")
    session.run("poetry", "run", "coverage", "report")
    session.run("poetry", "run", "coverage", "html")


@nox.session(python=versions)
def lints(session):
    session.run("poetry", "run", "black", ".")
    session.run("poetry", "run", "pylint", "{{cookiecutter.project_name}}")
