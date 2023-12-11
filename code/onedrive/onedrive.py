from graph_onedrive import OneDriveManager

def upload_to_onedrive(file_path, destination_folder):
    with OneDriveManager(config_path="config.json", config_key="onedrive") as my_drive:
        dst_folder_detail = my_drive.detail_item_path(destination_folder)
        new_file_id = my_drive.upload_file(file_path, verbose=True)
        my_drive.move_item(new_file_id, dst_folder_detail["id"])
        my_drive.to_file("config.json", "onedrive")



