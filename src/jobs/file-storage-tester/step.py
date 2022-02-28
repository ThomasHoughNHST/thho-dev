from hough_azure import file_storage_helper


def run_step():
    fsh = file_storage_helper.get_file_storage_helper()
    keyvault = fsh.get_keyvault()


if __name__ == '__main__':
    run_step()
