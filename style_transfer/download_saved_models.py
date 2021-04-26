import zipfile

save_location = "style_transfer/images/saved_models.zip"

try:
    from torch.utils.model_zoo import _download_url_to_file
except ImportError:
    try:
        from torch.hub import download_url_to_file as _download_url_to_file
    except ImportError:
        from torch.hub import _download_url_to_file


def unzip(source_filename, dest_dir):
    with zipfile.ZipFile(source_filename) as zf:
        zf.extractall(path=dest_dir)


if __name__ == "__main__":
    _download_url_to_file(
        "shorturl.at/xBKX6",
        save_location,
        None,
        True,
    )
    unzip(save_location, ".")
