name = "shotgrid"
title = "Shotgrid"
version = "0.4.1-dev.1"
client_dir = "ayon_shotgrid"

services = {
    "ShotgridLeecher": {
        "image": f"ynput/ayon-shotgrid-leecher:{version}"},
    "ShotgridProcessor": {
        "image": f"ynput/ayon-shotgrid-processor:{version}"},
    "ShotgridTransmitter": {
        "image": f"ynput/ayon-shotgrid-transmitter:{version}"},
}
