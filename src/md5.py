__all__ = ["create_md5_checksum"]


def create_md5_checksum(file_name: str) -> str:
    """ create hash based on contents of the files """
    from hashlib import md5
    with open(file_name, "rb") as f:
        data = f.read()
        file_hash = md5(data).hexdigest()
    return file_hash
   