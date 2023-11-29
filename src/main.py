from graph_onedrive import OneDrive

from graph_onedrive import OneDriveManager

# Use a context manager to manage the session
with OneDriveManager(config_path="config.json", config_key="onedrive") as my_drive:
    # Print the OneDrive usage
    my_drive.get_usage(verbose=True)

    # Upload a file to the root directory
    new_file_id = my_drive.upload_file("my-photo.jpg", verbose=True)
