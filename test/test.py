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


def test_download_conversion():
    import utils_conversion

    test_cases = []

    #test_cases.append("mzspec:MSV000091523:raw/piper_01_RA1_1_1681.d") # Bruker TIMS
    #test_cases.append("mzspec:MSV000094299:raw/RSC_LVManuscript_RawData/LV_Exp2/MS2-LV_Media_pos_2.d") # Agilent
    #test_cases.append("mzspec:MSV000088206:raw/M1_T21_325_2000_positive.d") # Agilent
    test_cases.append("mzspec:MSV000093589:raw/Jugione_A.d") # Agilent
    #test_cases.append("mzspec:MTBLS108:FILES/Lut_A_220d.raw") # Raw
    

    for test_mri in test_cases:
        print(test_mri)
        utils_conversion.download_mri(test_mri, "./tmp", cache_url="http://169.235.26.140:5234")


def main():
    #test()
    #test_parsing()
    #test_dataset_files()
    test_download_conversion()

if __name__ == "__main__":
    main()