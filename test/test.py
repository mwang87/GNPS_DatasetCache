import sys
sys.path.insert(0, "..")

def test():
    import requests
    import requests_cache
    import compute_tasks

    requests_cache.install_cache('demo_cache')

    from models import Filename
    Filename.create_table(True)

    # Query 
    #compute_tasks.populate_ftp()

def test_parsing():
    all_paths = []
    all_paths.append("MSV000082975/peak/Kermit_20130425_PB_Nadine_U2_01.mzML")
    all_paths.append("MSV000084314/updates/2020-10-08_mwang87_d7c866dd/other/MGF/MSV000078547.mgf")

    for msv_path in all_paths:
        collection_name, is_update, update_name = compute_tasks._get_file_metadata(msv_path)
        print(collection_name, is_update, update_name)

def test_dataset_files():
    import utils
    all_files = utils._get_massive_files("MSV000086709", acceptable_extensions=[])
    print("FTP", len(all_files))

    all_files = utils._get_massive_files("MSV000086709", acceptable_extensions=[], method="http")
    print("HTTP", len(all_files))


def main():
    #test()
    #test_parsing()
    test_dataset_files()

if __name__ == "__main__":
    main()