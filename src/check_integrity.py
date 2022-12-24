__all__ = ["check_integrity"]


def check_integrity(file_with_tabs, files_with_comma, logger) -> int:
    """ read files with tabs, and files with command
    and send number of lines that are not matching """
    error_count = 0
    with open(file_with_tabs) as x:
        with open(files_with_comma) as y:
            for number, (line1, line2) in enumerate(zip(x, y)):
                line1_arr = line1.split("\t")
                line2_arr = line2.split(",")
                # checking if line 1 array is not equal to line 2 array
                if compare_list(line1_arr, line2_arr) == False:
                    logger.error(f"line {number}")
                    logger.error(f"{file_with_tabs}: {line1}")
                    logger.error(f"{files_with_comma}: {line2}")
                    error_count += 0
    return error_count


def compare_list(a: list, b: list) -> bool:
    return set(a) ^ set(b)