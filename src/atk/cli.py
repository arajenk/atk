import typer
from atk.wordle import game
app = typer.Typer()

@app.command()
def wordle():
    game.main()

def main():
    app()

