import os
import getpass


print("Example input: make --jobs=4 TARGET_BITS=64 DISCORD_SDK=1 COOPNET=1 HEADLESS=0 RENDER_API=GL WINDOW_API=SDL2")
jobs = input("--jobs[1,2,3,4,...] Jobs amount, may speed up compilation. ", )
target_bits = input("TARGET_BITS [32|64] Compile to 32-bit or 64-bit. ", )
discord_sdk = input("DISCORD_SDK [0|1] Enable or disable Discord Game SDK. ", )
coopnet = input("COOPNET [0|1] Enable or disable the CoopNet networking system. ", )
headless = input("HEADLESS [0|1] Enable or disable headless mode (meant for servers). ", )
render_api = input("RENDER_API [GL|GL_LEGACY|D3D11|D3D12|DUMMY] Sets the rendering API. ", )
window_api = input("WINDOW_API [SDL1|SDL2|DXGI|DUMMY] Sets the window API. ", )


final_jobs = " --jobs="+jobs
final_target_bits = " TARGET_BITS="+target_bits
final_discord_sdk = " DISCORD_SDK="+discord_sdk
final_coopnet = " COOPNET="+coopnet
final_headless = " HEADLESS="+headless
final_render_api = " RENDER_API="+render_api
final_window_api = " WINDOW_API="+window_api
user = getpass.getuser()
command1 = "cd /home/"+user+" && git clone https://github.com/coop-deluxe/sm64coopdx.git"
command2 = "cd /home/"+user+"/sm64coopdx && make"+final_jobs+final_target_bits+final_discord_sdk+final_coopnet+final_headless+final_render_api+final_window_api


os.system(command1)
input("Copy a us rom of super mario 64 into the new sm64coopdx directory and rename the rom file to baserom.us.z64 and after that press enter")
os.system(command2)


def debug():
    print("jobs amount:", jobs)
    print("final output: --jobs=",jobs)
    print("target bits:", target_bits)
    print("final output: TARGET_BITS="+target_bits)
    print("discord sdk:", discord_sdk)
    print("final output: DISCORD_SDK="+discord_sdk)
    print("coopnet:", coopnet)
    print("final output: COOPNET="+coopnet)
    print("headless:", headless)
    print("final output: HEADLESS="+headless)
    print("render api:", render_api)
    print("final output: RENDER_API="+render_api)
    print("window api:", window_api)
    print("final output: WINDOW_API="+window_api)
    print(command1)
    print(command2)
