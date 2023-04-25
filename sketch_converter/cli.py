import typer

from sketch_converter import __copyright__, __version__
from sketch_converter.sketch import (
    CameraColorPencilSketch,
    CameraGrayPencilSketch,
    ImageColorPencilSketch,
    ImageGrayScalePencilSketch,
)

app = typer.Typer()


@app.command()
def version():
    print(f"Sketch Converter - {__version__}")
    print(__copyright__)


@app.command()
def video_capture_grayscale(videosrc: int = 0) -> None:
    print(f"Video mode(Grayscale): {videosrc}")
    CameraGrayPencilSketch(videosrc)
    return


@app.command()
def video_capture_color(videosrc: int = 0) -> None:
    print(f"Video mode(Colorful): {videosrc}")
    CameraColorPencilSketch(videosrc)
    return


@app.command()
def convert_to_gray_pencil_sketch(image_file: str) -> None:
    if image_file is not None or image_file != "":
        print(f"Picture mode(GrayScale): {image_file}")
        files: list[str] = []
        files.append(image_file)
        ImageGrayScalePencilSketch(files)
    return


@app.command()
def convert_to_color_pencil_sketch(image_file: str) -> None:
    if image_file is not None or image_file != "":
        print(f"Picture mode(Colorful): {image_file}")
        files: list[str] = []
        files.append(image_file)
        ImageColorPencilSketch(files)
    return


if __name__ == "__main__":
    app()
