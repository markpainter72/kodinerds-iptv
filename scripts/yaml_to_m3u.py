#!/usr/bin/env python

import yaml

def write_clean(content):
    with open("iptv/clean/clean.m3u", 'w') as file:
        file.write("#EXTM3U\n")
        for category_name, category in content.items():
            with open("iptv/clean/clean_" + category_name + ".m3u", 'w') as category_file:
                category_file.write("#EXTM3U\n")
                for subcategory_name, subcategory in category.items():
                    with open("iptv/clean/clean_" + category_name + "_" + subcategory_name + ".m3u", 'w') as subcategory_file:
                        subcategory_file.write("#EXTM3U\n")
                        for stream in subcategory:
                            stream_name = stream["name"]
                            header_line = "#EXTINF:-1 tvg-name=\"" + stream["tvg_name"] + "\" tvg-id=\"" + stream["tvg_id"] + "\" group-title=\"" + stream["group_title"] + "\" radio=\"" + str(stream["radio"]).lower() + "\" tvg-logo=\"" + stream["tvg_logo"] + "\"," + stream_name + "\n"
                            line = stream["url"] + "\n"
                            file.write(header_line)
                            file.write(line)
                            category_file.write(header_line)
                            category_file.write(line)
                            subcategory_file.write(header_line)
                            subcategory_file.write(line)

def write_kodi(content):
    with open("iptv/kodi/kodi.m3u", 'w') as file:
        file.write("#EXTM3U\n")
        for category_name, category in content.items():
            with open("iptv/kodi/kodi_" + category_name + ".m3u", 'w') as category_file:
                category_file.write("#EXTM3U\n")
                for subcategory_name, subcategory in category.items():
                    with open("iptv/kodi/kodi_" + category_name + "_" + subcategory_name + ".m3u", 'w') as subcategory_file:
                        subcategory_file.write("#EXTM3U\n")
                        for stream in subcategory:
                            stream_name = stream["name"]
                            header_line = "#EXTINF:-1 tvg-name=\"" + stream["tvg_name"] + "\" tvg-id=\"" + stream["tvg_id"] + "\" group-title=\"" + stream["group_title_kodi"] + "\" radio=\"" + str(stream["radio"]).lower() + "\" tvg-logo=\"" + stream["tvg_logo"] + "\"," + stream_name + "\n"
                            line = stream["url"] + "\n"
                            file.write(header_line)
                            file.write(line)
                            category_file.write(header_line)
                            category_file.write(line)
                            subcategory_file.write(header_line)
                            subcategory_file.write(line)

def write_pipe(content):
    with open("iptv/pipe/pipe.m3u", 'w') as file:
        file.write("#EXTM3U\n")
        for category_name, category in content.items():
            with open("iptv/pipe/pipe_" + category_name + ".m3u", 'w') as category_file:
                category_file.write("#EXTM3U\n")
                for subcategory_name, subcategory in category.items():
                    with open("iptv/pipe/pipe_" + category_name + "_" + subcategory_name + ".m3u", 'w') as subcategory_file:
                        subcategory_file.write("#EXTM3U\n")
                        for stream in subcategory:
                            stream_name = stream["name"]
                            header_line = "#EXTINF:-1 tvg-name=\"" + stream["tvg_name"] + "\" tvg-id=\"" + stream["tvg_id"] + "\" group-title=\"" + stream["group_title"] + "\" radio=\"" + str(stream["radio"]).lower() + "\" tvg-logo=\"" + stream["tvg_logo"] + "\"," + stream_name + "\n"
                            service_name = stream_name.replace("Ä", "Ae")
                            service_name = service_name.replace("ä", "ae")
                            service_name = service_name.replace("Ö", "Oe")
                            service_name = service_name.replace("ö", "oe")
                            service_name = service_name.replace("Ü", "Ue")
                            service_name = service_name.replace("ü", "ue")
                            service_name = service_name.replace(" ", "\ ")
                            line = "pipe://ffmpeg -loglevel fatal -i " + stream["url"] + " -vcodec copy -acodec copy -metadata service_name=" + service_name + " -metadata service_provider=" + stream["group_title"] + " -mpegts_service_type advanced_codec_digital_hdtv -f mpegts pipe:1\n"
                            file.write(header_line)
                            file.write(line)
                            category_file.write(header_line)
                            category_file.write(line)
                            subcategory_file.write(header_line)
                            subcategory_file.write(line)
    

with open("iptv/source.yaml", 'r') as file:
    try:
        content = yaml.safe_load(file)
        write_clean(content)
        write_kodi(content)
        write_pipe(content)
    except yaml.YAMLError as exc:
        print(exc)