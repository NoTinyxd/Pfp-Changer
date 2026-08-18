from pathlib import Path
import base64
import glob
import random
import base64
import mimetypes



def get_pfps():
    pfp_dir = Path(__file__).resolve().parents[1] / "Input" / "pfps"
    pfps = (
        glob.glob(str(pfp_dir / "*.png")) +
        glob.glob(str(pfp_dir / "*.jpg")) +
        glob.glob(str(pfp_dir / "*.jpeg"))+
        glob.glob(str(pfp_dir / "*.webp"))
    )
    pfp = random.choice(pfps)
    with open(pfp, "rb") as f:
        pfp_string = base64.b64encode(f.read()).decode()
    mime_type = mimetypes.guess_type(pfp)[0] or "application/octet-stream"
    data_uri=f"data:{mime_type};base64,{pfp_string}"
    pfp_name = Path(pfp).stem
    return data_uri,pfp_name


    


