import typer

from sketchconverter import __version__

from .sketch import CameraProcess, ImageProcess

app = typer.Typer()


@app.command()
def version():
    print(f"Sketch Converter - {__version__}")


@app.command()
def video_capture(videosrc: int = 0, pgcolor: int = 1, pscolor: int = 0) -> None:
    if videosrc >= 0:
        if pgcolor == 1 and pscolor == 1:
            print("Grayscale and Colorful Pencil Sketch can't use at the same time")
            return
        print(f"Video mode: {videosrc}")
        CameraProcess(pgcolor, pscolor, videosrc)
    return


@app.command()
def picture_capture(image_file: str, pgcolor: int, pscolor: int) -> None:
    if image_file is not None or image_file != "":
        if pgcolor == 1 and pscolor == 1:
            print("Grayscale and Colorful Pencil Sketch can't use at the same time")
            return
        print(f"Picture mode: {image_file}")
        files: list[str] = []
        files.append(image_file)
        ImageProcess(files, pgcolor, pscolor)
    return


if __name__ == "__main__":
    app()
