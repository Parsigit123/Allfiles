import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
#    with zipfile.ZipFile(dest_dir + "/" + "compressed.zip", 'w') as archive:
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, "r") as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
#    make_archive(filepaths=["filetobezipped1.txt", "filetobezipped2.txt"], dest_dir="dest")
     extract_archive("output.zip", dest_dir="files")
