import os
import gdown

def download_files(load_all=False):
    files_to_download = {
        "movies_dict.pkl": "1RNcXlMl_Pe5v2dPeJ0JIM_KoeDQpKoAK",
        "movies2_dict.pkl": "1PIkyf7WCx3ZAPhTFAHcKjTcIjsHGxaRA",
        "new_df_dict.pkl": "1IqR-E_IqlM1bWUWWUSNZL0yzUmfCigf_",
        "similarity_tags_genres.pkl": "1JL4Qfv13XN4BYtfeo269QxlloZVXFNjw",
        "similarity_tags_keywords.pkl": "1N1DUmYT60FWTQGucpOjdh5bBsaZxJlGN",
        "similarity_tags_tags.pkl": "1-fHq7RQjhf4gQ3NQDS76U2qg0Is10RNF",
        "similarity_tags_tcast.pkl": "1CI57xekM3r_cIOhj7gJFwt-_FHB-tALX",
        "similarity_tags_tprduction_comp.pkl": "127bAKeoq9PKPHABP0uBnDdJIeXtd5-k4",
    }

    # Directory to save downloaded files
    download_dir = r"D:/Movie-Recommender-System/Files"
    os.makedirs(download_dir, exist_ok=True)

    # Download files if not already present
    for filename, file_id in files_to_download.items():
        output_path = os.path.join(download_dir, filename)
        if not os.path.exists(output_path):  # Avoid re-downloading
            print(f"Downloading {filename}...")
            gdown.download(f"https://drive.google.com/uc?id={file_id}", output_path, quiet=False)

    print("All files are downloaded successfully.")

download_files()