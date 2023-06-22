from mutagen import File


def extract(address):
    audio = File(address)
    if "APIC:" in audio:
        cover_art = audio["APIC:"].data
        return cover_art

    else:
        return None


# extract("G:\music/Ed_Sheeran_-_Perfect_47828368.mp3")
